students = {
    "Benitez Nicolas": [10, 9, 7, 8],
    "Rodrigo Mamani" : [10, 6, 4, 2],
    "Leonel Cejas": [10, 8, 0, 10],
    "Diaz Joaquin": [8, 9, 7, 6]
}

def run_exercise_3():
    index = 0
    notes = list()

    print("\nCreate a program to store student names and their grades.")
    print("Each student can have a different number of grades.")
    print("Use a dictionary where keys are student names and values are lists of grades.")

    print("\nAsk how many students will be entered, then ask for each name and grades")
    print("(until a negative number is entered). At the end, display each student")
    print("with their average grade. If a name is repeated, show an error.")

    print("\nThe cut-off condition is given if a grade is entered outside the range [0,10]")
    name_student = input("\nEnter the student's name: ")

    if name_student in students:
        print("❌ Error: That name is already on the student list.")
        return

    while True:
        try:
            note_input = input(f"\nEnter note [{index}] for {name_student}: ")
            note = float(note_input)

            if note < 0 or note > 10: break
            notes.append(note)
            index += 1

        except ValueError:
            print("⚠️ Error: Please enter a valid number (float).")

    students[name_student] = notes

    print("\nFinal average of the students loaded.")
    for student, grades in students.items():
        if grades:
            average = sum(grades) / len(grades)
            print(f"Grade average: {average:.2f} | Student name: {student}")
        else:
            print(f"Grade average: N/A | Student name: {student}")