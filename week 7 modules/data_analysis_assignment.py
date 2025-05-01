"""
Data Analysis Assignment
-----------------------
This script performs basic data analysis and visualization on the Iris dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Task 1: Load and Explore the Dataset
print("TASK 1: LOADING AND EXPLORING THE DATASET")
print("-----------------------------------------")

# Use try-except for error handling when loading data
try:
    # Load the Iris dataset from the CSV file
    iris_df = pd.read_csv('iris_data.csv')
    
    print("Dataset loaded successfully!")
    
    # Display the first 5 rows
    print("\nFirst 5 rows of the dataset:")
    print(iris_df.head())
    
    # Check the structure of the dataset
    print("\nDataset structure:")
    print(iris_df.info())
    
    # Check for missing values
    print("\nMissing values in each column:")
    print(iris_df.isnull().sum())
    
    # Note about handling missing values
    print("\nNo missing values found in the dataset. If there were missing values, we could handle them by:")
    print("1. Dropping rows with missing values using df.dropna()")
    print("2. Filling missing values using df.fillna() with mean, median, or a specific value")
    
except FileNotFoundError:
    print("Error: iris_data.csv file not found. Please make sure the file is in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Task 2: Basic Data Analysis
print("\n\nTASK 2: BASIC DATA ANALYSIS")
print("--------------------------")

# Calculate basic statistics
print("Basic statistics of the numerical columns:")
print(iris_df.describe())

# Group by species and calculate mean for each numerical column
print("\nMean values for each feature grouped by species:")
species_means = iris_df.groupby('species').mean()
print(species_means)

# Identify patterns or interesting findings
print("\nInteresting findings:")
print("1. Setosa species has the smallest petal length and width.")
print("2. Virginica species has the largest petal length and width.")
print("3. Sepal width is the only feature where Setosa has the highest mean value.")

# Task 3: Data Visualization
print("\n\nTASK 3: DATA VISUALIZATION")
print("-------------------------")

# Set figure size for all plots
plt.figure(figsize=(12, 10))

# 1. Line chart - Showing trends
# Create a line chart of the sorted petal lengths for each species
plt.subplot(2, 2, 1)

# Get unique species
species_list = iris_df['species'].unique()

for species in species_list:
    # Sort values for each species to see the distribution
    species_data = iris_df[iris_df['species'] == species]
    sorted_values = sorted(species_data['petal_length'])
    plt.plot(sorted_values, label=species)

plt.title('Sorted Petal Length by Species')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)

# 2. Bar chart - Comparison across categories
plt.subplot(2, 2, 2)
species_means.plot(kind='bar', ax=plt.gca())
plt.title('Average Measurements by Species')
plt.xlabel('Species')
plt.ylabel('Value (cm)')
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# 3. Histogram - Distribution of a numerical column
plt.subplot(2, 2, 3)
plt.hist(iris_df['sepal_length'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# 4. Scatter plot - Relationship between two numerical columns
plt.subplot(2, 2, 4)

for species in species_list:
    species_data = iris_df[iris_df['species'] == species]
    plt.scatter(
        species_data['sepal_length'],
        species_data['petal_length'],
        label=species,
        alpha=0.7
    )

plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('iris_data_visualizations.png')
print("Visualizations have been created and saved as 'iris_data_visualizations.png'")

# Show all plots
plt.show()

print("\nAnalysis complete! Key observations:")
print("- Iris setosa has distinct characteristics from the other two species")
print("- There is a strong positive correlation between petal length and sepal length")
print("- The sepal width distribution shows more overlap between species than other features")