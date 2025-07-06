import numpy as np

def data():
    return (
        [[0] * 9 for _ in range(3)] +
        [[0.5] * 8 + [0.7]] +
        [[1] * 9 for _ in range(3)]
    )

def run_exercise_3():
    matrix = np.array(data())
    last_row = matrix[-1]
    average = np.mean(last_row)

    print(f"This is the whole matrix:\n {matrix} \n")
    print(f"Last row selected: {last_row} \n")
    print(f"Average of the last row: {average} \n")