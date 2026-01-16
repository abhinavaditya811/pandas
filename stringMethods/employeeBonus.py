import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (~employees['name'].str.startswith('M') & employees['employee_id'] % 2 != 0)

    employees['bonus'] = np.where(mask, employees['salary'], 0)

    result = employees[['employee_id', 'bonus']].sort_values(by='employee_id')

    return result

if __name__ == "__main__":
    employees = pd.DataFrame({
        'employee_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'salary': [50000, 60000, 55000, 70000, 65000]
    })
    print(calculate_special_bonus(employees))
