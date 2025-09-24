def run_exercise_5():
    year_input = input("Enter a year: ")
    try:
        year = int(year_input.strip())
    except ValueError:
        print("\n❌ Invalid input: please enter a valid number.\n")
        return

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"\n✅ The year {year} is a Leap Year.\n")
    else:
        print(f"\n❌ The year {year} is not a Leap Year.\n")
