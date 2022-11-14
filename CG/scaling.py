from PIL import Image,ImageDraw
img=Image.new('RGBA',(4000,2000),color=(255,255,255))
draw=ImageDraw.Draw(img)
x1,y1=[int(i) for i in input("Enter x1,y1: ").split(',')]
x2,y2=[int(i) for i in input("Enter x2,y2: ").split(',')]
start=0
end=0
print(f'Original Points are x1,y1: {x1},{y1} and x2,y2: {x2},{y2}')
draw.line([(start+x1,y1),(end+x2,y2)],width=5,fill=(255,0,0))
draw.line([(2000,0),(2000,2000)],width=5,fill=(255,0,0))
x,y=[int(i) for i in input("Enter Scaling factors x,y: ").split(',')]

x2*=x
y2*=y
start=2000
end=2000
print(f'scaled Points are x1,y1: {x1},{y1} and x2,y2: {x2},{y2}')
draw.line([(start+x1,y1),(end+x2,y2)],width=5,fill=(255,0,0))
img.show()
img.save('scaling.png')