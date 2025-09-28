import matplotlib.pyplot as plt

PIB_2020 = {
    'Brazil': (2364409.9, '#4C72B0'),
    'Mexico': (1309880.9, '#5FB49C'),
    'Argentina': (440769.2, '#4C9F70'),
    'Colombia': (394571.1, '#2A7F62'),
    'Chile': (286013.8, '#8DB2D1'),
    'Peru': (210881.6, '#A0CBE8'),
    'Uruguay': (120532.1, '#C6E2DD'),
    'Venezuela': (116067.8, '#3B6978'),
    'Ecuador': (88554.7, '#7AB0A0'),
    'Paraguay': (37260.6, '#88D8C0'),
    'Bolivia': (29702.8, '#86C5A3'),
    'Guyana': (11780.6, '#BFDCE5'),
    'Suriname': (11678.2, '#D0E1F9'),
}

def run_exercise_1():
    country_names = list(PIB_2020.keys())
    country_values = [value for value, color in PIB_2020.values()]
    palette = [color for value, color in PIB_2020.values()]

    plt.figure(figsize=(16, 9), constrained_layout=True)
    bars = plt.bar(country_names, country_values, color=palette)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 f'{height:,.0f}', ha='center', va='bottom',
                 fontsize=8, rotation=0)

    # Labels
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('GDP (Million USD)', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()