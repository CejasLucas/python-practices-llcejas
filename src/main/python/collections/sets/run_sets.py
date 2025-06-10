from src.main.python.collections.sets.example1 import run_example_1
from src.main.python.collections.sets.example2 import run_example_2
from src.main.python.collections.sets.example3 import run_example_3
from src.main.python.collections.sets.example4 import run_example_4

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
    print("\n============================== COLLECTIONS PRACTICE ==============================")
    print("Which example would you like to run?")
    print("1 - Intersection of sets without duplicates")
    print("2 - Union of sets without duplicates")
    print("3 - Difference of sets without duplicates")
    print("4 - Set operations toolkit (union, intersection, difference, equality, deduplication)")
    print("0 - Exit")

    choice = int(input("Enter a number: "))
    print("")
    if 0 < choice < 5:
        run(choice)
    elif choice == 0:
        print("You have finished the program")
    else:
        print("Invalid option, please re-enter a number")