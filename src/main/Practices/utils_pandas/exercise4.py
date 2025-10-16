from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[4]
DATA_FILE = PROJECT_ROOT / "data" / "cars_database.csv"

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
    print(f"Searching for the file at: {DATA_FILE}\n")

    if not DATA_FILE.exists():
        raise FileNotFoundError(f"❌ El archivo no existe en: {DATA_FILE}")

    dataframe = pd.read_csv(DATA_FILE, delimiter=";")

    new_dataframe = calculated_pandas_df(dataframe)

    print(f"cars_database.csv file found, its content is as follows:\n{dataframe}\n")

    pd.set_option('display.float_format', '{:.0f}'.format)

    print(f"Car price summary with Pandas DataFrame:\n{new_dataframe}\n")