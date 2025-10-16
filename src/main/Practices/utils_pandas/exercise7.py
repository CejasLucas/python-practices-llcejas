import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

custom_colors = ['#6C63FF', '#F5B7B1', '#FF6584']

def print_seniority_stats(df):
    df['yrs.service'] = pd.to_numeric(df['yrs.service'], errors='coerce')
    min_years = df['yrs.service'].min()
    max_years = df['yrs.service'].max()
    mean_years = df['yrs.service'].mean()

    print("\n" + "=" * 60)
    print(">> Seniority Statistics (Years of Service):")
    print(f"- Minimum: {min_years:.2f} years")
    print(f"- Maximum: {max_years:.2f} years")
    print(f"- Average: {mean_years:.2f} years")
    print("=" * 60)


def plot_rank_pie_chart(df):
    rank_counts = df['rank'].value_counts()
    labels = rank_counts.index
    sizes = rank_counts.values

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=custom_colors[:len(labels)],
        textprops={'fontsize': 10, 'fontweight': 'bold'}
    )
    plt.title("Percentage of Professors by Rank", fontsize=16)
    plt.gcf().canvas.manager.set_window_title("Exercise 7")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def aggregate_salary_stats(df):
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df['rank'] = df['rank'].astype(str)

    aggregation = df.groupby('rank')['salary'].agg([
        ('Sum', np.sum),
        ('Mean', np.mean),
        ('Standard Deviation', np.std)
    ]).sort_values(by='Sum', ascending=False)

    print("\n" + "-" * 80)
    print(">> Aggregated Salary Statistics by Rank:")
    print(aggregation)
    print("-" * 80)
    return aggregation


def run_exercise_7():
    base_path = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(base_path, "..", "..", "..", "..", "data", "salaries_database.csv"))

    print(f"Loading salary data from: {file_path}")
    df = pd.read_csv(file_path, delimiter=",", encoding="latin1")

    print_seniority_stats(df)
    plot_rank_pie_chart(df)
    aggregate_salary_stats(df)