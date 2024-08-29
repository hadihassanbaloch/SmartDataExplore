
import pandas as pd
import streamlit as st
from utils import load_data
from eda import EDA
from data_visualizer import DataVisualization
from hmv import MissingValuesHandler  # Import the new class

# Set up the Streamlit page configuration
st.set_page_config(page_title="Smart Data Explorer", page_icon="🫧", layout="wide")

st.markdown("# ⚒️ :violet[Smart Data] :rainbow[Explorer]")
st.write("##")

# Initialize session state for DataFrame if not already done
if "df" not in st.session_state:
    st.session_state.df = None

# Sidebar tools: File upload
st.sidebar.header(":violet[Upload Csv or Excel files]")
uploaded_file = st.sidebar.file_uploader(
    "upload file", label_visibility="hidden",
    type=["csv", "xls", "xlsx"], accept_multiple_files=False)

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None and not df.empty:
        st.session_state.df = df

# Create the tabs
tabs = st.tabs(["**Data Preview**", "**EDA**", "**Handle Missing Values**", "**Visualization**"])

# Data Preview tab
with tabs[0]:
    if st.session_state.df is not None:
        st.header("**Dataset Preview**")
        st.dataframe(st.session_state.df, use_container_width=True)
    else:
        st.warning("Please upload a dataset to preview the data.")

# EDA tab
with tabs[1]:
    if st.session_state.df is not None:
        eda = EDA()  # Initialize the EDA class
        eda.render_ui()  # Render the UI for EDA
    else:
        st.warning("Please upload a dataset to use EDA tools.")

# Missing Values tab
with tabs[2]:
    if st.session_state.df is not None:
        mv_handler = MissingValuesHandler()  # Initialize the class
        mv_handler.render_ui()  # Render the UI for handling missing values
    else:
        st.warning("Please upload a dataset to handle missing values.")

# Visualization tab
with tabs[3]:
    if st.session_state.df is not None:
        datavis = DataVisualization(st.session_state.df)
        datavis.render_ui()
    else:
        st.warning("Please upload a dataset to visualize data.")
