def menu():
    return [
        {
            "id": 0,
            "file_name": "conditionals",
            "name": "Conditionals",
            "submenu_func": "src.main.Modules.conditionals.get_conditionals_exercises"
        },
        {
            "id": 1,
            "file_name": "cycle_for",
            "name": "Cycle FOR",
            "submenu_func": "src.main.Modules.cycle_for.get_cycle_for_exercises"
        },
        {
            "id": 2,
            "file_name": "cycle_while",
            "name": "Cycle WHILE",
            "submenu_func": "src.main.Modules.cycle_while.get_cycle_while_exercises"
        },
        {
            "id": 3,
            "file_name": "dictionaries",
            "name": "Dictionaries",
            "submenu_func": "src.main.Modules.dictionaries.get_dictionaries_exercises"
        },
        {
            "id": 4,
            "file_name": "lists",
            "name": "Lists",
            "submenu_func": "src.main.Modules.lists.get_lists_exercises"
        },
        {
            "id": 5,
            "file_name": "sets",
            "name": "Sets",
            "submenu_func": "src.main.Modules.sets.get_sets_exercises"
        },
        {
            "id": 6,
            "file_name": "tuples",
            "name": "Tuples",
            "submenu_func": "src.main.Modules.tuples.get_tuples_exercises"
        },
        {
            "id": 7,
            "file_name": "utils_matplotlib",
            "name": "Matplotlib",
            "submenu_func": "src.main.Modules.utils_matplotlib.get_matplotlib_exercises"
        },
        {
            "id": 8,
            "file_name": "utils_networkx",
            "name": "Networkx",
            "submenu_func": "src.main.Modules.utils_networkx.get_networkx_exercises"
        },
        {
            "id": 9,
            "file_name": "utils_numpy",
            "name": "Numpy",
            "submenu_func": "src.main.Modules.utils_numpy.get_numpy_exercises"
        },
        {
            "id": 10,
            "file_name": "utils_pandas",
            "name": "Pandas",
            "submenu_func": "src.main.Modules.utils_pandas.get_pandas_exercises"
        },
        {
            "id": 11,
            "file_name": "utils_venn_diagrams",
            "name": "Venn Diagrams",
            "submenu_func": "src.main.Modules.utils_venn_diagrams.get_venn_diagrams_exercises"
        }
    ]
