from PIL import Image, ImageDraw
import random

SIZE = 128
img = Image.new("RGBA", (SIZE, SIZE), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# GitHub-style green scale (matches styles/colors.scss)
EMPTY = (235, 237, 240)
GREENS = [
	(155, 233, 168),  # work0
	(64, 196, 99),    # work25
	(48, 161, 78),    # work50
	(33, 110, 57),    # work75
]

# Grid layout: 7 rows x 11 cols of rounded squares with padding
cols, rows = 11, 7
margin = 10
gap = 3
avail_w = SIZE - 2 * margin
avail_h = SIZE - 2 * margin
cell_w = (avail_w - (cols - 1) * gap) / cols
cell_h = (avail_h - (rows - 1) * gap) / rows
cell = min(cell_w, cell_h)
radius = max(1, int(cell * 0.28))

# Center the grid
grid_w = cols * cell + (cols - 1) * gap
grid_h = rows * cell + (rows - 1) * gap
start_x = (SIZE - grid_w) / 2
start_y = (SIZE - grid_h) / 2

random.seed(7)

# Weighted intensity pattern: some empty, more low, fewer high, with a
# diagonal ramp so the logo reads as "activity increasing over time".
for c in range(cols):
	for r in range(rows):
		ramp = c / (cols - 1)
		roll = random.random()
		if roll < 0.18 - 0.12 * ramp:
			color = EMPTY
		else:
			level = min(3, int(random.random() * 3 * (0.4 + 0.9 * ramp)))
			color = GREENS[level]
		x0 = start_x + c * (cell + gap)
		y0 = start_y + r * (cell + gap)
		draw.rounded_rectangle(
			[x0, y0, x0 + cell, y0 + cell],
			radius=radius,
			fill=color,
		)

img.save("img/logo.png")
print("saved img/logo.png", img.size)
