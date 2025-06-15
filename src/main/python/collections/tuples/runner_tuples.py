from src.main.python.collections.tuples.launcher_tuples import menu, run
from colorama import Fore

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\n============================== COLLECTIONS PRACTICE TUPLE ==============================")
    while True:
        menu()
        try:
            choice = int(input("Enter a number: " ))
            print("")
            if 0 < choice < 4:
                run(choice)
            elif choice == 0:
                print("You have finished the program")
                break
            else:
                print("Invalid option, please re-enter a number")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue