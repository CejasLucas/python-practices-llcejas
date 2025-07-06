import pandas as pd
import os

def calculated_pandas_df(dataframe):
    dataframe['Price'] = pd.to_numeric(dataframe['Price'], errors='coerce')

    min_price = dataframe['Price'].min()
    max_price = dataframe['Price'].max()
    avr_price = dataframe['Price'].mean()
    min_brands = ", ".join(dataframe.loc[dataframe['Price'] == min_price, 'Brand'].astype(str).values)
    max_brands = ", ".join(dataframe.loc[dataframe['Price'] == max_price, 'Brand'].astype(str).values)

    data = {
        'Price': [min_price, max_price, avr_price],
        'Brand': [min_brands, max_brands, '—']
    }
    return pd.DataFrame(data, index=['Minimum', 'Maximum', 'Average'])


def run_exercise_4():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "..", "..", "data", "car_database.csv")
    file_path = os.path.abspath(file_path)

    print(f"Searching for the file at: {file_path}\n")

    dataframe = pd.read_csv(file_path, delimiter=";")

    new_dataframe = calculated_pandas_df(dataframe)

    print(f"car_database.csv file found, its content is as follows:\n{dataframe}\n")

    pd.set_option('display.float_format', '{:.0f}'.format)

    print(f"Car price summary with Pandas DataFrame:\n{new_dataframe}\n")