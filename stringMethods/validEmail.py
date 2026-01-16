import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    result = users[users['mail'].str.match(pattern)]

    return result

if __name__ == "__main__":
    users = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'mail': ['a@leetcode.com', '.b@leetcode.com', '-c@leetcode.com', 'd.a@leetcode.com', 'e@leetcode.com']
    })
    print(valid_emails(users))