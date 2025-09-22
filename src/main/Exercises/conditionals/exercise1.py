def run_exercise_1():
    x_input = yield "Please enter the first number: "
    y_input = yield "Please enter the second number: "

    try:
        x = float(x_input.strip())
        y = float(y_input.strip())
    except ValueError:
        yield "\n❌ Invalid input: make sure to type numbers only."
        return
    yield "\n🔎 Comparing the two numbers..."

    if x < y:
        yield f"✅ Result: {x} is smaller than {y}.\n"
    elif y < x:
        yield f"✅ Result: {y} is smaller than {x}.\n"
    else:
        yield f"✅ Result: both numbers are equal ({x}).\n"
    return
