import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Data Scientist Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Scientist Agent")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])