import matplotlib.pyplot as plt

PIB_2020 = {
    'Brazil': (2364409.9, '#FFB6C1'),    # Rosado claro
    'Uruguay': (120532.1, '#ADD8E6'),    # Azul pastel
    'Ecuador': (88554.7, '#00CED1'),     # Cian
    'Argentina': (440769.2, '#87CEFA'),  # Azul claro
    'Guyana': (11780.6, '#00FFFF'),      # Cian brillante
    'Colombia': (394571.1, '#40E0D0'),   # Turquesa
    'Venezuela': (116067.8, '#BA55D3'),  # Violeta medio
    'Peru': (210881.6, '#87CEEB'),       # Azul celeste
    'Suriname': (11678.2, '#4169E1'),    # Azul royal
    'Mexico': (1309880.9, '#DA70D6'),    # Violeta
    'Bolivia': (29702.8, '#8A2BE2'),     # Violeta oscuro
    'Chile': (286013.8, '#FF69B4'),      # Rosa fuerte
    'Paraguay': (37260.6, '#FF1493')     # Rosado intenso
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