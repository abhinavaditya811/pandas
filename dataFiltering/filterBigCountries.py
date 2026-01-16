import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), ['name', 'area', 'population']]
    return result

if __name__ == "__main__":
    world = pd.DataFrame({
        'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan'],
        'area': [652230, 28748, 2381741, 468, 1246700, 2780400, 29743, 7692024, 83871, 86600],
        'population': [38928346, 2877797, 43851044, 77265, 32866272, 45195777, 2963234, 25499884, 9006398, 10139177]
    })
    print(big_countries(world))