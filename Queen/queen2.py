from itertools import permutations
from PIL import Image,ImageDraw
from pathlib import Path
from multiprocessing import Pool
n=5
def baseSolution(n):
    row=[]
    for i in range(n):
        col=''
        for j in range(n):
            if i==j:
                col+='Q'
            else:
                col+='.'
        row.append(col)
    return row
def getVerboseSolutions(baseSol=baseSolution(n)):
    # return [list(i) for i in permutations(baseSol)]
    return permutations(baseSol)



def emptyBox(num=n):
    box={}
    for row in range(n):
        for col in range(n):
            box.update({f'{row}[{col}]':True})
    return box

def printChess(box):
    for row in range(n):
        for col in range(n):
            print(f"{row}[{col}]:{box[f'{row}[{col}]']}  ",end=' ')
        print()
def getMainSolution(verboseSolution=getVerboseSolutions()):
    # pool=Pool()
    
    # l=pool.map(checkThisSol,list(verboseSolution))
    mainSolutions=[]
    # checkThisSol(verboseSolution[6])
    a=0
    from math import factorial
    total=factorial(n)
    for i in verboseSolution:
        a=a+1
        print(f'{a} out of {total}')
        
        # pool.map(checkThisSol,i)

        if checkThisSol(list(i),emptyBox()):
            mainSolutions.append(i)
    return mainSolutions



def checkThisSol(solution,chessbox=emptyBox()):
    chessbox=emptyBox()
    result=True
    for row in range(n):
        col=solution[row].index('Q')
        # print(row,col)
        #print(f'{row},{col}')
        if chessbox[f'{row}[{col}]']:
            chessbox[f'{row}[{col}]']=False
            for i in range(n):
                if row-i>=0 and col-i>=0:chessbox[f'{row-i}[{col-i}]']=False
                if row+i<n and col-i>=0:chessbox[f'{row+i}[{col-i}]']=False
                if row-i>=0 and col+i<n:chessbox[f'{row-i}[{col+i}]']=False
                if row+i<n and col+i<n:chessbox[f'{row+i}[{col+i}]']=False
            for i in range(n):
                chessbox[f'{row}[{i}]']=False
                chessbox[f'{i}[{col}]']=False
            
        else:
            result= False
    return result






def showImage(solution):
    if not solution:
        print('No Solution')
        return
    n=len(solution[0][0])
    solutions=solution
    cell_size=50
    cell_border=2

    height=n*cell_size*len(solutions)+len(solutions)*cell_size
    img=Image.new("RGBA",
    (n*cell_size,height),"black")
    draw=ImageDraw.Draw(img)
    a=0
    for sol in solutions:
        l=a*n+a
        a=a+1
    
        for i in range(n):
            row=sol[i]
            for j in range(n):
                if row[j]=='.':
                    fill=(40,40,40)
                else:
                    fill=(220,235,113)
                draw.rectangle((( i * cell_size + cell_border,( l+j) * cell_size + cell_border),
                        (  (i + 1) * cell_size - cell_border,( l+j + 1) * cell_size - cell_border)),
                            fill=fill)
    
    # img.save(Path(f'/queen_solutions/{n}.png'))
    img.save(f'Queen/queen_solutions/{n} Queens.png')
    img.show()


n=int(input("Enter n: "))
showImage(getMainSolution(getVerboseSolutions(baseSolution(n))))

