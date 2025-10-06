def run_exercise_5():
    sum = 0
    while True:
        number = int(input("\nEnter a positive number: "))
        if number <= 0:
            break
        sum += number

    print(f"\nThe sum of the positive numbers is {sum}")