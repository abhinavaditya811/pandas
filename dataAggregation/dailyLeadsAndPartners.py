import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id', 'make_name'], as_index=False).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).sort_values(by=['make_name', 'date_id'], ascending=False)

    return result

if __name__ == "__main__":
    daily_sales = pd.DataFrame({
        'date_id': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
        'make_name': ['Toyota', 'Toyota', 'Honda', 'Honda', 'Ford'],
        'lead_id': [1, 2, 1, 3, 4],
        'partner_id': [10, 20, 10, 30, 40]
    })
    result = daily_leads_and_partners(daily_sales)
    print(result)