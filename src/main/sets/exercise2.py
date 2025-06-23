from sets.exercise1 import create_set

def run_exercise_2():
    first_set = create_set("first")
    second_set = create_set("second")
    union_of_sets = first_set.union(second_set)

    if len(first_set) == 0: first_set.add("∅")
    if len(second_set) == 0: second_set.add("∅")
    if len(union_of_sets) == 0: union_of_sets.add("∅")
    print(f"The union of the sets {first_set} and {second_set} is {union_of_sets}")