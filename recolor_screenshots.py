import os
from PIL import Image
import numpy as np

# Screenshots that show the blue contribution graph / blue UI accents.
targets = [
	"contributionGraph.png",
	"timeWindow.png",
	"timeRange.png",
	"hoverTimeRange.png",
	"multipleUsers.png",
	"clickDay.png",
	"dayWindow.png",
	"chooseWidget.png",
	"clickWidget.png",
	"configureWidget.png",
]

img_dir = "img"
backup_dir = os.path.join(img_dir, "blue_backup")
os.makedirs(backup_dir, exist_ok=True)

# Hue window (PIL HSV, 0-255) covering ADO blue through blue-purple.
H_LO, H_HI = 135, 200
S_MIN = 22               # ignore near-gray/white so text & background stay
GREEN_H = 97             # ~137 degrees, GitHub-style green

for name in targets:
	src = os.path.join(img_dir, name)
	if not os.path.exists(src):
		print("skip (missing):", name)
		continue

	# Back up the original once.
	bak = os.path.join(backup_dir, name)
	if not os.path.exists(bak):
		Image.open(src).save(bak)

	im = Image.open(src).convert("RGB")
	hsv = np.array(im.convert("HSV")).astype(np.int16)
	h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]

	mask = (h >= H_LO) & (h <= H_HI) & (s >= S_MIN)
	hsv[..., 0] = np.where(mask, GREEN_H, h)

	out = Image.fromarray(hsv.astype(np.uint8), "HSV").convert("RGB")
	out.save(src)
	print(f"{name}: recolored {int(mask.sum())} px")

print("done")
