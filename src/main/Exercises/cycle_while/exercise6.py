def run_exercise_6():
    limit_number = int(input("\nEnter a limit positive number: "))

    if limit_number > 0:
        total = 0
        while total < limit_number:
            number = int(input("\nEnter a positive number: "))
            if number > 0:
                total += number
            else:
                print("\nOnly positive numbers are allowed.")
        print(f"\nThe sum of the positive numbers is {total}")
    else:
        print("\nYou entered a non-positive number as the limit.")