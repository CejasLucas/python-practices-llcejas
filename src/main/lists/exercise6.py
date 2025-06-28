from src.main.lists.exercise1 import run_exercise_1

def run_exercise_6():
    first_word_list = run_exercise_1()
    second_word_list = []

    for i in range(len(first_word_list) - 1, -1, -1):
        second_word_list.append(first_word_list[i])

    print("Original list:")
    print(first_word_list)

    print("Reversed list:")
    print(second_word_list)