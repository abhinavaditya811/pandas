import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses.groupby('class', as_index=False)['student'].count().query('student >= 5')[['class']]

if __name__ == "__main__":
    courses = pd.DataFrame({
        'class': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C'],
        'student': ['John', 'Jane', 'Tom', 'Jerry', 'Spike', 'Alice', 'Bob', 'Charlie', 'David', 'Eve']
    })
    print(find_classes(courses))