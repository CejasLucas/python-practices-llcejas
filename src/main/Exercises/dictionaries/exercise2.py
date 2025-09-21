fruits_per_kilogram = {
        "apple": 1000,
        "melon": 2000,
        "mango": 3000,
        "banana": 1000,
        "orange": 2000,
        "pineapple": 3000,
        "blueberry": 6000,
        "strawberry": 5000
}

def is_validate_kilogram(kilogram):
    if kilogram < 0:
        print("Entering a kilogram in negative is invalid")
        return False
    else:
        return True


def is_validate_name(name):
    if name not in fruits_per_kilogram:
        print("Entering an empty fruit name is invalid.")
        return False
    elif name == "":
        print(f"The fruit '{name}' is not in the list.")
        return False
    else:
        return True


def run_exercise_2():
    print(f"Available fruits: {', '.join(fruits_per_kilogram.keys())}")

    while True:
        fruit_name = input("Enter the name of the fruit: ").lower()

        fruit_kilogram = float(input("Enter the number of kilos sold of that fruit: "))

        if not is_validate_kilogram(fruit_kilogram): break

        if not is_validate_name(fruit_name): break

        price_per_kilogram = fruits_per_kilogram[fruit_name]

        print(f"The total price for {fruit_kilogram} kg of {fruit_name} is: {price_per_kilogram * fruit_kilogram} units.")
        print("-----------------------------------------------------------")