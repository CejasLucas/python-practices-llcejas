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

def space(): print("-" * 40)
def space_with_jump(): print("\n" + "-" * 40)

def run_exercise_2():
    print("\nCreate a dictionary to store fruit prices.")
    print("The program will ask for the fruit name and quantity sold,")
    print("then calculate and display the total price.")

    print("\nIf the fruit is not in the dictionary, an error will be shown.")
    print("After each query, the user will be asked whether they want to continue.")

    space_with_jump()
    print("Fruit            | Price per Kilogram")
    space()
    for fruit, price in fruits_per_kilogram.items(): print(f"{fruit.capitalize():<16} | {price:>7} units")
    space()

    while True:
        fruit_name = input("\nEnter the name of the fruit: ").strip().lower()

        if fruit_name not in fruits_per_kilogram:
            print("\n⚠️  That fruit is not in the list. Please try again.")
            break

        try:
            fruit_kilogram = float(input("\nEnter the number of kilos sold of that fruit: "))
        except ValueError:
            print("\n⚠️  Invalid input. Please enter a numeric value for kilograms.")
            break

        if fruit_kilogram < 0:
            print("\n⚠️  Kilograms cannot be negative.")
            break

        price_per_kilogram = fruits_per_kilogram[fruit_name]
        total_price = price_per_kilogram * fruit_kilogram

        print(f"\n💰  The total price for {fruit_kilogram:.2f} kg of {fruit_name} is: {total_price:.2f} units.")
        print("\n" + "=" * 75)