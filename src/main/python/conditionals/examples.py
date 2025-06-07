from src.main.python.conditionals.example1 import run_example_1
from src.main.python.conditionals.example2 import run_example_2
from src.main.python.conditionals.example3 import run_example_3
from src.main.python.conditionals.example4 import run_example_4
from src.main.python.conditionals.example5 import run_example_5
from src.main.python.conditionals.example6 import run_example_6

def run(number):
    examples = {
        1: run_example_1,
        2: run_example_2,
        3: run_example_3,
        4: run_example_4,
        5: run_example_5,
        6: run_example_6
    }
    if number in examples:
        examples[number]()
    else:
        print("Invalid option. Try again.")


if __name__ == "__main__":
    print("\nWhich example do you want to run?")
    print("1 - Find the Smaller Number")
    print("2 - Day of the Week")
    print("3 - Voting System")
    print("4 - Check for Vowel")
    print("5 - Leap Year")
    print("6 - Students of an institute")
    print("0 - Exit")

    choice = int(input("Enter a number: "))
    run(choice)