import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv(r"C:\MinGW\bin\C progms\Machine_Learning\hcc_dataset.csv" )

# Replace '?' with NaN values

df.replace('?', np.nan, inplace=True)

df.to_csv('modified_file.csv', index=False)
