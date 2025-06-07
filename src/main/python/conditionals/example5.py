print("CONDITIONALS PRACTICE\n")

def run_example_5():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"The year {year} is a Leap Year.\n")
    else:
        print(f"The year {year} is not a Leap Year.\n")