def run_exercise_1():
    number = int(input("\nEnter the number of words: "))
    word_list = []

    for i in range(number):
        word = input(f"\nEnter word {i + 1}: ")
        word_list.append(word)

    print(word_list)
    return word_list