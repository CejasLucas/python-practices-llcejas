import random

def run_exercise_2():

    number = int(input("\nEnter a positive index from 0 to 39: "))

    if -1 < number < 40:
        numbers = tuple(random.randint(1, 10) for _ in range(40))

        print(f"\nNumber of printed element {len(numbers)}")

        print(f"\nRandomly created tuple: {numbers}")

        print(f"\nThe number at index of the tuple is [{number}] = {numbers[number]}")

    else:
        print("\nYou entered a number outside the range.")