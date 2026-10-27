import math
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

R = float(input("Enter cell radius (km): "))
i, j = 2, 1
N = i*i + i*j + j*j
D = R * math.sqrt(3 * N)
d = R * math.sqrt(3)                 # distance between two neighbour cells

colors = {"A": "red", "B": "deepskyblue", "C": "lightgreen", "D": "orange",
          "E": "violet", "F": "yellow", "G": "pink"}

fig, ax = plt.subplots(figsize=(6, 6))

def move(steps, angle):              # walk some cells in a direction
    a = math.radians(angle)
    return steps * d * math.cos(a), steps * d * math.sin(a)

def cell(x, y, letter, border):
    ax.add_patch(RegularPolygon((x, y), 6, radius=R, facecolor=colors[letter],
                                edgecolor=border, linewidth=3))
    ax.text(x, y, letter, ha="center", va="center", fontweight="bold")

def cluster(cx, cy, border):
    cell(cx, cy, "A", border)                    # A in the middle
    for k, letter in enumerate("BCDEFG"):        # 6 neighbours, every 60 degrees
        x, y = move(1, 60 * k)
        cell(cx + x, cy + y, letter, border)

cluster(0, 0, "black")
for border, angle in [("blue", 0), ("green", 60)]:
    x1, y1 = move(i, angle)                      # go i cells
    x2, y2 = move(j, angle + 60)                 # turn 60 degrees, go j cells
    cluster(x1 + x2, y1 + y2, border)
    if border == "blue":                         # draw D from A to A
        ax.plot([0, x1 + x2], [0, y1 + y2], color="red", linewidth=2)
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, f"D = {D:.2f} km", color="red",
                fontweight="bold", backgroundcolor="white", ha="center")

ax.set_aspect("equal")
ax.autoscale_view()
ax.axis("off")
plt.show()
