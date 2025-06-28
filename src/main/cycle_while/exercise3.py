def run_exercise_3():
    first_number = float(input("Enter a decimal number: "))
    list_of_numbers = [first_number]

    while True:
        last_number = float(input("Enter a decimal number: "))
        list_of_numbers.append(last_number)
        if last_number < first_number:
            break

    last_number = list_of_numbers.pop()
    print(f"The last number is less than the first. Cut number was = {last_number}")
    print(f"List of entered numbers greater than the first: {list_of_numbers}")