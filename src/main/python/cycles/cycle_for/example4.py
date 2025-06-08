def run_example_4():
    x, y, z = 1, 1, 1
    fibonacci_sequence = []
    test_number = int(input("Enter a number to calculate its Fibonacci sequence: "))
    if test_number > 0:
        for number in range(test_number):
            z = x + y
            y = x
            x = z
            fibonacci_sequence.append(x)
        print("For the number N the following Fibonacci sequence was created")
        print(fibonacci_sequence)
    else:
        print("Negative numbers are not allowed")