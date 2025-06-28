from colorama import Fore, Style, init
init()

class ExerciseBuilder:
    def __init__(self, exercises: dict, menu_text: str):
        self.exercises = exercises
        self.menu_text = menu_text

    def show_menu(self):
        print(Fore.LIGHTWHITE_EX + Style.NORMAL + self.menu_text + Style.RESET_ALL)

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