from src.main.python.collections.dictionaries.example1 import run_example_1
from src.main.python.collections.dictionaries.example2 import run_example_2
from src.main.python.collections.dictionaries.example3 import run_example_3

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
    print("\n============================== COLLECTIONS PRACTICE ==============================")
    print("Which example would you like to run?")
    print("1 - Add contacts (name and phone number) to a dictionary. No duplicate names allowed.")
    print("2 - Fruit price calculator: enter fruit name and quantity sold to get the total price.")
    print("3 - Student grades: store students and their grades, then calculate average per student.")
    print("0 - Exit")

    choice = int(input("Enter a number: "))
    print("")
    if 0 < choice < 4:
        run(choice)
    elif choice == 0:
        print("You have finished the program")
    else:
        print("Invalid option, please re-enter a number")