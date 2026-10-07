# PCA-Data-Retrieval-Automation
Python-based automation for retrieving product-level PCA data from multiple monthly CSV files.

A python-based data retrieval and automation project developed using Pandas to efficiently search and analyze product-level PCA data stored across multiple CSV files.
The project was developed to reduce the manual efforts involved in searching historical PCA data and to support **market trend analysis and product/formulation evaluation.**

## Business Requirenment
Management needed PCA data to understand the market trend and potential of specific medicines/formulations.

# The analysis involved:
- Collecting monthly product items/quantity from PCA data.
- Obtaining the current market price of the product from relevant registered online source.
- Calculating estimated **year-over-year(YoY) sales value** using:
    **Annual Items/Quantity * Current Price**
- Comparing product performance across years to understand market movement.
- Using historical market data as an input when evaluating opportunities to **launch a new product or formulation.**

# Solution
A python-based solution was developed using **Pandas** to combine multiple monthly PCA CSV files into a single dataset and quickly retrieve the required product-level data.
The retrieve data can then be used with current market price information for further market trend analysis, estimated sales value calculation, and product opportunity evaluation.

## Dataset
The project uses monthly PCA CSV files containing product and pharmaceutical data, including:
- Year and Month
- Region
- Generic / BNF Equivalent Product Name
- BNF Chemical Substance
- Items
- Total Quantity

The monthly files are combined into a single dataset before performing product searches and analysis.

## Tools Used
- Python
- Pandas
- CSV
- Jupyter Notebook

## Key Features
- Combine multiple monthly PCA CSV files into a single dataset.
- Searches product names using **case-sensitive keyword matching.**
- Identifies multiple product name matching a search term.
- Filters data for the required product.
- Groups product data by **YEAR-MONTH.**
- Calculates monthly **Items** for the selected products.
- Provides structured product-level data for further market analysis.

## Output
The script generates a monthly product-level summary containing:
-YEAR-MONTH
-GENERIC_BNF_EQUIVALENT_NAME
-ITEMS

**Example:**
YEAR_MONTH    GENERIC_BNF_EQUIVALENT_NAME                         ITEMS
202101        Proguanil 25mg / Atovaquone 62.5mg tablets              8
202102        Proguanil 25mg / Atovaquone 62.5mg tablets              4
202103        Proguanil 25mg / Atovaquone 62.5mg tablets              7

The retrieved monthly data can subsequently be aggregated by year and combined with the current market price to estimate yearly sales value.
            **Estimated Sales Value = Annual Items/Quantity × Current Price**
This provides an indicative view of market performance and can support product or formulation evaluation.

## Project Structure
PCA-Data-Retrieval-Automation/
│
├── PCA_Data_Retrieval.py
├── README.md
└── Data_Dictionary.md

