import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[views['author_id'] == views['viewer_id'], ['author_id']]

    unique_df = df['author_id'].unique()

    result = pd.DataFrame({'id': unique_df})

    result = result.sort_values(by='id', ascending=True)
    return result

if __name__ == "__main__":
    views = pd.DataFrame({
        'author_id': [1, 2, 3, 4, 5, 1, 2, 3],
        'viewer_id': [1, 2, 3, 4, 5, 2, 3, 4]
    })
    print(article_views(views))