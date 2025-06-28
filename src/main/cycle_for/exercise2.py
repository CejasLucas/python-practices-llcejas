def run_exercise_2():
    sum = 0
    odd_numbers = []
    stop = int(input("Enter a number: "))
    for number in range(0,stop):
        if number % 2 != 0:
            odd_numbers.append(number)
            sum += number

    print(f"List odd numbers found: {odd_numbers}")
    print(f"The sum of the first N = {stop} numbers is {sum}")