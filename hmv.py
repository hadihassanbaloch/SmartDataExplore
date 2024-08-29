import streamlit as st

class MissingValuesHandler:
    
    def __init__(self):
        if "df" not in st.session_state:
            st.session_state.df = None
        
    def handle_missing_data(self, method, column=None):
        df = st.session_state.df
        
        if method in ["Impute with mean", "Impute with max", "Impute with min"] and column:
            # Handle only numeric columns
            if column in df.select_dtypes(include=['number']).columns:
                if method == "Impute with mean":
                    df[column] = df[column].fillna(df[column].mean())
                elif method == "Impute with max":
                    df[column] = df[column].fillna(df[column].max())
                elif method == "Impute with min":
                    df[column] = df[column].fillna(df[column].min())
                st.success(f"Column '{column}' has been imputed with {method.split()[-1].lower()}.")
            else:
                st.warning(f"Column '{column}' is not numeric and cannot be imputed.")
        elif method == "Remove Column" and column:
            df = df.drop(columns=[column])
            st.session_state.df = df
            st.success(f"Column '{column}' has been removed.")
        elif method == "Remove All Null Values":
            df = df.dropna()
            st.session_state.df = df
            st.success("All rows with null values have been removed.")
        
        # Update session state with the modified DataFrame
        st.session_state.df = df  
        return df

    def render_ui(self):
        if "df" not in st.session_state or st.session_state.df is None:
            st.warning("No data to process.")
            return
        
        # Sidebar UI for Missing Values handling
        st.sidebar.header("Handle Missing Values]",divider="orange")
        mv_options = ["Replace with Mean",
                      "Replace with Max",
                      "Replace with Min",
                      "Remove Column",
                      "Remove all Nan"]
        
        clean_options = st.sidebar.radio("**Select an operation**", mv_options)

        column = None
        if clean_options in ["Replace with Mean", "Replace with Max", "Replace with Min", "Remove Column"]:
            column = st.sidebar.selectbox("**Choose a column**", st.session_state.df.columns)
        
        execute = st.sidebar.button("**Execute**",use_container_width=True)

        if execute: 
            self.handle_missing_data(clean_options, column)     
            st.dataframe(st.session_state.df, use_container_width=True)
