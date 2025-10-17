phone_book = {
    'Cejas Lucas': 1169591337,
    'Diaz Brisa': 1147894526,
    'Sanchez Claudia': 1145789654,
    'Galarza Natalia': 112458794
}

def run_exercise_1():
    print("\nCreate a dictionary where the key is the user's name and the value is their")
    print("phone number. Keep asking for contacts until the user chooses to stop.")
    print("Names must be unique (no duplicates allowed).")
    print("\n[NOTE] Leave the name empty and press Enter to finish.")

    while True:
        print("\n" + "-" * 75)
        username = input("Contact name: ").strip()
        user_telephone = input("\nContact phone number: ").strip()

        if username == "" or user_telephone == "":
            print("\n⚠️  I can't save an empty contact\n")
            print("\n" + "=" * 75)
            break

        if not user_telephone.isdigit():
            print("\n⚠️  Phone number must contain only digits.\n")
            print("\n" + "=" * 75)
            break
        phone_book[username] = int(user_telephone)

    print("\n📖  Created contact book:\n")

    for name, telephone in phone_book.items(): print(f"Name: {name} | Telephone: {telephone}")