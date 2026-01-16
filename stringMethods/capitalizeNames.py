import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()

    return users.sort_values(by='user_id')

if __name__ == "__main__":
    users = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'name': ['alice', 'bob', 'charlie', 'david', 'eve']
    })
    print(fix_names(users))