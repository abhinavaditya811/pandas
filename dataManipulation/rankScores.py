import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)

    scores = scores.sort_values(by='rank', ascending=True)

    return scores[['score', 'rank']]

if __name__ == "__main__":
    scores = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'score': [90, 80, 90, 70, 80]
    })
    print(order_scores(scores))