def run_exercise_3():
    test_number = int(input("Enter a number to calculate its factorial: "))
    if test_number < 0:
        print("There is no factorial of a negative number")
    elif test_number < 2:
        print(f"The factorial of '{test_number}' is 1")
    else:
        product = 1
        for number in range(1, test_number + 1): product *= number
        print(f"The factorial of N = '{test_number}' is {product}")