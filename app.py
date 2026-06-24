import streamlit as st
import pandas as pd

from utils.profiler import *
from utils.visualizer import *
from utils.quality import *

st.set_page_config(
    page_title="AI Data Scientist Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Scientist Agent")

st.write(
    "An AI-powered platform for dataset analysis, machine learning, "
    "insight generation and automated reporting."
)

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Load Dataset
    df = pd.read_csv(uploaded_file, header=1)

    # Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Dataset Information
    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # Data Profiling
    show_data_types(df)

    show_missing_values(df)

    show_duplicates(df)

    show_statistics(df)

    # Visualization
    show_histogram(df)
    show_heatmap(df)

    # Quality Score
    show_quality_score(df)