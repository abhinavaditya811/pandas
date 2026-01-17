import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates()

    employee = employee.sort_values(ascending=False)

    columns = 'SecondHighestSalary'

    if len(employee) < 2:
        return pd.DataFrame({ columns: [None] })

    return pd.DataFrame({ columns: [employee.iloc[1]] })

if __name__ == "__main__":
    employee = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'salary': [100, 200, 300, 400, 500]
    })
    print(second_highest_salary(employee))