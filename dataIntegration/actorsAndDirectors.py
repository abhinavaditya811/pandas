import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director.groupby(['actor_id', 'director_id'], as_index=False).agg(
        cnt=('director_id', 'count')
    ).query('cnt >= 3')[['actor_id', 'director_id']]

    return result

if __name__ == "__main__":
    data = {
        'actor_id': [1, 1, 1, 2, 2, 3, 3, 3, 3],
        'director_id': [10, 10, 10, 20, 20, 30, 30, 30, 40]
    }
    df = pd.DataFrame(data)
    print(actors_and_directors(df))