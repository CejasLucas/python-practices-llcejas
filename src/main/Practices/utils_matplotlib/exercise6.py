import matplotlib.pyplot as plt

def run_exercise_6():

    # Data
    group_one = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    group_two = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
    grades = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Crear gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(grades, group_one, color='blue', label='Group 1', s=100, alpha=0.7)
    plt.scatter(grades, group_two, color='green', label='Group 2', s=100, alpha=0.7)

    # Añadir etiquetas y título
    plt.xlabel('Range', fontsize=12)
    plt.ylabel('Qualification', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.gcf().canvas.manager.set_window_title("Elements")
    plt.tight_layout()
    plt.show()