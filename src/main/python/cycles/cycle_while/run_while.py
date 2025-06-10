from src.main.python.cycles.cycle_while.example1 import run_example_1
from src.main.python.cycles.cycle_while.example2 import run_example_2
from src.main.python.cycles.cycle_while.example3 import run_example_3
from src.main.python.cycles.cycle_while.example4 import run_example_4
from src.main.python.cycles.cycle_while.example5 import run_example_5
from src.main.python.cycles.cycle_while.example6 import run_example_6
from src.main.python.cycles.cycle_while.example7 import run_example_7
from src.main.python.cycles.cycle_while.example8 import run_example_8

def run(number):
    examples = {
        1: run_example_1,
        2: run_example_2,
        3: run_example_3,
        4: run_example_4,
        5: run_example_5,
        6: run_example_6,
        7: run_example_7,
        8: run_example_8
    }
    if number in examples:
        examples[number]()
    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    print("\n============CYCLES PRACTICE============")
    print("Which exercise would you like to run?")
    print("1 - Enter a specified amount of positive numbers")
    print("2 - Enter a second number greater than the first")
    print("3 - Keep entering decimals greater than the first")
    print("4 - Keep entering increasingly larger integers")
    print("5 - Enter numbers until a negative is entered, then sum them")
    print("6 - Enter numbers until their sum exceeds a given limit")
    print("7 - Enter numbers between two values until one is outside the range")
    print("8 - Enter even numbers while choosing to continue")
    print("0 - Exit")

    choice = int(input("Enter a number: "))
    print("")

    if 0 < choice < 9:
        run(choice)
    elif choice == 0:
        print("You have finished the program")
    else:
        print("Invalid option, please re-enter a number")