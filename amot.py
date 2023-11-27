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
        centroids.append(region.centroid)
        areas.append(region.area)

    centroids_list.append(centroids)
    areas_list.append(areas)

fig, ax = plt.subplots()

for idx, centroids in enumerate(centroids_list):
    x_values = [centroid[1] for centroid in centroids]
    y_values = [centroid[0] for centroid in centroids]
    areas = areas_list[idx]
    colors = ['red' if area == 1245.0 else 'blue' for area in areas]
    
    ax.scatter(x_values, y_values, s=50, color=colors)

ax.set_xlabel('X-координата')
ax.set_ylabel('Y-координата')
plt.show()
