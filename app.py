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
    # =========================
    # Data Types
    # =========================

    st.subheader("Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(dtype_df)

    # =========================
    # Missing Values
    # =========================

    st.subheader("Missing Values")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum(),
        "Missing %": round((df.isnull().sum()/len(df))*100,2)
    })

    st.dataframe(missing_df)

    # =========================
    # Duplicate Records
    # =========================

    st.subheader("Duplicate Records")

    duplicates = df.duplicated().sum()

    st.metric(
        "Duplicate Rows",
        duplicates
    )

    # =========================
    # Dataset Health Dashboard
    # =========================

    st.subheader("Dataset Health")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Missing",
            df.isnull().sum().sum()
        )

    with col2:
        st.metric(
            "Duplicate Rows",
            duplicates
        )

    with col3:
        st.metric(
            "Total Features",
            len(df.columns)
        )

    # =========================
    # Basic Statistics
    # =========================

    st.subheader("Basic Statistics")
    st.dataframe(df.describe())