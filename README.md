

# BBC News Feed Dashboard

A **Streamlit-based web app** that fetches the latest news headlines from **BBC News RSS Feed** and displays them in a styled interactive dashboard.
It includes **keyword search, category filtering, and text highlighting** for easy news exploration.

---

## 📌 Features

* Fetches real-time news using **BBC RSS feed**.
* Displays **Title, Description, Publication Date, and Read More links**.
* **Search by keyword** across all fields or within a specific column.
* **Highlighted results** for better readability.
* **Styled sidebar** with custom colors and improved UI.
* Opens links in a **new tab** with "Read More" text.

---

## 🚀 How to Run

1.  Install dependencies (make sure you have `pip`):

   ```bash
   pip install streamlit requests beautifulsoup4 pandas
   ```

3. Run the app with:

   ```bash
   streamlit run app.py
   ```

4. The app will open in your **default browser** at:

   ```
   http://localhost:8501/
   ```

---

## 📂 Project Structure

```
bbc-news-dashboard/
│── app.py              # Main Streamlit application
│── README.md           # Documentation
```

---

## 🔧 Technologies Used

* **Python**
* **Streamlit** – for interactive web dashboard
* **Requests** – for fetching RSS feed
* **BeautifulSoup** – for parsing XML
* **Pandas** – for structured data handling
* **Regex (re)** – for highlighting search terms

---

