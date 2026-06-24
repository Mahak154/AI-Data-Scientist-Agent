import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Data Scientist Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Scientist Agent")

uploaded_file = st.file_uploader(
    "Upload a CSV file or Excel file",
    type=["csv","xlsx"]
)

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file, header=1)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file, header=1)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        st.stop()
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

    st.subheader("Histogram")

    selected_column = st.selectbox(
        "Select Column",
        [col for col in df.columns if col not in ["Unnamed: 0"]]  
    )

    fig, ax = plt.subplots(figsize=(5, 3))
    if df[selected_column].nunique() < 20:
        df[selected_column].value_counts().plot(
            kind="bar",
            ax=ax
        )

    else:
        ax.hist(df[selected_column], bins=20)
    ax.set_title(f"Distribution of {selected_column}")

    df[selected_column].value_counts().head(20).plot(
        kind="bar",
        ax=ax
    )
   
    st.pyplot(fig)

    st.subheader("Correlation Heatmap")

    numeric_df = df.select_dtypes(include=["number"])
    st.write(numeric_df.shape)
    if len(numeric_df.columns) > 1:

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(
            numeric_df.corr(),
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)
        st.subheader("Data Quality Score")

        score = 100

        missing_cells = df.isnull().sum().sum()

        duplicates = df.duplicated().sum()

        score -= min(missing_cells, 50)

        score -= min(duplicates * 5, 50)

        score = max(score, 0)

        st.metric(
            "Quality Score",
            f"{score}/100"
        )