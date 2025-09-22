def run_exercise_2():
    day_input = yield "Enter a number from 1 to 7 to get the day of the week: "

    try:
        day = int(day_input.strip())
    except ValueError:
        yield "\n❌ Invalid input: please enter a number."
        return

    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if day in days:
        yield f"\n✅ The day {day} is {days[day]}.\n"
    else:
        yield "\n❌ That day does not exist.\n"
    return
