## PCA Data Dictionary
This document describes the key fields used in the PCA Data Retriieval Automation Project.

## Dataset Fields

| Column Name | Description |
|-------------|-------------|
| **YEAR_MONTH** | Represent the year and month of the PCA data.  |
| **REGION_NAME** | Represents the geographical region associated with the product data. |
| **GENERIC_BNF_EQUIVALENT_NAME** | Name of the generic or BNF equivalent product. This Field is used to search and identify the required product. |
| **BNG_CHEMICAL_SUBSTANCE** | Represents the chemical substance associated with the product. |
| **ITEMS** | Number of items recorded for the product during the respective period. |
| **TOTAL_QUANTITY** | Total quantity recorded for the product during the respective period. |


## Usage in the Project
The above fields are loaded from the monthly PCA CSV files and combined into a single dataset.
The GENERIC_BNF_EQUIVALENT_NAME field is used to search for the required product, while YEAR_MONTH and ITEMS are used to generate the monthly product-level output.
TOTAL_QUANTITY is also loaded and can be used when the analysis requires quantity-based reporting.

## Notes
- The original PCA source files may contain additional fields.
- Only the fields required for this analysis are loaded by the Python script.
- Actual PCA source files are not included in this repository due to data confidentiality.
