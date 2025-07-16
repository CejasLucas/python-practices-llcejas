import pandas as pd

data = {
    "Cejas": 10,
    "Diaz": 9.5,
    "Rodriguez": 8,
    "Uriarte": 7.5,
    "Martins": 10,
    "Coronel": 4,
    "Paz": 2.5,
    "Messi": 1,
    "Cerrito": 3.5,
    "Lopez": 6
}

def calculated_pandas_series(serie):
    return pd.Series(
        [serie.min(), serie.max(), serie.mean()],
        index=["Minimum", "Maximum", "Average"]
    )

def run_exercise_2():
    pandas_series = pd.Series(data.values(), index=data.keys())

    print(f"\nStudents with their notes:\n{pandas_series}")

    print(f"\nCalculated the maximum, minimum and average:\n{calculated_pandas_series(pandas_series)}\n")