from PIL import Image

img = Image.open("beach.jpg")
# reflect: think a,b = b,a
pixmap = img.load()

 #pixmap[i,j] = pixmap[img.size[0]-1-i,j] = pixmap[img.size[0]-1-i,j]'reflects half of the image'

#new_img = Image.new("RGB", img.size)
#new_map = new_img.load()
#
#from random import randint

#for i in range(img.size[0]):
#    for j in range(img.size[1]):
#        #new_map[i,j] = pixmap[i%(img.size[0]//2),j] 'half and half copies'
#        #new_map[i,j] = pixmap[randint(0,img.size[0]-1),randint(0,img.size[1]-1)] 'scattered pixels'
#        n = randint(0,9)
#        if n> 7:
#            pixmap[i,j] = (0,0,0) #img.show() 'shows black pixels scattered'

            
def mirror():
    for i in range(img.size[0]//2):
        for j in range(img.size[1]):
            pixmap[i,j], pixmap[img.size[0]-1-i,j] = pixmap[img.size[0]-1-i,j], pixmap[i,j]
    img.show()
    
def lt_rt_reflect():
    for i in range(img.size[0]//2):
        for j in range(img.size[1]):
            pixmap[img.size[0]-1-i,j] = pixmap[i,j]
    img.show()
    
def rt_lt_reflect():
    #reflects the right side to the left
    for i in range(img.size[0]//2):
        for j in range(img.size[1]):
            pixmap[i,j] = pixmap[img.size[0]-1-i,j]
    img.show()
    
    
def main():
    #mirror()
    lt_rt_reflect()
    #rt_lt_reflect()
    
if __name__ == "__main__":
    main()