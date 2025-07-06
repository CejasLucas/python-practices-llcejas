import pandas as pd

def run_exercise_1():
    start_year = int(input("Year sales began: "))
    last_year = int(input("Last year of sales made: "))

    sales = dict()
    discounted_sales = dict()

    for year in range(start_year, last_year + 1):
        total = float(input(f"Enter the final sales total for year {year}: "))
        sales[year] = total
        discounted_sales[year] = total - total * 0.1

    print(f"\nSales for each year:\n{pd.Series(sales)}")

    print(f"\nSales with a 10% discount for each year:\n{pd.Series(discounted_sales)}\n")