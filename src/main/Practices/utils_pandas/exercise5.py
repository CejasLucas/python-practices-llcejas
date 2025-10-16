import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def number_of_spaces(number): return print('\n' * number)

def space_with_delimiter(number, delimiter): return print(delimiter * number)

def print_ordered_provinces(series):
    provinces_sorted = series.sort_index()
    space_with_delimiter(60, '-')
    print(" " * 10 + "<< PROVINCES ORDERED ALPHABETICALLY >>")
    for i, (prov, val) in enumerate(provinces_sorted.items(), 1): print(f"{i:02d}. {prov:<25} {val:,.2f}")
    space_with_delimiter(60, '-')


def return_province_values(dataframe):
    dataframe['valor'] = pd.to_numeric(dataframe['valor'], errors='coerce')
    df = dataframe[(dataframe['alcance_tipo'] == 'PROVINCIA') & (dataframe['alcance_nombre'] != 'INDETERMINADA')]
    # This is a Series because it's the result of grouping by 'alcance_nombre' and summing only the 'valor' column

    total_by_province = df.groupby('alcance_nombre')['valor'].sum()
    total_by_province = total_by_province.sort_values(ascending=True)
    print_ordered_provinces(total_by_province)
    return total_by_province


def chart_of_values_by_province(dataframe):
    plt.figure(figsize=(14, 8))
    sns.barplot(x=dataframe.values, y=dataframe.index, palette="magma", legend=False)
    plt.gcf().canvas.manager.set_window_title("Exercise 5")
    plt.title('Total employment by province (sorted)')
    plt.xlabel('Total employment value')
    plt.ylabel('Province')
    plt.tight_layout()
    plt.show()


def data_printing(dataframe):
    space_with_delimiter(40, '=')
    print(f"- Number of records uploaded: {dataframe.size}")
    print(f"- Dataframe dimensions: {dataframe.ndim}")
    space_with_delimiter(40, '=')

    number_of_spaces(1)
    space_with_delimiter(40, '-')
    print(" " * 10 + "<< COLUMN NAMES >>")
    for i, col in enumerate(dataframe.columns): print(f"Column[{i}] {col}")

    number_of_spaces(1)
    space_with_delimiter(40, '-')
    print(" " * 10 + "<< COLUMN TYPES >> \n", dataframe.dtypes)

    number_of_spaces(1)
    space_with_delimiter(140, '-')
    print(" " * 50 + "<< FIRST 5 ROWS OF THE DATA FRAME >>\n", dataframe.head(5))

    number_of_spaces(1)
    space_with_delimiter(140, '-')
    print(" " * 50 + "<< LAST 5 ROWS OF THE DATA FRAME >>\n", dataframe.tail(5))

    number_of_spaces(2)


def run_exercise_5():
    base_path = os.path.dirname(__file__)
    file_path_test = os.path.abspath(os.path.join(base_path, "..", "..", "..", "..", "data", "commerce_database.csv"))

    print(f"Searching for the file at: {file_path_test} \n")
    data = pd.read_csv(file_path_test, delimiter=",", encoding='latin1')
    df = pd.DataFrame(data)

    data_printing(df)
    series = return_province_values(df)
    chart_of_values_by_province(series)