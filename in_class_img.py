from PIL import Image

img = Image.open("beach.jpg")
#img.show()#original image

pixmap = img.load()

r,g,b = pixmap[100,100]

for i in range(img.size[0]):
    for j in range(img.size[1]):#(0,img.size[1],6)   this limits the filter to every pixel, shows lines
        #pixmap[i,j] = (255,255,255)
        r,g,b = pixmap[i,j]
        r += 255
        g += 0
        b += 0
        pixmap[i,j] = (b,g+b,b)
    
img.show()
img.save("beach_filter2.jpg")