import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r'(^|\s)DIAB1'
    result = patients.loc[patients['conditions'].str.contains(pattern, case = 'False'), ['patient_id', 'patient_name', 'conditions']]

    return result

if __name__ == "__main__":
    patients = pd.DataFrame({
        'patient_id': [1, 2, 3, 4, 5],
        'patient_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'conditions': ['ACNE +DIAB100, HYPER2', 'HYPER2, DIAB201', 'DIAB1', 'HYPER2', 'DIAB1, HYPER2, ASTHMA']
    })
    print(find_patients(patients))