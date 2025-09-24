def run_exercise_1():
    x_input = input("\nPlease enter the first number: ")
    y_input = input("\nPlease enter the second number: ")

    try:
        x = float(x_input.strip())
        y = float(y_input.strip())
    except ValueError:
        print("\n❌ Invalid input: make sure to type numbers only.")
        return

    print("\n🔎 Comparing the two numbers...")

    if x < y:
        print(f"\nResult: {x} is smaller than {y}.")
    elif y < x:
        print(f"\nResult: {y} is smaller than {x}.")
    else:
        print(f"\nResult: both numbers are equal ({x}).")
    return
