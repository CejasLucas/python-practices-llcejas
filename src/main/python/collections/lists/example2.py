from src.main.python.collections.lists.example1 import run_example_1

def run_example_2():
    count = 0
    create_word_list = run_example_1()
    word_to_search = input("Enter a word to find within the list already created: ")
    for word in create_word_list:
        if word_to_search == word:
            count =+ 1

    print(f"The word {word_to_search} is found {count} times")