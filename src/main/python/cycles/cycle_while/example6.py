def run_example_6():
    limit_number = int(input("Enter a limit positive number: "))

    if limit_number > 0:
        total = 0
        while total < limit_number:
            number = int(input("Enter a positive number: "))
            if number > 0:
                total += number
            else:
                print("Only positive numbers are allowed.")
        print(f"The sum of the positive numbers is {total}")
    else:
        print("You entered a non-positive number as the limit.")