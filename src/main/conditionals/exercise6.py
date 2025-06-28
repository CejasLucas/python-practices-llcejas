def run_exercise_6():
    print("\nWrite the number corresponding to the day of the week to complete the task: ")
    print("(1) Monday")
    print("(2) Tuesday")
    print("(3) Wednesday")
    print("(4) Thursday")
    print("(5) Friday")
    print("(0) Exit")
    number = int(input("Enter a number: "))
    levels = { 1: level, 2: level, 3: level, 4: practical, 5: queries }

    if number in levels:
        levels[number]()
    else:
        print("Invalid option. Try again.")


def level():
    response = input("Were there exams that day? Enter [Y] to confirm: ")
    if response in "Yy":
        approved = int(input("Enter the number of students who passed = "))
        disapproved = int(input("Enter the number of failed students = "))
        number_of_students = approved + disapproved
        if number_of_students == 0:
            print("No students registered.")
        else:
            passing_percentage = (approved / number_of_students) * 100
            print(f"Passing percentage: {passing_percentage:.2f}%")



def practical():
    response = int(input("Enter the attendance percentage between 0 and 100: "))
    condition = 0 < response < 100
    if condition:
        if response > 50:
            print("Perfect, most of the students attended")
        else:
            print("The number of student attendance is very low")
    else:
        print("Number outside the requested parameters")


def queries():
    number_of_student = int(input("Enter the number of students who attended: "))
    value_per_query = float(input("Enter the price per consultation: "))
    final_total_income = float(number_of_student * value_per_query)
    print(f"Final total income ${final_total_income}")