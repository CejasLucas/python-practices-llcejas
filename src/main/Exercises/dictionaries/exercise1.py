phone_book = {
    'Cejas Lucas': 1169591337,
    'Diaz Brisa': 1147894526,
    'Sanchez Claudia': 1145789654,
    'Galarza Natalia': 112458794
}

def is_valid_input(data, message):
    if data == "":
        print(f"\nInvalid {message}.")
        return False
    return True


def run_exercise_1():
    print("\nLeave the name empty and press Enter to finish.")

    while True:
        username = input("\nContact name: ").strip()

        user_telephone = input("\nContact phone number: ").strip()

        if not is_valid_input(username, "username"): break

        if not is_valid_input(user_telephone, "phone number"): break

        if not user_telephone.isdigit():
            print("\nPhone number must contain only digits.")
            break

        print("-----------------------------------------")
        phone_book[username] = int(user_telephone)

    print("\nCreated contact book:")

    print(phone_book)