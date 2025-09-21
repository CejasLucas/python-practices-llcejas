def run_exercise_7():
    list_of_numbers = []

    while True:
        min = float(input("Enter the minimum of the range: "))
        max = float(input("Enter the maximum of the range: "))
        if min > max:
            print("The maximum must be greater than the minimum.")
        else:
            print(f"Perfect, your range is the following [{min},{max}]")
            break

    while True:
        number = float(input("Enter a number: "))
        if min < number < max:
            list_of_numbers.append(number)
        else:
            break

    print(f"List of numbers within the established range [{min},{max}]")
    print(list_of_numbers)