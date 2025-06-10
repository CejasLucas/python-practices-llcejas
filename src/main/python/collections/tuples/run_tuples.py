from src.main.python.collections.tuples.example1 import run_example_1
from src.main.python.collections.tuples.example2 import run_example_2
from src.main.python.collections.tuples.example3 import run_example_3

def run(number):
    examples = {
        1: run_example_1,
        2: run_example_2,
        3: run_example_3
    }
    if number in examples:
        examples[number]()
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("\n==============================COLLECTIONS PRACTICE==============================")
    print("Which example would you like to run?")
    print("1 - Create a tuple with numbers and show how many times a given number appears")
    print("2 - Display the value from a tuple (1 to 10) based on a given index")
    print("3 - Manage passengers and destinations with queries by ID or country")
    print("0 - Exit")

    choice = int(input("Enter a number: "))
    print("")
    if 0 < choice < 4:
        run(choice)
    elif choice == 0:
        print("You have finished the program")
    else:
        print("Invalid option, please re-enter a number")