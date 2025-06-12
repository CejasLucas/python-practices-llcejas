students = {
    "Benitez Nicolas": [10, 9, 7, 8],
    "Rodrigo Mamani" : [10, 6, 4, 2],
    "Leonel Cejas": [10, 8, 0, 10],
    "Diaz Joaquin": [8, 9, 7, 6]
}

def run_example_3():
    index = 0

    notes = list()

    print("The cut-off condition is given if a grade is entered outside the range [0,10]")

    name_student = input("Enter the student's name: ")

    note = float(input(f"Enter note [{index}] for {name_student}: "))

    while -1 < note < 11:
        index += 1
        notes.append(note)
        students[name_student] = notes
        note = float(input(f"Enter note [{index}] for {name_student}: "))

    print("\nFinal average of the students loaded.")
    for student, grades in students.items():
        average = sum(grades) / len(grades)
        print(f"Grade average: {average:.2f} | Student name: {student}")