import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Pengaturan Judul Halaman Web
st.set_page_config(page_title="Sales Forecast Dashboard", layout="wide")
st.title("📈 Smart Sales Forecasting & Inventory Dashboard")

# 1. Membuat Data Penjualan Harian Buatan (Simulasi)
@st.cache_data
def load_data():
    dates = pd.date_range(start="2026-01-01", periods=180, freq="D")
    sales = np.sin(np.linspace(0, 20, 180)) * 50 + 200 + np.random.normal(0, 10, 180)
    df = pd.DataFrame({"Tanggal": dates, "Penjualan": sales})
    return df.set_index("Tanggal")

df = load_data()

# 2. Kontrol Interaktif di Sidebar
st.sidebar.header("⚙️ Parameter Peramalan")
forecast_days = st.sidebar.slider("Jumlah Hari Prediksi", min_value=7, max_value=30, value=14)
buffer_factor = st.sidebar.slider("Safety Stock Factor (%)", 10, 50, 20) / 100

# 3. Pemodelan Peramalan (Holt-Winters)
model = ExponentialSmoothing(df["Penjualan"], trend="add", seasonal="add", seasonal_periods=7).fit()
forecast = model.forecast(forecast_days)

# 4. Menampilkan Grafik
fig = px.line(df, y="Penjualan", title="Riwayat & Prediksi Penjualan Harian")
fig.add_scatter(x=forecast.index, y=forecast.values, mode="lines+markers", name="Hasil Prediksi")
st.plotly_chart(fig, use_container_width=True)

# 5. Menampilkan Indikator Angka Ringkas
col1, col2, col3 = st.columns(3)
col1.metric("Total Prediksi Penjualan", f"{int(forecast.sum()):,} unit")
col2.metric("Rata-rata Penjualan/Hari", f"{int(forecast.mean()):,} unit")
col3.metric("Rekomendasi Safety Stock", f"{int(forecast.mean() * (1 + buffer_factor)):,} unit")