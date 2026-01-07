import pandas as pd
import numpy as np

# Load your data from the specified path
file_path = r"D:\UNI STUDY\Exchange\SUFE studying\Time series analysis\FINAL PROJ\dataset\Retail inventory - Copy.csv"
df = pd.read_csv(file_path)

# Convert the 'Past promotion of product in lac' and 'Demand forecast' columns to correct values (multiply by 1000 for decimals)
df['Past promotion of product in lac'] = df['Past promotion of product in lac'].apply(lambda x: x * 1000 if x < 10 else x)
df['demand forecast'] = df['demand forecast'].apply(lambda x: x * 1000 if x < 10 else x)

# Replace the old 'Inventory Level' column with new random integers in the range 15,000 to 140,000
df['inventory level'] = np.random.randint(15000, 140001, size=len(df))

# Save the modified DataFrame to a new CSV file
output_path = r"D:\UNI STUDY\Exchange\SUFE studying\Time series analysis\FINAL PROJ\dataset\Updated_Retail_inventory.csv"
df.to_csv(output_path, index=False)

# Display the first few rows to verify the changes
print(df.head())
