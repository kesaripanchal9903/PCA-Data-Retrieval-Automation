import pandas as pd
import glob
import os

# Update this path to the folder containing the monthly PCA CSV files
folder_path = r'PATH_TO_PCA_CSV_FILES'   

#Columns required for the analysis
columns_to_keep = ['YEAR_MONTH', 'REGION_NAME', 'GENERIC_BNF_EQUIVALENT_NAME', 'BNF_CHEMICAL_SUBSTANCE', 'ITEMS','TOTAL_QUANTITY']

# LOAD AND COMBINE MONTHLY CSV FILES
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# Read and concatenate CSVs
merged_df = pd.concat(
    [pd.read_csv(file, usecols=lambda col: col in columns_to_keep) for file in csv_files],
    ignore_index=True
)
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
print(f"Found {len(csv_files)} CSV files.")

# PRODUCT SEARCH
search_product = input ("\nEnter product name or keyword to search: ").strip()
if not search_product:
print("No product name entered.")
exit()

# Find products matching the search keyword
filtered_products = merged_df[merged_df['GENERIC_BNF_EQUIVALENT_NAME'].str.contains(search_product, case=False, na=False)][
                           'GENERIC_BNF_EQUIVALENT_NAME'].drop_duplicates().reset_index(drop=True)


# Display matching products
print(f"Entries matching '{search_product}':")
print(filtered_products.to_string(index=False))

# for multiple product
search_term = ["Proguanil 25mg / Atovaquone 62.5mg tablets"]

# Your list of search terms (case-insensitive partial matches)
pattern = '|'.join(search_term)


# Filter rows where the generic name contains the search term
filtered_df = merged_df[
    merged_df['GENERIC_BNF_EQUIVALENT_NAME'].str.contains(pattern, case=False, na=False)
]

# Group by YEAR_MONTH and GENERIC_BNF_EQUIVALENT_NAME, then sum the quantities
grouped_df = (
    filtered_df
    .groupby(['YEAR_MONTH', 'GENERIC_BNF_EQUIVALENT_NAME'])['ITEMS']
    .sum()
    .reset_index()
    .sort_values(['YEAR_MONTH', 'GENERIC_BNF_EQUIVALENT_NAME'])
)

# Show the result
print(grouped_df.to_string(index=False))
