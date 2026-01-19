import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    result = activities.groupby('sell_date', as_index=False)['product'].agg(
        num_sold= 'nunique',
        products= lambda x: ','.join(sorted(x.unique()))
    )

    return result

if __name__ == "__main__":
    activities = pd.DataFrame({
        'sell_date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
        'product': ['A', 'B', 'A', 'C', 'B']
    })
    categorized_products = categorize_products(activities)
    print(categorized_products)