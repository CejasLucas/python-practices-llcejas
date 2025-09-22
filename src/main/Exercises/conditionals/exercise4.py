def run_exercise_4():
    character_input = yield "Enter a character: "
    character = character_input.strip()

    if len(character) == 1:
        vowels = "AEIOUaeiou"
        if character in vowels:
            yield f"\n✅ {character} is a vowel.\n"
        else:
            yield "\n❌ Not a vowel.\n"
    else:
        yield "\n❌ Error: Please enter only one character.\n"
    return
