import pandas as pd
import streamlit as st

def show_data_types(df):

    st.subheader("Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(dtype_df)


def show_missing_values(df):

    st.subheader("Missing Values")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum()
    })

    st.dataframe(missing_df)


def show_duplicates(df):

    st.subheader("Duplicate Records")

    duplicates = df.duplicated().sum()

    st.metric(
        "Duplicate Rows",
        duplicates
    )


def show_statistics(df):

    st.subheader("Basic Statistics")

    st.dataframe(df.describe())