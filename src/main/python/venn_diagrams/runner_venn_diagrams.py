from src.main.python.venn_diagrams.launcher_venn_diagrams import menu, run
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\n================== VENN DIAGRAMS PRACTICE ==================" + Style.RESET_ALL)
    while True:
        menu()
        try:
            choice = int(input("Enter a number: " + Style.RESET_ALL))
            print()
            if 1 <= choice <= 11:
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