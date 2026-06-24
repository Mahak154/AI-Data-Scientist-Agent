import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def show_histogram(df):

    st.subheader("Data Distribution")

    selected_column = st.selectbox(
        "Select Column",
        df.columns
    )

    fig, ax = plt.subplots(figsize=(6,4))

    if df[selected_column].nunique() < 20:

        df[selected_column].value_counts().plot(
            kind="bar",
            ax=ax
        )

    else:

        ax.hist(
            df[selected_column],
            bins=20
        )

    ax.set_title(f"Distribution of {selected_column}")

    st.pyplot(fig)


def show_heatmap(df):

    st.subheader("Correlation Heatmap")

    numeric_df = df.select_dtypes(include=["number"])

    if len(numeric_df.columns) > 1:

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(
            numeric_df.corr(),
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)