import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


class DataVisualization:
    def __init__(self,df):
        # Use the DataFrame from session state
        self.df = st.session_state.get('df', None)
        if self.df is None or self.df.empty:
            st.error("DataFrame is empty or not loaded.")
    
    def scatterplot(self, x_col, y_col):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x=x_col, y=y_col)
        st.pyplot(plt.gcf())  # Display the plot in Streamlit
        plt.clf()  # Clear the plot after displaying to avoid overlap

    def lineplot(self, x_col, y_col):
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.df, x=x_col, y=y_col)
        st.pyplot(plt.gcf())
        plt.clf()

    def boxplot(self, x_col, y_col):
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df, x=x_col, y=y_col)
        st.pyplot(plt.gcf())
        plt.clf()

    def barplot(self, x_col, y_col):
        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.df, x=x_col, y=y_col)
        st.pyplot(plt.gcf())
        plt.clf()

    def histogram(self, x_col):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[x_col], kde=True)
        st.pyplot(plt.gcf())
        plt.clf()

    def render_ui(self):
        if self.df is None or self.df.empty:
            st.error("DataFrame is not available for visualization.")
            return
        
        st.sidebar.header("Data Visualization with Seaborn]",divider="orange")
        plots = ["Scatterplot", "Lineplot", "Boxplot", "Histogram", "Barplot"]
        
        plot_type = st.sidebar.radio("**Choose plot type**", options=plots)
        
        if plot_type in ["Scatterplot", "Lineplot", "Boxplot", "Barplot"]:
            x_col = st.sidebar.selectbox("Select X-axis column", options=self.df.columns)
            y_col = st.sidebar.selectbox("Select Y-axis column", options=self.df.columns)
            
            if st.sidebar.button("**Visualize**",use_container_width=True):
                if plot_type == "Scatterplot":
                    self.scatterplot(x_col, y_col)
                elif plot_type == "Lineplot":
                    self.lineplot(x_col, y_col)
                elif plot_type == "Boxplot":
                    self.boxplot(x_col, y_col)
                elif plot_type == "Barplot":
                    self.barplot(x_col, y_col)
        
        elif plot_type == "Histogram":
            hist_col = st.sidebar.selectbox("Select column", options=self.df.columns)
            
            if st.sidebar.button("**Visualize**",use_container_width=True):
                self.histogram(hist_col)
