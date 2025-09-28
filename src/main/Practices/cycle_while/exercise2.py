def run_exercise_2():
    first = int(input("\nEnter the first integer: "))
    second = int(input("\nEnter the second integer: "))

    while first > second:
        print("The second number must be greater than the first number entered.")
        second = int(input(f"\nFirst number entered {first}. Enter the second integer: "))

    print(f"\nVerified: First {first} < Second {second}")