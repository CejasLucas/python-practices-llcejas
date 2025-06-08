from src.main.python.collections.lists.example1 import run_example_1

def run_example_3():
    word_list = run_example_1()
    first_word = input("Enter the word to replace: ")
    if first_word in word_list:
        print(f"Initial list: {word_list}")
        word_change(first_word, word_list)
        print(f"Modified list: {word_list}")
    else:
        print(f"The word '{first_word}' was not found in the list.")


def word_change(first_word, word_list):
    second_word = input("Enter the second word: ")
    i = word_list.index(first_word)
    word_list[i] = second_word