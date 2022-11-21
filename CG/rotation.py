from PIL import Image,ImageDraw
from math import cos,sin,radians
img=Image.new('RGBA',(4000,2000),color=(255,255,255))
draw=ImageDraw.Draw(img)
x1,y1=[int(i) for i in input("Enter x1,y1: ").split(',')]
x2,y2=[int(i) for i in input("Enter x2,y2: ").split(',')]
start=0
end=0
print(f'Original Points are x1,y1: {x1},{y1} and x2,y2: {x2},{y2}')
draw.line([(start+x1,y1),(end+x2,y2)],width=5,fill=(255,0,0))
draw.line([(2000,0),(2000,2000)],width=5,fill=(255,0,0))
angle=int(input("enter angle of rotation in degrees: "))
angleInRadians=radians(angle)
X_new=x2 * cos(angleInRadians) - y2 * sin(angleInRadians)
Y_new=x2 * sin(angleInRadians) + y2 * cos(angleInRadians)
start=2000
end=2000
print(f'Rotated Points are x1,y1: {x1},{y1} and x2,y2: {X_new},{Y_new}')
draw.line([(start+x1,y1),(end+X_new,Y_new)],width=5,fill=(255,0,0))
img.show()
img.save('CG\\rotation.png')