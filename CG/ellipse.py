from PIL import Image,ImageDraw
img=Image.new('RGBA',(2000,2000),color=(255,255,255))
draw=ImageDraw.Draw(img)
def getDrawCords(x,y,x_width,y_width):
    return (x-int(x_width/2),y-int(y_width/2),x+int(x_width/2),y+int(y_width/2))
x,y=[int(i) for i in input("Enter center of ellipse x,y: ").split(',')]
x_width,y_width=[int(i) for i in input("Enter width of ellipse in both axes x,y ").split(',')]

draw.ellipse(getDrawCords(x,y,x_width,y_width), fill=(255,0,0), outline=(0, 0, 0))
img.show()