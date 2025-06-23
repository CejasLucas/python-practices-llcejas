from colorama import Fore, Style

class ExerciseBuilder:
    def __init__(self, exercises: dict, menu_text: str):
        self.exercises = exercises
        self.menu_text = Fore.LIGHTWHITE_EX + Style.DIM + menu_text + Style.RESET_ALL

    def show_menu(self):
        print(self.menu_text)

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