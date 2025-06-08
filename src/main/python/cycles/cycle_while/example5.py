def run_example_5():
    sum = 0
    while True:
        number = int(input("Enter a positive number: "))
        if number <= 0:
            break
        sum += number

    print(f"The sum of the positive numbers is {sum}")