import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

centroids_list = []
areas_list = []

for i in range(100):
    circles = np.load(f"h_{i}.npy")
    labeled_image = label(circles)
    labeled_regions = regionprops(labeled_image)

    centroids = []
    areas = []

    for region in labeled_regions:
        centroid = region.centroid
        centroids.append(centroid)

        area = region.area
        areas.append(area)

    centroids_list.append(centroids)
    areas_list.append(areas)

fig, ax = plt.subplots()

trajectory_x_red = []
trajectory_y_red = []
trajectory_x_blue = []
trajectory_y_blue = []

for idx, centroids in enumerate(centroids_list):
    x_values = [centroid[1] for centroid in centroids]
    y_values = [centroid[0] for centroid in centroids]

    areas = areas_list[idx]
    colors = ['red' if area == 1245.0 else 'blue' for area in areas]

    red_indices = [i for i, color in enumerate(colors) if color == 'red']
    if red_indices:
        trajectory_x_red.extend([x_values[i] for i in red_indices])
        trajectory_y_red.extend([y_values[i] for i in red_indices])

    blue_indices = [i for i, color in enumerate(colors) if color == 'blue']
    if blue_indices:
        trajectory_x_blue.extend([x_values[i] for i in blue_indices])
        trajectory_y_blue.extend([y_values[i] for i in blue_indices])

ax.plot(trajectory_x_red, trajectory_y_red, linestyle='-', linewidth=2, color='red', label='area=1245')
ax.plot(trajectory_x_blue, trajectory_y_blue, linestyle='-', linewidth=2, color='blue', label='other')

ax.set_xlabel('X-координата')
ax.set_ylabel('Y-координата')
ax.legend()

plt.show()
