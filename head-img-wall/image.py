import math
from PIL import Image
import os

all_image = os.listdir('D://images')
each_size = int(math.sqrt(float(640*640)/len(all_image)))
lines = int(640/each_size)
image = Image.new('RGB', (640, 640))
x = 0
y = 0
for i in range(0, len(all_image)):
    img = Image.open('D://images' + "/" + all_image[i])
    img = img.resize((each_size, each_size), Image.ANTIALIAS)
    image.paste(img, (x * each_size, y * each_size))
    x += 1
    if x == lines:
        x = 0
        y += 1
image.save('D://images' + "/" + "all.jpg")