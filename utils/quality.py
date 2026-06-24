import streamlit as st

def show_quality_score(df):

    score = 100
    missing_cells = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    score -= min(missing_cells, 50)
    score -= min(duplicates * 5, 50)
    score = max(score, 0)

    st.subheader("Data Quality Score")

    st.metric(
        "Quality Score",
        f"{score}/100"
    )