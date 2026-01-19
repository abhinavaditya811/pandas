import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id').agg(
        cnt = ('subject_id', 'nunique')
    ).reset_index()

    return result

if __name__ == "__main__":
    teacher = pd.DataFrame({
        'teacher_id': [1, 1, 2, 2, 3],
        'subject_id': [101, 102, 101, 103, 104]
    })
    print(count_unique_subjects(teacher))