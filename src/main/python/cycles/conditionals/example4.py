print("CONDITIONALS PRACTICE\n")

def run_example_4():

    character = input("Enter a character: ")

    if len(character) == 1 :
        vowels = "AEIOUaeiou"
        if character in vowels:
            print(f"{character} is a vowel.\n")
        else:
            print("Not a vowel.\n")
    else:
        print(print("Error: Please enter only one character.\n"))
        return