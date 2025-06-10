from src.main.python.cycles.cycle_for.example1 import run_example_1
from src.main.python.cycles.cycle_for.example2 import run_example_2
from src.main.python.cycles.cycle_for.example3 import run_example_3
from src.main.python.cycles.cycle_for.example4 import run_example_4

def run(number):
    examples = {
        1: run_example_1,
        2: run_example_2,
        3: run_example_3,
        4: run_example_4
    }
    if number in examples:
        examples[number]()
    else:
        print("Invalid option. Please try again.")


if __name__ == "__main__":
    print("\n============CYCLES PRACTICE============")
    print("Which exercise would you like to run?")
    print("1 - Print the first 100 natural numbers")
    print("2 - Sum the first N odd numbers")
    print("3 - Calculate the factorial of a number")
    print("4 - Display the first N numbers of the Fibonacci sequence")
    print("0 - Exit")

    choice = int(input("Enter a number: "))
    print("")

    if 0 < choice < 5:
        run(choice)
    elif choice == 0:
        print("You have finished the program")
    else:
        print("Invalid option, please re-enter a number")