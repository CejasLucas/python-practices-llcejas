from Exercises.lists.exercise1 import run_exercise_1

def run_exercise_4():
    word_list = run_exercise_1()
    word_to_search = input("Enter a word to search for in the list and delete it: ")

    if word_to_search in word_list:
        word_list.remove(word_to_search)
        print(f"The word '{word_to_search}' was deleted.")
        print(f"Updated list: {word_list}")
    else:
        print(f"The word '{word_to_search}' was not found in the list.")