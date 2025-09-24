def run_exercise_1():
    x_input = input("Please enter the first number: ")
    y_input = input("Please enter the second number: ")

    try:
        x = float(x_input.strip())
        y = float(y_input.strip())
    except ValueError:
        print("\n❌ Invalid input: make sure to type numbers only.")
        return

    print("\n🔎 Comparing the two numbers...")

    if x < y:
        print(f"✅ Result: {x} is smaller than {y}.\n")
    elif y < x:
        print(f"✅ Result: {y} is smaller than {x}.\n")
    else:
        print(f"✅ Result: both numbers are equal ({x}).\n")
