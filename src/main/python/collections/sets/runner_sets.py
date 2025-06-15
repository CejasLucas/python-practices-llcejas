from src.main.python.collections.sets.launcher_sets import menu, run
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\n============================== COLLECTIONS PRACTICE SET ==============================")
    while True:
        menu()
        try:
            choice = int(input("Enter a number: " + Style.RESET_ALL))
            print("")
            if 0 < choice < 5:
                run(choice)
            elif choice == 0:
                print("You have finished the program.\n")
                break
            else:
                print("Invalid option, please re-enter a number.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue