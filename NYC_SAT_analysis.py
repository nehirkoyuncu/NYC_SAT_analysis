import pandas as pd
import numpy as np
# Read in the data
schools = pd.read_csv("schools.csv")

#  Best math schools (>= 80% of 800 = 640)
best_math_schools = schools[schools['average_math'] >= 640][['school_name', 'average_math']]
best_math_schools = best_math_schools.sort_values('average_math', ascending=False).reset_index(drop=True)

# Top 10 schools by combined SAT scores
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name', 'total_SAT']].sort_values('total_SAT', ascending=False).head(10).reset_index(drop=True)

# Borough with largest standard deviation
borough_stats = schools.groupby('borough').agg({
    'school_name': 'count',
    'total_SAT': ['mean', 'std']
}).reset_index()
borough_stats.columns = ['borough', 'num_schools', 'average_SAT', 'std_SAT']

# Find the borough with the largest standard deviation
largest_std_dev = borough_stats.loc[borough_stats['std_SAT'].idxmax()].to_frame().T

# Ensure proper rounding: num_schools as integer, others to 2 decimal places
largest_std_dev['num_schools'] = largest_std_dev['num_schools'].astype(int)
largest_std_dev['average_SAT'] = np.round(largest_std_dev['average_SAT'].astype(float), 2)
largest_std_dev['std_SAT'] = np.round(largest_std_dev['std_SAT'].astype(float), 2)

# Reset index to get a clean single-row DataFrame
largest_std_dev = largest_std_dev.reset_index(drop=True)

print("=== BEST MATH SCHOOLS ===")
print(best_math_schools.head())
print("\n=== TOP 10 SCHOOLS BY COMBINED SAT SCORES ===")
print(top_10_schools)
print("\n=== BOROUGH WITH LARGEST STANDARD DEVIATION ===")
print(largest_std_dev)
print("\nData types in largest_std_dev:")
print(largest_std_dev.dtypes)
