import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

class SalaryAnalyzer:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        
    def get_basic_stats(self):
        stats = self.df.describe()
        missing_values = self.df.isnull().sum()
        return stats, missing_values
    
    def create_salary_distribution(self):
        fig = px.histogram(
            self.df, 
            x='Salary',
            title='Distribution of Salaries',
            labels={'Salary': 'Salary ($)'},
            nbins=15
        )
        return fig
    
    def create_level_salary_scatter(self):
        fig = px.scatter(
            self.df,
            x='Level',
            y='Salary',
            title='Level vs Salary Relationship',
            labels={'Level': 'Position Level', 'Salary': 'Salary ($)'},
            trendline="ols"
        )
        return fig
    
    def create_position_salary_bar(self):
        fig = px.bar(
            self.df,
            x='Position',
            y='Salary',
            title='Salary by Position',
            labels={'Position': 'Job Position', 'Salary': 'Salary ($)'}
        )
        fig.update_layout(xaxis_tickangle=-45)
        return fig
    
    def calculate_salary_growth(self):
        self.df['Salary_Growth'] = self.df['Salary'].pct_change() * 100
        growth_df = self.df[['Position', 'Salary', 'Salary_Growth']].round(2)
        return growth_df 