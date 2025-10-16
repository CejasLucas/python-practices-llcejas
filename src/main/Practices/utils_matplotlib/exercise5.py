import matplotlib.pyplot as plt
import numpy as np

def run_exercise_5():
    # Data
    tea = np.array([1, 2, 5, 2, 1, 3])
    water = np.array([10, 3, 14, 12, 15, 13])
    coffee = np.array([5, 5, 7, 6, 7, 4])
    names = ['María', 'Pablo', 'Ema', 'Franco', 'Estefanía', 'Pedro']

    # Configuration basic
    x = np.arange(len(names))
    width = 0.25

    # Create
    fig, ax = plt.subplots(figsize=(12, 6))

    violet_color = "#6C63FF"
    water_color = "#3B6978"
    cian_color = "#00D1B2"

    ax.bar(x - width, tea, width, label='Tea', color=violet_color)
    ax.bar(x, water, width, label='Water', color=water_color)
    ax.bar(x + width, coffee, width, label='Coffee', color=cian_color)

    # Labels
    ax.set_ylabel('Number of Drinks')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=0)
    ax.legend()

    plt.gcf().canvas.manager.set_window_title("Beverage Consumption by Person")
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()