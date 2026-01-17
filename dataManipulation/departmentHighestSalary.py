import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))

    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')

    mask = df['salary'] == df['max_salary']

    print(mask)

    result = df[mask]

    result = result[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']

    return result

if __name__ == "__main__":
    employee = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'salary': [100, 200, 300, 400, 500],
        'departmentId': [1, 1, 2, 2, 3]
    })
    department = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['HR', 'Engineering', 'Sales']
    })
    print(department_highest_salary(employee, department))