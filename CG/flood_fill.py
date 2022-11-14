from PIL import Image,ImageDraw
img=Image.new('RGBA',(10,10),color=(255,0,0))
draw=ImageDraw.Draw(img)
x1,y1=[int(i) for i in input("Enter starting point to fill color x1,y1: ").split(',')]
x2,y2=[int(i) for i in input("Enter ending point to fill color x2,y2: ").split(',')]
print('Default color is (255,0,0) in RGB')
color_to_fill=tuple([int(i) for i in input("Enter color to fill in RBG separated by ','").split(',')])
rgb_im = img.convert('RGB')
def floodFill( x, y,x1,y1,x2,y2 , color_to_fill):
    if rgb_im.getpixel((x, y))==color_to_fill:
        return
    print(x,y)
    if (x >=x1 and x <=x2  and y>=y1 and y<=y2):
        if rgb_im.getpixel((x, y))!=color_to_fill:
            draw.point((x,y),fill=color_to_fill)
            floodFill( x-1, y,x1,y1,x2,y2 , color_to_fill)
            floodFill( x+1, y,x1,y1,x2,y2 ,  color_to_fill)
            floodFill( x, y-1,x1,y1,x2,y2 ,  color_to_fill)
            floodFill( x, y+1,x1,y1,x2,y2 ,  color_to_fill)
            return
    else:
        return
    return

floodFill(3,3,x1,y1,x2,y2,(255,255,0))
img.show()