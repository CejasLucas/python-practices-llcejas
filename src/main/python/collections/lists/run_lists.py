from src.main.python.collections.lists.example1 import run_example_1
from src.main.python.collections.lists.example2 import run_example_2
from src.main.python.collections.lists.example3 import run_example_3
from src.main.python.collections.lists.example4 import run_example_4
from src.main.python.collections.lists.example5 import run_example_5
from src.main.python.collections.lists.example6 import run_example_6

def run(number):
    examples = {
        1: run_example_1,
        2: run_example_2,
        3: run_example_3,
        4: run_example_4,
        5: run_example_5,
        6: run_example_6
    }
    examples[number]()

if __name__ == "__main__":
    print("\n==================COLLECTIONS PRACTICE==================")
    print("Which example would you like to run?")
    print("1 - Create a list of words and display it")
    print("2 - Count how many times a word appears in the list")
    print("3 - Replace a word in the list with another")
    print("4 - Remove a word from the list")
    print("5 - Remove from the first list the words that appear in the second list")
    print("6 - Create a reversed copy of the list")
    print("0 - Exit")

    choice = int(input("Enter a number: "))
    print("")
    if 0 < choice < 7:
        run(choice)
    elif choice == 0:
        print("You have finished the program")
    else:
        print("Invalid option, please re-enter a number")