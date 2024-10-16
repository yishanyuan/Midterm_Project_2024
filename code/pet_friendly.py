import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_price_distribution(data, bins=20, kde=True):
    """
    
    """
    
    one_day_data = data[data['Length of lease'] == 'one day']

    
    plt.figure(figsize=(10, 6))
    sns.histplot(one_day_data['Price Per Night'], bins=bins, kde=kde, color='green')
    plt.title('Price Distribution of One-Day Airbnb Listings')
    plt.xlabel('Price Per Night ($)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    

def plot_city_comparison_boxplot(data, selected_cities):
    """
    
    """
    
    one_day_data = data[data['Length of lease'] == 'one day']
    df_filtered = one_day_data[one_day_data['City'].isin(selected_cities)]

    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='City', y='Price Per Night', data=df_filtered)
    plt.title('Comparison of One-Day Airbnb Prices in Selected Cities')
    plt.xlabel('City')
    plt.ylabel('Price Per Night ($)')
    plt.grid(True)
    plt.xticks(rotation=45)  
    plt.tight_layout()

def plot_pet_combined_price_distributions(one_day_file, one_week_file, one_month_file, output_file):
    """
    
    """
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6)) 

    
    data_one_month = pd.read_excel(one_month_file)
    sns.histplot(data=data_one_month, x='Price Per Night', hue='Pets allowed', multiple='stack', bins=20, palette='Set2', ax=axes[0])
    axes[0].set_title('One Month Price Distribution')
    axes[0].set_xlabel('One Month Price ($)')
    axes[0].set_ylabel('Count')

   
    data_one_week = pd.read_excel(one_week_file)
    sns.histplot(data=data_one_week, x='Price Per Night', hue='Pets allowed', multiple='stack', bins=20, palette='Set2', ax=axes[1])
    axes[1].set_title('One Week Price Distribution')
    axes[1].set_xlabel('One Week Price ($)')
    axes[1].set_ylabel('')

    
    data_one_day = pd.read_excel(one_day_file)
    sns.histplot(data=data_one_day, x='Price Per Night', hue='Pets allowed', multiple='stack', bins=20, palette='Set2', ax=axes[2])
    axes[2].set_title('One Day Price Distribution')
    axes[2].set_xlabel('One Day Price ($)')
    axes[2].set_ylabel('')

   
    plt.tight_layout()
    plt.savefig(output_file, format='png')
    
