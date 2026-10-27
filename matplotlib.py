
import math
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

# Input
R = float(input("Enter Cell Radius (km): "))

# Frequency reuse parameters
i, j = 2, 1
N = i*i + i*j + j*j
D = R * math.sqrt(3*N)

labels = ["A", "B", "C", "D", "E", "F", "G"]
colors = ["red", "deepskyblue", "lightgreen",
          "orange", "violet", "yellow", "pink"]

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect("equal")
ax.axis("off")

# Draw multiple hexagonal cells
limit = 4

for q in range(-limit, limit + 1):
    for r in range(-limit, limit + 1):

        # Position of each hexagonal cell
        x = math.sqrt(3) * R * (q + r/2)
        y = 1.5 * R * r

        # Assign one of seven frequency groups
        group = (q + 5*r) % 7

        hexagon = RegularPolygon(
            (x, y),
            numVertices=6,
            radius=R,
            orientation=math.radians(30),
            facecolor=colors[group],
            edgecolor="darkgreen",
            linewidth=2
        )

        ax.add_patch(hexagon)

        # Display frequency group label
        ax.text(
            x, y, labels[group],
            ha="center", va="center",
            fontsize=12, fontweight="bold"
        )

# Draw frequency reuse distance
x1 = 0
y1 = 0

x2 = math.sqrt(3) * R * (i + j/2)
y2 = 1.5 * R * j

ax.annotate(
    "", xy=(x2, y2), xytext=(x1, y1),
    arrowprops=dict(
        arrowstyle="<->", color="blue", linewidth=2
    )
)

ax.text(
    (x1+x2)/2, (y1+y2)/2 + 0.3*R,
    f"D = {D:.2f} km",
    color="red", fontsize=11, fontweight="bold",
    ha="center",
    bbox=dict(facecolor="white", edgecolor="none")
)

ax.set_xlim(-6*R, 6*R)
ax.set_ylim(-5.5*R, 5.5*R)

plt.title(
    f"Cellular Frequency Reuse Pattern (N = {N})",
    fontsize=15, fontweight="bold"
)

plt.tight_layout()
plt.show()

print("Cluster size N =", N)
print(f"Frequency reuse distance D = {D:.2f} km")
