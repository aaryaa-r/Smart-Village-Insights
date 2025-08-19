
# Smart Village Insights (Streamlit App)

A simple data-driven dashboard for rural internship projects:
- Electricity cut analysis (30-day simulation)
- Water usage vs wastage (10-day simulation)
- Rainfall vs crop yield relationship (prototype)

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Push this folder to a **public GitHub repo**.
2. Go to https://streamlit.io/cloud → New App → connect your repo.
3. Set the entry file to `app.py`.
4. (Optional) Under **App settings → Advanced**, set a custom **App URL** slug.

## Deploy on Render
1. Create a new **Web Service**.
2. Runtime: Python; Build Command: `pip install -r requirements.txt`
3. Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
