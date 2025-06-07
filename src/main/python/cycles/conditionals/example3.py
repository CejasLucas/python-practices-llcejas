print("CONDITIONALS PRACTICE\n")

def run_example_3():
    print("R = RED Party")
    print("G = GREEN Party")
    print("B = BLUE Party")
    party = input("Choose a letter: ").upper()

    parties = {
        "R": "RED",
        "G": "GREEN",
        "B": "BLUE"
    }

    if party in parties:
        print(f"You voted for the {parties[party]} party.\n")
    else:
        print("Invalid option.\n")