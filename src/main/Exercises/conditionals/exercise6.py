def run_exercise_6():
    while True:
        menu_text = (
            "\nWrite the number corresponding to the day of the week to complete the task:\n"
            "1) Monday\n"
            "2) Tuesday\n"
            "3) Wednesday\n"
            "4) Thursday\n"
            "5) Friday\n"
            "0) Exit\n"
        )
        number_input = yield menu_text + "Enter a number: "

        try:
            number = int(number_input.strip())
        except ValueError:
            yield "❌ Invalid input: please enter a number.\n"
            continue

        if number == 0:
            yield "Exiting the exercise.\n"
            break

        levels = {1: level, 2: level, 3: level, 4: practical, 5: queries}

        if number in levels:
            for msg in levels[number]():
                yield msg
        else:
            yield "❌ Invalid option. Try again.\n"



def level():
    response = yield "Were there exams that day? Enter [Y] to confirm: "
    if response.strip().upper() == "Y":
        approved_input = yield "Enter the number of students who passed = "
        disapproved_input = yield "Enter the number of failed students = "
        try:
            approved = int(approved_input.strip())
            disapproved = int(disapproved_input.strip())
        except ValueError:
            yield "❌ Invalid input: numbers only.\n"
            return

        number_of_students = approved + disapproved
        if number_of_students == 0:
            yield "No students registered.\n"
        else:
            passing_percentage = (approved / number_of_students) * 100
            yield f"✅ Passing percentage: {passing_percentage:.2f}%\n"
    else:
        yield "No exams that day.\n"
    return


def practical():
    response_input = yield "Enter the attendance percentage between 0 and 100: "
    try:
        response = int(response_input.strip())
    except ValueError:
        yield "❌ Invalid input: number expected.\n"
        return

    if 0 < response <= 100:
        if response > 50:
            yield "✅ Perfect, most of the students attended\n"
        else:
            yield "⚠️ The number of student attendance is very low\n"
    else:
        yield "❌ Number outside the requested parameters\n"
    return


def queries():
    number_input = yield "Enter the number of students who attended: "
    value_input = yield "Enter the price per consultation: "

    try:
        number_of_student = int(number_input.strip())
        value_per_query = float(value_input.strip())
    except ValueError:
        yield "❌ Invalid input: numbers only.\n"
        return

    final_total_income = number_of_student * value_per_query
    yield f"✅ Final total income: ${final_total_income:.2f}\n"
    return