from itertools import combinations

shopping_center = {
    'Магазин A': {'Магазин B': 50, 'Магазин C': 150},
    'Магазин B': {'Магазин A': 50, 'Магазин C': 100, 'Магазин D': 300},
    'Магазин C': {'Магазин A': 150, 'Магазин B': 100},
    'Магазин D': {'Магазин B': 300}
}

def get_distance_description(distance):
    switch = {
        range(0, 51): "рядом",
        range(51, 101): "очень близко",
        range(101, 201): "недалеко",
        range(201, 501): "достаточно далеко"
    }
    
    for key, value in switch.items():
        if distance in key:
            return value
    return "очень далеко"

def describe_distance(store1, store2, shopping_center):
    if store1 not in shopping_center or store2 not in shopping_center[store1]:
        return "Информация недоступна"
    
    distance = shopping_center[store1][store2]
    return get_distance_description(distance)


def describe_multiple_stores(stores, shopping_center):
    distances = []

    for store1, store2 in combinations(stores, 2):
        if store1 in shopping_center and store2 in shopping_center[store1]:
            distances.append(shopping_center[store1][store2])
        elif store2 in shopping_center and store1 in shopping_center[store2]:
            distances.append(shopping_center[store2][store1])
    if not distances:
        return "Недостаточно данных для оценки"

    avg_distance = sum(distances) / len(distances)
    return get_distance_description(avg_distance)

print(describe_distance("Магазин A", "Магазин B", shopping_center))  # рядом
print(describe_distance("Магазин A", "Магазин D", shopping_center))  # Информация недоступна
print(describe_multiple_stores(["Магазин A", "Магазин B", "Магазин C"], shopping_center))  # недалеко
print(describe_multiple_stores(["Магазин A", "Магазин D"], shopping_center))  #Недостаточно данных для оценки

input('')
