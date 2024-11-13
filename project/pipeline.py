#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import sqlite3
import requests

# Step 1: Define the dataset URL and data directory
url = "https://pasteur.epa.gov/uploads/10.23719/1531143/SupplyChainGHGEmissionFactors_v1.3.0_NAICS_CO2e_USD2022.csv"
data_directory = './data'
os.makedirs(data_directory, exist_ok=True)

# Step 2: Download the dataset and load it into a DataFrame
try:
    data = pd.read_csv(url)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Failed to load dataset: {e}")
    exit(1)

# Step 3: Display basic information and clean the data
print("\nColumns in the dataset:", data.columns)
print("\nFirst few rows:", data.head())
data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)

# Step 4: Store the cleaned data in a SQLite database
db_file = os.path.join(data_directory, 'supply_chain_ghg_emissions.db')
conn = sqlite3.connect(db_file)

table_name = 'ghg_emission_factors'
data.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
print(f"\nData saved to SQLite table '{table_name}' in {db_file}.")

# Step 5: Confirmation of data storage
with sqlite3.connect(db_file) as conn:
    result = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5", conn)
    print("\nSample data from SQLite database:\n", result)


# In[ ]:




