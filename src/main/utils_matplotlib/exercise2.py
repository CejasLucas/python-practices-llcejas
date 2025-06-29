import matplotlib.pyplot as plt

PIB_2020 = {
    'Brazil': (2364409.9, '#4C72B0'),
    'Uruguay': (120532.1, '#C6E2DD'),
    'Ecuador': (88554.7, '#7AB0A0'),
    'Argentina': (440769.2, '#4C9F70'),
    'Guyana': (11780.6, '#BFDCE5'),
    'Colombia': (394571.1, '#2A7F62'),
    'Venezuela': (116067.8, '#3B6978'),
    'Peru': (210881.6, '#A0CBE8'),
    'Suriname': (11678.2, '#D0E1F9'),
    'Mexico': (1309880.9, '#5FB49C'),
    'Bolivia': (29702.8, '#86C5A3'),
    'Chile': (286013.8, '#8DB2D1'),
    'Paraguay': (37260.6, '#88D8C0')
}

def run_exercise_2():
    palette = [color for value, color in PIB_2020.values()]
    country_values = [value for value, color in PIB_2020.values()]
    country_names = list(PIB_2020.keys())

    plt.figure(figsize=(10, 10))
    plt.pie(
        country_values,
        labels=country_names,
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.85,
        colors=palette,
        textprops={'color': 'black', 'fontsize': 10},
        radius = 1.75
    )

    # Donut effect
    centre_circle = plt.Circle((0, 0), 0.25, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    #plt.title('GDP of Latin American Countries in 2020 (Millions USD)', fontsize=14)
    plt.gcf().canvas.manager.set_window_title("Latin American Countries in 2020")
    plt.tight_layout()
    plt.show()