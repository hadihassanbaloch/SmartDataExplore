import streamlit as st
import io

class EDA:
    def __init__(self):
        # Access the DataFrame directly from session state
        self.df = st.session_state.get('df', None)

    def perform_eda(self, options, column=None):
        # Ensure the DataFrame is loaded from session state
        if self.df is None:
            st.warning("No data available. Please upload a dataset.")
            return None

        # EDA functions based on the user selection
        if options == "Head":
            return self.df.head()
        elif options == "Describe":
            return self.df.describe()
        elif options == "Info":
            buffer = io.StringIO()
            self.df.info(buf=buffer)
            info_str = buffer.getvalue()
            return info_str
        elif options == "Null Values":
            return self.df.isnull().sum()
        elif options == "Correlation":
            numeric_df = self.df.select_dtypes(include=['number'])
            return numeric_df.corr()
        elif options == "Value Counts" and column:
            return self.df[column].value_counts()

    def render_ui(self):
        # Access the DataFrame directly from session state
        self.df = st.session_state.get('df', None)

        if self.df is None:
            st.warning("No data available. Please upload a dataset.")
            return

        # Sidebar UI for EDA options
        st.sidebar.header("Exploratory Data Analysis (EDA)",divider="orange")
        eda_options = ["Head", "Describe", "Info", "Null Values", "Correlation", "Value Counts"]
        options = st.sidebar.radio("Choose how you want to explore the data", options=eda_options)

        # Conditional display for column selection
        column = None
        if options == "Value Counts":
            column = st.sidebar.selectbox("Choose column for value counts", self.df.columns)
        elif options == "Correlation":
            column = None

        execute = st.sidebar.button("**Submit**",use_container_width=True)

        # Execute the selected function and display the result
        if execute:
            result = self.perform_eda(options, column)
            if result is not None:
                st.header(f"Results for {options}")
                if options == "Info":
                    st.text(result)
                else:
                    st.dataframe(result, use_container_width=True)
