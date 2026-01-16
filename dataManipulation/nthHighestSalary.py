import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates()

    df = df.sort_values(ascending=False)

    columns = 'getNthHighestSalary('+str(N)+')'

    if N > len(df) or N <= 0:
        return pd.DataFrame({columns: [None]})

    return pd.DataFrame({columns: [df.iloc[N-1]]})

if __name__ == "__main__":
    employee = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'salary': [100, 200, 300, 400, 500]
    })
    N = 2
    print(nth_highest_salary(employee, N))