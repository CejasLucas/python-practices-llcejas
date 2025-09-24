def run_exercise_4():
    character_input = input("\nEnter a character: ")
    character = character_input.strip()
    vowels = "AEIOUaeiou"

    if len(character) == 1:
        if character in vowels:
            print(f"\n✅ {character} is a vowel.\n")
        else:
            print("\n❌ Not a vowel.\n")
    else:
        print("\n❌ Error: Please enter only one character.\n")
    return
