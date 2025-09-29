import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import re

# BBC RSS Feed
URL = "https://feeds.bbci.co.uk/news/rss.xml"

# Function to scrape news
def fetch_news():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")

    news_data = []
    for item in items:
        title = item.title.text
        description = item.description.text
        link = item.link.text
        pub_date = item.pubDate.text
        news_data.append([title, description, pub_date, link])
    
    return pd.DataFrame(news_data, columns=["Title", "Description", "Publication Date", "Link"])

# Highlight search word
def highlight_text(text, word):
    if word:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        return pattern.sub(lambda m: f"<b><span style='background-color: yellow;'>{m.group(0)}</span></b>", text)
    return text

# Streamlit page config
st.set_page_config(page_title="BBC News Feed Dashboard", layout="wide")

# Sidebar styling
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #28a745;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    /* Make text input and selectbox text black */
    .stTextInput > div > div > input {
        color: black !important;
    }
    .stSelectbox > div > div > div > div {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar search panel
st.sidebar.title("🔍 Search Panel")
search_query = st.sidebar.text_input("Search by keyword:")

# Selectbox with black text using format_func
def format_option(option):
    return f"{option}"  # ensures black text

category_filter = st.sidebar.selectbox(
    "Search by column:", 
    ["All", "Title", "Description", "Publication Date"], 
    format_func=format_option
)

# Main heading
st.markdown("<h1 style='color: #28a745; text-align: center;'>BBC News Feed Dashboard</h1>", unsafe_allow_html=True)
# Fetch news
df = fetch_news()

# Apply search filter
if search_query:
    if category_filter == "All":
        mask = df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)
    else:
        mask = df[category_filter].str.contains(search_query, case=False, na=False)
    df = df[mask]

# Highlight searched word in DataFrame
if search_query:
    for col in ["Title", "Description", "Publication Date"]:
        df[col] = df[col].astype(str).apply(
            lambda x: highlight_text(x, search_query) if re.search(search_query, x, re.IGNORECASE) else x
        )

# Replace link text with "Read more"
df["Link"] = df["Link"].apply(lambda x: f"<a href=\"{x}\" target=\"_blank\" style=\"color: #28a745;\">Read more</a>")

# Table styling
st.markdown("""
    <style>
    th {
        background-color: #28a745 !important;
        color: white !important;
        text-align: center !important;
    }
    td {
        vertical-align: top !important;
    }
    </style>
""", unsafe_allow_html=True)

# Display the DataFrame as an HTML table with links and highlights
st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
