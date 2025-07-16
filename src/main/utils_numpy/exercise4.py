import numpy as np

def square_matrix_with_values_between_five_and_fifteen():
    return np.random.uniform(5, 15, size=(5, 5))

def square_matrix_with_values_between_zero_and_one():
    return np.random.rand(5, 5)

def elements_greater_than(matrix, number):
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            value = matrix[i][j]
            if value > number:
                print(f"Matrix[{i}][{j}] = {value}")


def run_exercise_4():
    first_matrix = square_matrix_with_values_between_five_and_fifteen()
    second_matrix = square_matrix_with_values_between_zero_and_one()

    print("\n--- First matrix (5-15) ---\n", first_matrix)
    print("\n--- Second matrix (0-1) ---\n", second_matrix)
    print("\n--- Elements > 0.5 in second matrix ---")
    elements_greater_than(second_matrix, 0.5)