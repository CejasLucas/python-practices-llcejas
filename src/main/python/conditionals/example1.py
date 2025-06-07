print("CONDITIONALS PRACTICE\n")

def run_example_1():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    if x < y:
        print(f"{x} is less than {y}\n")
    elif y < x:
        print(f"{y} is less than {x}\n")
    else:
        print(f"{x} and {y} are equal\n")