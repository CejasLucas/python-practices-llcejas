def run_exercise_1():
    count = 0
    list_of_numbers = []
    test_number = int(input("Enter the number of N numbers to be loaded into the system: "))
    if 0 < test_number < 15:
        while count < test_number:
            number = int(input(f"Enter a number for index [{count}]: "))
            list_of_numbers.append(number)
            count += 1
        print(f"List of numbers created: {list_of_numbers}")
    else:
        print("The entered number is not within the range [0,100]")