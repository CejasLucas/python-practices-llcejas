def run_exercise_8():
    list_of_numbers = []
    while True:
        number = int(input("Enter an even number: "))
        if number % 2 == 0:
            print(f"Great, the number {number} is even")
            list_of_numbers.append(number)
        else:
            print(f"This is an odd number {number}")
            break
    print(f"List of entered even numbers: {list_of_numbers}")
