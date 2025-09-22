def run_exercise_3():
    yield "R = RED Party\nG = GREEN Party\nB = BLUE Party\n"
    party_input = yield "Choose a letter: "
    party = party_input.strip().upper()

    parties = {
        "R": "RED",
        "G": "GREEN",
        "B": "BLUE"
    }

    if party in parties:
        yield f"\n✅ You voted for the {parties[party]} party.\n"
    else:
        yield "\n❌ Invalid option.\n"
    return
