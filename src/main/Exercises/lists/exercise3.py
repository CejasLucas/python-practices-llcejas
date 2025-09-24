from Exercises.lists.exercise1 import run_exercise_1

def run_exercise_3():
    word_list = run_exercise_1()
    first_word = input("\nEnter the word to replace: ")
    if first_word in word_list:
        print(f"I\nnitial list: {word_list}")
        word_change(first_word, word_list)
        print(f"\nModified list: {word_list}")
    else:
        print(f"\nThe word '{first_word}' was not found in the list.")


def word_change(first_word, word_list):
    second_word = input("\nEnter the second word: ")
    i = word_list.index(first_word)
    word_list[i] = second_word