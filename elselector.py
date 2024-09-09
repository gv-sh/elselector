import numpy as np
import matplotlib.pyplot as plt

def generate_parallel_lines(x_min, x_max, y_min, y_max, m, h):
    # Calculate center point
    center_x = (x_min + x_max) / 2
    center_y = (y_min + y_max) / 2

    # Calculate perpendicular slope
    m_perp = -1 / m if m != 0 else float('inf')

    # Generate lines
    lines = []
    d = 0
    while True:
        # Calculate offset from center
        dx = d / np.sqrt(1 + m_perp**2)
        dy = m_perp * dx

        # Calculate start and end points of the line
        x1 = x_min
        y1 = center_y + dy + m * (x1 - (center_x + dx))
        x2 = x_max
        y2 = center_y + dy + m * (x2 - (center_x + dx))

        # Check if line is out of bounds
        if y1 < y_min and y2 < y_min or y1 > y_max and y2 > y_max:
            break

        lines.append([(x1, y1), (x2, y2)])

        # Add line in opposite direction from center
        y1 = center_y - dy + m * (x1 - (center_x - dx))
        y2 = center_y - dy + m * (x2 - (center_x - dx))
        lines.append([(x1, y1), (x2, y2)])

        d += h

    return lines

def draw_and_save_image(x_min, x_max, y_min, y_max, lines, filename='parallel_lines.png'):
    plt.figure(figsize=(10, 10))
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    for line in lines:
        x_values, y_values = zip(*line)
        plt.plot(x_values, y_values, 'b-')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(filename)
    plt.close()

# Example usage
x_min, x_max, y_min, y_max = -10, 10, -10, 10
m = 0.50  # slope
h = 1    # line interdistance

lines = generate_parallel_lines(x_min, x_max, y_min, y_max, m, h)
draw_and_save_image(x_min, x_max, y_min, y_max, lines)
