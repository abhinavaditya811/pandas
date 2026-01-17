import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts[accounts.income < 20000].shape[0],
            accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
            accounts[accounts.income > 50000].shape[0],
        ]
    })

    return result

if __name__ == "__main__":
    accounts = pd.DataFrame({
        'account_id': [1, 2, 3, 4, 5],
        'income': [15000, 25000, 30000, 60000, 45000]
    })
    salary_categories = count_salary_categories(accounts)
    print(salary_categories)