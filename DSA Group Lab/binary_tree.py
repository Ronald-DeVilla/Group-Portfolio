import math

def calculate_node_positions(values, container_width=1200, node_size=50, vertical_spacing=100):
    positions = []
    for i, value in enumerate(values):
        level = math.floor(math.log2(i + 1))
        index_in_level = i - (math.pow(2, level) - 1)
        nodes_in_level = math.pow(2, level)
        x = (container_width / (nodes_in_level + 1)) * (index_in_level + 1) - node_size / 2
        y = level * vertical_spacing
        positions.append({
            'value': value,
            'x': int(x),
            'y': int(y),
            'level': level
        })

    return positions


def calculate_lines(positions, node_size=50):
    lines = []
    for i in range(1, len(positions)):
        parent_index = math.floor((i - 1) / 2)
        
        x1 = positions[parent_index]['x'] + node_size // 2
        y1 = positions[parent_index]['y'] + node_size // 2
        x2 = positions[i]['x'] + node_size // 2
        y2 = positions[i]['y'] + node_size // 2
        
        lines.append({
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2
        })
    return lines