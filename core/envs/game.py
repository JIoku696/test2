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
    def __init__(self, args, env_ind=0):
        super(AtariEnv, self).__init__(args, env_ind)
    
        self.env = gym.make(self.game)
        self.env.seed(self.seed)    # NOTE: so each env would be different

        # action space setup
        self.actions     = range(self.action_dim)
        self.logger.warning("Action Space: %s", self.actions)
        # state space setup
        self.hei_state = args.hei_state
        self.wid_state = args.wid_state
        self.preprocess_mode = args.preprocess_mode if not None else 0 # 0(crop&resize) | 1(rgb2gray) | 2(rgb2y)

    def _preprocessState(self, state):
        if self.preprocess_mode == 3 or self.preprocess_mode == 2 or self.preprocess_mode == 1 or self.preprocess_mode == 0:	
            pass
        return state.reshape(self.hei_state * self.wid_state)
	
    __init__(0, 0, 0)	
	
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
