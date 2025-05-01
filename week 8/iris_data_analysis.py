"""
Iris Dataset Analysis
Week 8 PLP Assignment
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Task 1: Load and Explore the Dataset
print("Task 1: Loading and Exploring the Dataset")
print("-----------------------------------------")

# Try to load the Iris dataset from CSV file
try:
    # Define the CSV file path - make sure iris_dataset.csv is in the same folder as this script
    file_path = "iris_dataset.csv"
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        print("Make sure the CSV file is in the same directory as this script.")
        exit()
    
    # Load the dataset from CSV
    df = pd.read_csv(file_path)
    
    # Print the first 5 rows of the dataset
    print("First 5 rows of the dataset:")
    print(df.head())
    print()
    
    # Check the data types and structure
    print("Dataset info:")
    print(df.info())
    print()
    
    # Check for missing values
    print("Missing values:")
    print(df.isnull().sum())
    print()
    
    # Check if there are any missing values and handle them if needed
    if df.isnull().sum().sum() > 0:
        # Fill missing numerical values with mean of respective column
        for col in df.select_dtypes(include=['float64', 'int64']).columns:
            df[col].fillna(df[col].mean(), inplace=True)
        
        # Fill missing categorical values with mode (most frequent value)
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        print("Missing values have been handled.")
    else:
        print("Dataset is clean - no missing values found.")
    
except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
print("\nTask 2: Basic Data Analysis")
print("---------------------------")

# Calculate basic statistics
print("Basic statistics of numerical columns:")
print(df.describe())
print()

# Group by species and calculate mean of each feature
print("Average measurements for each species:")
species_means = df.groupby('species').mean()
print(species_means)
print()

# Find some interesting patterns
print("Interesting findings:")
print(f"1. The species with the largest sepal length on average is {species_means['sepal_length'].idxmax()}.")
print(f"2. The species with the smallest petal length on average is {species_means['petal_length'].idxmin()}.")
print(f"3. The difference between max and min average petal width is {species_means['petal_width'].max() - species_means['petal_width'].min():.2f} cm.")
print()

# Task 3: Data Visualization
print("\nTask 3: Data Visualization")
print("-------------------------")

# Set a nicer visual style
sns.set_style("whitegrid")

# Create a figure with 2x2 subplots
plt.figure(figsize=(14, 10))

# 1. Line chart - Average measurements by species
plt.subplot(2, 2, 1)
species_means.T.plot(kind='line', ax=plt.gca(), marker='o')
plt.title('Average Measurements by Species')
plt.xlabel('Measurements')
plt.ylabel('Value (cm)')
plt.legend(title='Species')
plt.tight_layout()

# 2. Bar chart - Comparison of petal length across species
plt.subplot(2, 2, 2)
sns.barplot(x='species', y='petal_length', data=df, palette='viridis')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()

# 3. Histogram - Distribution of sepal width
plt.subplot(2, 2, 3)
for species, group in df.groupby('species'):
    plt.hist(group['sepal_width'], alpha=0.5, label=species)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.legend(title='Species')
plt.tight_layout()

# 4. Scatter plot - Relationship between sepal length and petal length
plt.subplot(2, 2, 4)
for species, group in df.groupby('species'):
    plt.scatter(group['sepal_length'], group['petal_length'], label=species, alpha=0.7)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()

# Save the figure
plt.savefig('iris_analysis_plots.png')
print("Visualizations saved to 'iris_analysis_plots.png'")

# Show all plots
plt.show()

print("\nAnalysis complete! Check the saved visualization file.")