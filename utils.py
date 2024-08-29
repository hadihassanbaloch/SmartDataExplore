import pandas as pd
import streamlit as st

# load data function
def load_data(uploaded_file):
    try:
        file_extention = uploaded_file.name.split('.')[-1].lower()
        if file_extention == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extention in ["xls","xlsx"]:
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format, Please upload Csv or Excel file")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None 
    
