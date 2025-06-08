def run_example_4():
    previous_number = float(input("Enter a decimal number: "))
    list_of_numbers = [previous_number]

    while True:
        last_number = float(input("Enter a decimal number: "))
        list_of_numbers.append(last_number)
        if last_number < previous_number:
            break
        previous_number = last_number

    last_number = list_of_numbers.pop()
    print(f"The last number was less than to the previous. Cut number was = {last_number}")
    print(f"List of exponential numbers: {list_of_numbers}")