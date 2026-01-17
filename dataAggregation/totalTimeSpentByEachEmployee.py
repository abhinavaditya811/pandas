import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']

    result = employees.groupby(['event_day', 'emp_id'], as_index=False)['total_time'].sum()

    result.columns = ['day', 'emp_id', 'total_time']
    return result

if __name__ == "__main__":
    employees = pd.DataFrame({
        'emp_id': [1, 1, 2, 2, 3],
        'event_day': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
        'in_time': [8, 13, 9, 8, 10],
        'out_time': [12, 17, 17, 16, 15]
    })
    print(total_time(employees))