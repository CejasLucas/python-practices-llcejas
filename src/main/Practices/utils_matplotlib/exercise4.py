import matplotlib.pyplot as plt
import numpy as np

product_per_day = {
    'Monday': (20, 25),
    'Tuesday': (35, 32),
    'Wednesday': (30, 34),
    'Thursday': (35, 20),
    'Friday': (27, 25)
}

def run_exercise_4():
    washing_machine = [value[0] for value in product_per_day.values()]
    refrigerators = [value[1] for value in product_per_day.values()]
    days = list(product_per_day.keys())

    fig, ax1 = plt.subplots(figsize=(18, 8))
    x = np.arange(len(days))
    ax2 = ax1.twinx()
    width = 0.4

    washing_machine_color = "#3B6978"
    refrigerators_color = "#6BAF92"

    # Create bars
    pop_bars = ax1.bar(x - width/2, washing_machine, width, label='Washing Machine', color=washing_machine_color, alpha=0.8)
    area_bars = ax2.bar(x + width/2, refrigerators, width, label='Refrigerators', color=refrigerators_color, alpha=0.6)

    # Y-axis labels
    ax1.set_ylabel('Washing Machine Units', color=washing_machine_color, fontsize=13, weight='bold')
    ax2.set_ylabel('Refrigerators Units', color=refrigerators_color, fontsize=13, weight='bold')

    # X-axis labels
    ax1.set_xticks(x)
    ax1.set_xticklabels(days, rotation=0, fontsize=11)

    # Tick color match
    ax1.tick_params(axis='y', labelcolor=washing_machine_color)
    ax2.tick_params(axis='y', labelcolor=refrigerators_color)

    # Add grid for clarity
    ax1.grid(True, which='major', axis='y', linestyle='--', alpha=0.5)

    # Legend
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    fig.legend(handles1 + handles2, labels1 + labels2, loc="upper right", bbox_to_anchor=(0.9, 0.9), fontsize=13)

    # Set title and show
    plt.gcf().canvas.manager.set_window_title("Comparison of household appliances.")
    plt.tight_layout()
    plt.show()