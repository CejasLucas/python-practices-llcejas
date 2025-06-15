from src.main.python.cycles.cycle_while.launcher_while import menu, run
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\n========================= WHILE CYCLE PRACTICE =========================" + Style.RESET_ALL)
    while True:
        menu()
        try:
            choice = int(input("Enter a number: " + Style.RESET_ALL))
            print("")
            if 0 < choice < 9:
                run(choice)
            elif choice == 0:
                print("You have finished the program\n")
                break
            else:
                print("Invalid option, please re-enter a number\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")