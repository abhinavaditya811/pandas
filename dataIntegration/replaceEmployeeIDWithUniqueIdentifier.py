import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employees, employee_uni, how='left', on='id')

    return result[['unique_id', 'name']]

if __name__ == "__main__":
    employees = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie']
    })
    employee_uni = pd.DataFrame({
        'id': [1, 2, 3],
        'unique_id': ['U001', 'U002', 'U003']
    })
    print(replace_employee_id(employees, employee_uni))