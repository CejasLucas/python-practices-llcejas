from src.main.python.collections.lists.example1 import run_example_1

def run_example_4():
    word_list = run_example_1()
    word_to_search = input("Enter a word to search for in the list and delete it: ")

    if word_to_search in word_list:
        word_list.remove(word_to_search)
        print(f"The word '{word_to_search}' was deleted.")
        print(f"Updated list: {word_list}")
    else:
        print(f"The word '{word_to_search}' was not found in the list.")