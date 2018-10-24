from PIL import Image
from random import randint

def snow(width,height):
    img = Image.new("RGB",(width,height))
    pixelmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            n = randint(0,1)
            if n:
                pixelmap[i,j] = (255,255,255)
    img.show()
    
def multi_color_snow(width,height,bgcolor):
    img = Image.new("RGB",(width,height))
    pixelmap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            pixelmap[i,j] = (r,g,b)
    img.show()
    
def smile():
    img = Image.new("RGB",(50,50),(255,255,0))
    pixelmap = img.load()
    pixelmap[15,15] = (0,0,0)
    pixelmap[30,15] = (0,0,0)
    pixelmap[32,30] = (0,0,0)
    pixelmap[33,30] = (0,0,0)
    pixelmap[34,30] = (0,0,0)
    pixelmap[35,30] = (0,0,0)
    img.show()
    img.save("my_image.jpg")
    
if __name__ == "__main__":
    #snow(500,500)
    #multi_color_snow(500,500,(0,0,255))
    smile()
#create a new 300*200 black image
#img = Image.new("RGB",(600,400),(255,0,0))
#pixelmap = img.load()
#pixelmap[100,100] = (0,0,0)
#img.show()
#print(pixelmap[0,0])

#pixelmap[i,j]
