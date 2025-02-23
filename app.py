import streamlit as st
import pandas as pd
from src.data_analysis import SalaryAnalyzer

# Page configuration
st.set_page_config(
    page_title="Salary Analysis Dashboard",
    page_icon="💰",
    layout="wide"
)

# Title and description
st.title("💰 Position Salary Analysis Dashboard")
st.markdown("""
This dashboard provides insights into the relationship between positions and their corresponding salaries.
Explore different visualizations and statistics to understand salary distributions and trends.
""")

# Initialize analyzer
analyzer = SalaryAnalyzer('Position_Salaries.csv')

# Sidebar
st.sidebar.header("Dashboard Navigation")
page = st.sidebar.radio(
    "Select a section:",
    ["Overview", "Salary Distribution", "Position Analysis", "Growth Analysis"]
)

# Main content
if page == "Overview":
    # Display basic statistics
    st.header("Dataset Overview")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Raw Data")
        st.dataframe(analyzer.df)
    
    with col2:
        st.subheader("Statistical Summary")
        stats, missing = analyzer.get_basic_stats()
        st.dataframe(stats)
        
        st.subheader("Missing Values")
        st.dataframe(missing)

elif page == "Salary Distribution":
    st.header("Salary Distribution Analysis")
    
    # Salary distribution plot
    st.plotly_chart(analyzer.create_salary_distribution(), use_container_width=True)
    
    # Level vs Salary scatter plot
    st.plotly_chart(analyzer.create_level_salary_scatter(), use_container_width=True)

elif page == "Position Analysis":
    st.header("Position-wise Salary Analysis")
    
    # Position vs Salary bar plot
    st.plotly_chart(analyzer.create_position_salary_bar(), use_container_width=True)
    
    # Additional statistics
    st.subheader("Position-wise Statistics")
    position_stats = analyzer.df.groupby('Position')['Salary'].agg(['mean', 'min', 'max']).round(2)
    st.dataframe(position_stats)

elif page == "Growth Analysis":
    st.header("Salary Growth Analysis")
    
    # Salary growth table
    growth_df = analyzer.calculate_salary_growth()
    st.dataframe(growth_df)
    
    # Additional insights
    st.subheader("Key Insights")
    avg_growth = growth_df['Salary_Growth'].mean()
    max_growth = growth_df['Salary_Growth'].max()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Growth Rate", f"{avg_growth:.2f}%")
    with col2:
        st.metric("Maximum Growth Rate", f"{max_growth:.2f}%")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit") 