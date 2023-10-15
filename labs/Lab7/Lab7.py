# Lab 7

import pandas as pd

# Manually create a dataframe:
df = pd.DataFrame(
	{
		"Name": [
			"Lucy",
			"Thor",
			"Jenga"
		],
		"Age": [7, 11, 4],
		"Species": ["dog", "dog", "cat"]
	}
)
print(df)

# To save to csv:
df.to_csv('data.csv')

# Create dataframe from csv:
df2 = pd.read_csv('data.csv')

# Get information about the dataframe:
print(df.info())