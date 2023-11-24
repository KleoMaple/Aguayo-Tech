
# Funcion recursiva que retorna todos los subconjuntos de una lista
def recursive_subsets(actual, set):
    if set: 
        return recursive_subsets(actual, set[1:]) + recursive_subsets(actual + [set[0]], set[1:])

    return[actual]  

def subsets(items):
    """
    Recibe una lista y retorna todos los subconjuntos de la lista
    """
    return recursive_subsets([], items)

def get_below_weight_sets(subsets, weight_limit: int):
    """
    Recibe una lista de subconjuntos y retorna todos los subconjuntos que su peso total es igual o menor que el limite del peso
    """
    items_below_weight = []
    for set in subsets:
        if sum(set) <= weight_limit:
            items_below_weight.append(set)
    
    return items_below_weight
        