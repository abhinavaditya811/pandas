import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets.loc[tweets['content'].str.len() > 15, ['tweet_id']]
    return df

if __name__ == "__main__":
    tweets = pd.DataFrame({
        'tweet_id': [1, 2, 3, 4, 5],
        'content': ['Hello world!', 'This is a longer tweet that exceeds the limit.', 'Short', 'Another long tweet that should be filtered out.', 'Tiny']
    })
    print(invalid_tweets(tweets))