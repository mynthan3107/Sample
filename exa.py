import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

# Data for the segments
segments = [
    ("Anything\nAny Device", 60),
    ("Anyone\nAnybody", 60),
    ("Any Service\nAny Business", 60),
    ("Any Path\nAny Network", 60),
    ("Any Place\nAnywhere", 60),
    ("Anytime\nAny Context", 60)
]

# Colors for the segments
colors = ['#005cb9', '#0072c6', '#0085d4', '#2196f3', '#42a5f5', '#64b5f6']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Create the circular segments
start_angle = 90
for i, (label, size) in enumerate(segments):
    wedge = Wedge(center=(0, 0), r=1, theta1=start_angle, theta2=start_angle+size, facecolor=colors[i], edgecolor='white', linewidth=2)
    ax.add_patch(wedge)
    start_angle += size

# Add text annotations
start_angle = 90
for i, (label, size) in enumerate(segments):
    angle = np.deg2rad(start_angle + size / 2)
    x = 1.2 * np.cos(angle)
    y = 1.2 * np.sin(angle)
    ha = 'right' if x < 0 else 'left'
    va = 'top' if y < 0 else 'bottom'
    ax.text(x, y, label, ha=ha, va=va, fontsize=12, color='black', weight='bold')
    start_angle += size

# Add the central text
ax.text(0, 0, "The\nINTERNET\nof\nTHINGS", ha='center', va='center', fontsize=16, weight='bold', color='#005cb9')

# Set limits and aspect
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Remove axis
ax.axis('off')

# Save the figure
plt.savefig('/mnt/data/iot_circular_diagram.png', dpi=300, bbox_inches='tight')
plt.show()
