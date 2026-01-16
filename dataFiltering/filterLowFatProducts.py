import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df.iloc[:, :1]


if __name__ == "__main__":
    products = pd.DataFrame({
        'product_id': [1, 2, 3, 4, 5],
        'low_fats': ['Y', 'N', 'Y', 'N', 'Y'],
        'recyclable': ['Y', 'Y', 'N', 'N', 'Y']
    })
    print(find_products(products))

# The .iloc method stands for "integer-location based indexing." It is used to select data by its numerical position (index) rather than by name.

# The syntax follows the format: df.iloc[row_selection, column_selection].

# : (The first part): This tells pandas to select all rows from the filtered DataFrame.

# , :1 (The second part): This tells pandas to select all columns starting from index 0 up to (but not including) index 1. In simpler terms, it grabs the first column only.