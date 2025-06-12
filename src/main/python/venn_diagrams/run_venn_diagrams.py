import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

def mostrar_diagrama():
    # Datos
    solo_moto = 5
    moto_bici = 3
    moto_auto = 20
    moto_auto_bici = 10
    solo_auto = 46
    solo_bici = 14
    auto_bici = 10

    subsets = (solo_moto, solo_auto, moto_auto, solo_bici, moto_bici, auto_bici, moto_auto_bici)

    plt.figure("Ejercicio Numero 1")
    plt.title("Diagrama de Venn - Medios de Transporte")
    diagram = venn3(subsets=subsets, set_labels=("Moto", "Auto", "Bicicleta"))

    for subset_id in ['100', '010', '110', '001', '101', '011', '111']:
        label = diagram.get_label_by_id(subset_id)
        if label is not None:
            idx_map = {
                '100': 0,
                '010': 1,
                '110': 2,
                '001': 3,
                '101': 4,
                '011': 5,
                '111': 6,
            }
            label.set_text(str(subsets[idx_map[subset_id]]))

    plt.show()  # ✅ Esto abre el gráfico si tenés backend gráfico funcionando

if __name__ == "__main__":
    mostrar_diagrama()