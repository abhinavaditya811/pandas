import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_ids = orders['customerId']

    mask = ~customers['id'].isin(ordered_ids)

    result = customers.loc[mask, ['name']]
    result.columns = ['Customers']

    return result

if __name__ == "__main__":
    customers = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    })
    orders = pd.DataFrame({
        'orderId': [101, 102, 103],
        'customerId': [1, 2, 3]
    })
    print(find_customers(customers, orders))