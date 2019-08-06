import itchat
import math
import PIL.Image as Image
import os

itchat.auto_login()
friends = itchat.get_friends(update=True)
num = 0

if not os.path.exists("image"):
    os.mkdir("image")
for friend  in friends:
    img = itchat.get_head_img(userName=friend["UserName"])
    fileImage = open('image' + "/" + str(num) + ".jpg", 'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

all_image = os.listdir('image')
each_size = int(math.sqrt(float(640*640)/len(all_image)))
lines = int(640/each_size)
image = Image.new('RGBA', (640, 640))
x = 0
y = 0
for i in range(0, len(all_image)):
    img = Image.open('image' + "/" + str(i) + ".jpg")
    img = img.reszie((each_size, each_size), Image.ANTIALIAS)
    image.paste(img, (x * each_size, y * each_size))
    x += 1
    if x == lines:
        x = 0
        y += 1
image.save('image' + "/" + "all.jpg")
itchat.send_image('image' + "/" + "all.jpg", 'filehelper')
