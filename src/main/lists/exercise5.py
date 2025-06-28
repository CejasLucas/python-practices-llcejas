from src.main.lists.exercise1 import run_exercise_1

def run_exercise_5():
    first_word_list = run_exercise_1()
    second_word_list = run_exercise_1()

    for word in range(len(first_word_list) - 1, -1, -1):
        if first_word_list[word] in second_word_list:
            del first_word_list[word]

    print("Updated first list (after deletions):")
    print(first_word_list)