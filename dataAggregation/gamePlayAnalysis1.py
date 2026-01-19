import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby('player_id', as_index=False)['event_date'].min()

    result.columns = ['player_id', 'first_login']

    return result

if __name__ == "__main__":
    activity = pd.DataFrame({
        'player_id': [1, 1, 2, 2, 3],
        'event_date': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-03', '2024-01-02']
    })
    print(game_analysis(activity))