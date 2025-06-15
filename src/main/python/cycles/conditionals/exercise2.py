def run_exercise_2():

    day = int(input("Enter a number from 1 to 7 to get the day of the week: "))

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
        print(f"The day {day} is {days[day]}\n")
    else:
        print("That day does not exist.\n")