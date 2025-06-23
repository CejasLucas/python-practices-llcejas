def run_exercise_1():
    number = int(input("Enter the number of words: "))
    word_list = []

    for i in range(number):
        word = input(f"Enter word {i + 1}: ")
        word_list.append(word)

    print(f"The created list is: {word_list} \n")
    return word_list