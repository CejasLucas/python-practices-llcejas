import random

def run_exercise_2():

    number = int(input("Enter a positive index from 0 to 39: "))

    if -1 < number < 40:
        numbers = tuple(random.randint(1, 10) for _ in range(40))

        print(f"Number of printed element {len(numbers)}")

        print(f"Randomly created tuple: {numbers}")

        print(f"The number at index of the tuple is [{number}] = {numbers[number]}")

    else:
        print("You entered a number outside the range.")