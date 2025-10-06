from colorama import Fore, Style

class ExerciseBuilder:
    def __init__(self, exercises: dict, menu: dict):
        self.exercises = exercises
        self.menu = menu

    def show_menu(self):
        print(Fore.LIGHTWHITE_EX + Style.NORMAL)
        for key, name in self.menu.items():
            print(f" {key}. {name}")
        print(" 0. Exit")
        print(Style.RESET_ALL, end="")

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("Enter a number: "))
                print("")
                if choice in self.exercises:
                    self.exercises[choice]()
                elif choice == 0:
                    print("You have finished the program.\n")
                    break
                else:
                    print("Invalid option, please re-enter a number.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
