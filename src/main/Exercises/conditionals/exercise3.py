def run_exercise_3():
    print("R = RED Party\nG = GREEN Party\nB = BLUE Party\n")
    party_input = input("Choose a letter: ")
    party = party_input.strip().upper()

    parties = {
        "R": "RED",
        "G": "GREEN",
        "B": "BLUE"
    }

    if party in parties:
        print(f"\n✅ You voted for the {parties[party]} party.\n")
    else:
        print("\n❌ Invalid option.\n")
