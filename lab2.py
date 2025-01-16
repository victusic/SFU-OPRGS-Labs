import numpy as np

def dangerous_safe_directions(coastline, ship_coords):
    directions = {
        "N": (0, 1),
        "NE": (1, 1),
        "E": (1, 0),
        "SE": (1, -1),
        "S": (0, -1),
        "SW": (-1, -1),
        "W": (-1, 0),
        "NW": (-1, 1)
    }
    
    min_distance = float('inf')
    max_distance = 0
    dangerous_dir = None
    safe_dir = None
    
    for direction, (dx, dy) in directions.items():
        direction_vector = np.array([dx, dy])
        
        for point in coastline:
            coast_vector = np.array(point) - np.array(ship_coords)
            projection = np.dot(coast_vector, direction_vector) / np.linalg.norm(direction_vector)
            
            if projection > 0:
                distance = np.linalg.norm(coast_vector)
                
                if distance < min_distance:
                    min_distance = distance
                    dangerous_dir = direction

                if distance > max_distance:
                    max_distance = distance
                    safe_dir = direction

    return dangerous_dir, safe_dir

def is_position_safe(coastline, ship_coords, safety_threshold):
    for point in coastline:
        distance = np.linalg.norm(np.array(point) - np.array(ship_coords))
        if distance < safety_threshold:
            return False
    return True

if __name__ == "__main__":
    coastline = [(1, 1), (3, 2), (5, 5), (6, 3), (4, 0)]
    ship_coords = (3, 3)
    safety_threshold = 2.5
    
    dangerous_dir, safe_dir = dangerous_safe_directions(coastline, ship_coords)
    print(f"Опасное направление: {dangerous_dir}")
    print(f"Безопасное направление: {safe_dir}")
    
    is_safe = is_position_safe(coastline, ship_coords, safety_threshold)
    print(f"Текущее положение безопасно: {is_safe}")

input('')

