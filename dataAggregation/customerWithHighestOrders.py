import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders.groupby('customer_number', as_index=False).agg(
        cnt=('order_number', 'nunique')
    ).sort_values(by='cnt', ascending=False).head(1)[['customer_number']]

    return result

if __name__ == "__main__":
    orders = pd.DataFrame({
        'customer_number': [1, 1, 2, 2, 3],
        'order_number': [101, 102, 101, 103, 104],
    })
    print(largest_orders(orders))