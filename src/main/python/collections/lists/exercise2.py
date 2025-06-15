from src.main.python.collections.lists.exercise1 import run_exercise_1

def run_exercise_2():
    count = 0
    create_word_list = run_exercise_1()
    word_to_search = input("Enter a word to find within the list already created: ")
    for word in create_word_list:
        if word_to_search == word:
            count =+ 1

    print(f"The word {word_to_search} is found {count} times")