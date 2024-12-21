import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

# Title of the App
st.title("Crypto Price Correlation Dashboard")

# Upload the crypto prices file
uploaded_file = st.file_uploader("Upload the crypto_prices.csv file", type=["csv"])

if uploaded_file:
    # Load the data
    data = pd.read_csv(uploaded_file, index_col='timestamp', parse_dates=True)

    # Show data preview
    st.write("### Data Preview", data.head())

    # Data Cleaning and Percentage Change
    data = data.interpolate(method='time').dropna()
    returns = data.pct_change(fill_method=None).dropna()

    # Correlation Matrix
    correlation_matrix = returns.corr()

    # Display Correlation Matrix
    st.write("### Correlation Matrix")
    st.dataframe(correlation_matrix)

    # Generate and Display Heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, ax=ax)
    st.pyplot(fig)

    # Download Heatmap
    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    st.download_button("Download Heatmap", buffer, file_name="correlation_heatmap.png", mime="image/png")
