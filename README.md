# 📈 Smart Sales Forecasting & Inventory Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Time%20Series-green?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly)

An end-to-end interactive Data Science web application designed to forecast daily sales trends and optimize inventory buffer requirements using **Holt-Winters Exponential Smoothing** and dynamic safety stock modeling.

---

## 📌 Project Overview

In retail and supply chain management, balancing stock levels is critical. Overstocking increases holding costs, while understocking leads to lost revenue and dissatisfied customers.

This project bridges data analytics and operational Decision Support Systems (DSS) by:

1. **Predicting Daily Demand:** Utilizing time series forecasting (Holt-Winters Additive Seasonality) to project sales over custom horizons (7 to 30 days).
2. **Buffer/Safety Stock Optimization:** Dynamically calculating recommended safety stock based on adjustable risk tolerance parameters.
3. **Interactive Decision Making:** Providing business users with an intuitive dashboard to simulate various demand scenarios in real-time.

---

## ✨ Key Features

- 🔮 **Time Series Forecasting:** Automated fitting of Holt-Winters Triple Exponential Smoothing model capturing daily trend and 7-day weekly seasonality.
- 🛡️ **Dynamic Safety Stock Calculator:** Real-time buffer stock adjustments based on user-defined buffer percentages.
- 📊 **Interactive Visualizations:** High-precision, zoomable time series plots generated with Plotly.
- ⚡ **Real-Time KPIs:** Dynamic metric cards showing total projected sales, daily average demand, and recommended buffer inventory.

---

## 🛠️ Tech Stack & Libraries

| Category                 | Tools / Libraries                    |
| :----------------------- | :----------------------------------- |
| **Language**             | Python 3.9+                          |
| **Web Framework**        | Streamlit                            |
| **Time Series Modeling** | `statsmodels` (ExponentialSmoothing) |
| **Data Manipulation**    | `pandas`, `numpy`                    |
| **Data Visualization**   | `plotly.express`                     |

---

## 📁 Repository Structure

```text
sales-forecasting-dashboard/
├── data/
│   └── sales_data.csv        # Simulated daily sales dataset
├── app.py                     # Main Streamlit dashboard application
├── requirements.txt           # Python dependency specifications
└── README.md                  # Comprehensive project documentation
```

---

## 🚀 Getting Started Locally

Follow these step-by-step instructions to run the application on your local machine:

### 1. Prerequisites

Ensure you have Python 3.9 or higher installed. Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sales-forecasting-dashboard.git
cd sales-forecasting-dashboard
```

### 3. Install Dependencies

Install all required libraries specified in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

Execute the following command to start the Streamlit local server:

```bash
python -m streamlit run app.py
```

_(Using `python -m streamlit` avoids environment PATH issues on Windows)._

The application will automatically open in your default browser at `http://localhost:8501`.

---

## 🧮 Theoretical Background

### Holt-Winters Exponential Smoothing (Additive Seasonality)

The core forecasting engine utilizes Holt-Winters Exponential Smoothing, suited for time series data showing both trend and daily seasonality ($s = 7$ for weekly patterns):

$$\hat{y}_{t+h|t} = \ell_t + h b_t + s_{t+h-m(k+1)}$$

- **Level ($\ell_t$):** Represents the smoothed series value at time $t$.
- **Trend ($b_t$):** Estimates the local growth rate/slope.
- **Seasonality ($s_t$):** Captures recurring 7-day patterns in sales velocity.

### Safety Stock Formula

$$ ext{Safety Stock} = ar{D}_{forecast} imes (1 + ext{Buffer Factor})$$
Where $ ar{D}_{forecast}$ represents the projected mean daily demand, adjusted by a user-selected safety margin percentage (10% - 50%).

---

## 🌐 Live Deployment

This dashboard is ready to be deployed on **Streamlit Community Cloud**:

1. Push this repository to your GitHub account.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub repository and set the main file path to `app.py`.
4. Click **Deploy**!

---

## 👤 Author

**Veranda Ardiyan PP**

- Data Science Student & Enthusiast
- GitHub: [verangod](https://github.com/verangod)
  README.md
  Menampilkan README.md.
