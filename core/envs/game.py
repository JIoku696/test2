import numpy as np
import random
from PIL import Image, ImageDraw

class set_rand_pict(self.x, self.k, self.width, self.height, self.draw, self.image):
    for i in range(self.width):
        for j in range(self.height):
            a = self.x
            b = self.x
            c = self.x
            self.draw.point((i,j),(a, b, c))
    self.image.save("temp_" + str(self.k) + ".jpg", "JPEG")

class brightness_down(self.k, self.pix, self.draw, self.image):
    self.k += 1
    for i in range(self.width):
        for j in range(self.height):
            a = pix[i, j][0] - 1
            b = pix[i, j][0] - 1
            c = pix[i, j][0] - 1
            self.draw.point((i,j),(a, b, c))
    self.image.save("temp_" + str(self.k) + ".jpg", "JPEG")
    return(self.k)

class brightness_up(self.k, self.pix, self.draw, self.image):
    self.k += 1
    for i in range(self.width):
        for j in range(self.height):
            a = self.pix[i, j][0] + 1
            b = self.pix[i, j][0] + 1
            c = self.pix[i, j][0] + 1
            self.draw.point((i,j),(a, b, c))
    self.image.save("temp_" + str(self.k) + ".jpg", "JPEG")
    return(self.k)

class score(j):
    if self.j > 128:
        s = self.j - 128
        return(s)
    else:
        s = 128 - self.j
        return(s)

class down(self.x):
    self.x -= 1
    print('down ', score(self.x))
    return(self.x)

class up(self.x):
    self.x += 1
    print('up ', score(self.x))
    return(self.x)



class game():
    self.image = Image.open("temp.jpg")
    self.draw = ImageDraw.Draw(image)
    self.width = image.width
    self.height = image.height
    self.x = np.random.randint(255)
    self.k = 0
    set_rand_pict(self.x, self.k, self.width, self.height, self.draw, self.image)
	self.pix = image.load()
    #print(x)
    while self.x != 128:
        if self.x < 128:
            self.x = up(self.x)
            self.k = brightness_up(self.k, self.pix, self.draw, self.image)
        else:
            self.x = down(self.x)
            self.k = brightness_down(self.k, self.pix, self.draw, self.image)
    print('x = ', self.x)
    del self.draw