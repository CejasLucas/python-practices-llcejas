import random

def run_example_1():
    number = int(input("Enter a positive number from [1,50]: "))

    numbers = tuple(random.randint(1, 50) for _ in range(100))

    print(f"Randomly created tuple: {numbers}")

    print(f"The entered number '{number}' is repeated within the tuple {numbers.count(number)} times")