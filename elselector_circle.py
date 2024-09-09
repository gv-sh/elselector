import numpy as np
import matplotlib.pyplot as plt

def generate_parallel_lines_circle(radius, m, h):
    # Calculate diameter
    diameter = 2 * radius

    # Generate lines
    lines = []
    d = -radius
    while d <= radius:
        # Calculate y-intercept
        b = d * np.sqrt(1 + m**2)

        # Calculate intersection points with the circle
        discriminant = radius**2 * (1 + m**2) - b**2
        if discriminant >= 0:
            x1 = (-m*b - np.sqrt(discriminant)) / (1 + m**2)
            y1 = m * x1 + b
            x2 = (-m*b + np.sqrt(discriminant)) / (1 + m**2)
            y2 = m * x2 + b
            lines.append([(x1, y1), (x2, y2)])

        d += h

    return lines

def draw_and_save_image_circle(radius, lines, filename='parallel_lines_circle.png'):
    plt.figure(figsize=(10, 10))
    plt.xlim(-radius, radius)
    plt.ylim(-radius, radius)

    # Draw the circle
    circle = plt.Circle((0, 0), radius, fill=False)
    plt.gca().add_artist(circle)

    for line in lines:
        x_values, y_values = zip(*line)
        plt.plot(x_values, y_values, 'b-')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(filename)
    plt.close()

# Example usage
radius = 10
m = 0.50  # slope
h = 1     # line interdistance

lines = generate_parallel_lines_circle(radius, m, h)
draw_and_save_image_circle(radius, lines)
