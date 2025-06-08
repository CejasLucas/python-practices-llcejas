def run_example_2():
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))

    while first > second:
        print("The second number must be greater than the first number entered.")
        second = int(input(f"First number entered {first}. Enter the second integer: "))

    print(f"Verified: First {first} < Second {second}")