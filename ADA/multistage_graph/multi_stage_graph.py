from PIL import Image,ImageDraw,ImageFont

all_inputs=[
    {
'stage_count':5,
'nodes_count':[1,4,3,3,1],
'edge_count':[4,8,7,3,0],
'nodes_name':[1,2,3,4,5,6,7,8,9,10,11,12],
'edges':[
    [[1,2,3],[1,3,8],[1,4,4],[1,5,5]],
    [[2,6,4],[2,7,3],[3,6,4],[3,7,5],[4,7,3],[4,8,2],[5,7,2],[5,8,1]],
    [[6,9,3],[6,10,4],[7,9,4],[7,10,7],[7,11,6],[8,10,8],[8,11,7]],
    [[9,12,3],[10,12,1],[11,12,4]],
    ]
   },
   {
'stage_count':5,
'nodes_count':[1,2,3,2,1],
'edge_count':[2,5,6,2,0],
'nodes_name':[1,2,3,4,5,6,7,8,9],
'edges':[
    [[1,2,5],[1,3,2]],
    [[2,4,3],[2,6,3],[3,4,6],[3,5,5],[3,6,8]],
    [[4,7,1],[4,8,4],[5,7,6],[5,8,2],[6,7,6],[6,8,2]],
    [[7,9,7],[8,9,3]],
    ]},
    {
'stage_count':9,
'nodes_count':[1,2,4,3,3,2,4,3,1],
'edge_count':[2,5,8,7,4,6,12,3,0],
'nodes_name':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'],
'edges':[
    [['A','B',4],['A','C',3]],
    [['B','D',9],['B','E',8],['C','E',8],['C','F',4],['C','G',9]],
    [['D','H',5],['D','I',7],['E','H',2],['E','J',4],['F','I',6],['F','J',3],['G','I',7],['G','J',5]],
    [['H','K',11],['H','L',2],['I','K',3],['I','L',13],['I','M',8],['J','L',6],['J','M',7]],
    [['K','N',6],['L','N',7],['L','O',6],['M','O',8]],
    [['N','P',4],['N','Q',7],['N','R',3],['O','Q',6],['O','R',5],['O','S',2]],
    [['P','T',7],['P','U',8],['P','V',4],['Q','T',9],['Q','U',8],['Q','V',3],['R','T',6],['R','U',3],['R','V',11],['S','T',6],['S','U',7],['S','V',5]],
    [['T','W',6],['U','W',5],['V','W',8]]
    ]}
    ]
inputs=all_inputs[2]
SCALE_BY=0.5
NODE_SIZE=int(100*SCALE_BY)
X_DIFF=int(200*SCALE_BY)
Y_DIFF=int(200*SCALE_BY)
IMAGE_HEIGHT=max(inputs['nodes_count']) * Y_DIFF
NODE_COLOR=(255,255,255)
EDGE_COLOR=(255,0,0)
BG_COLOR=(0,0,0)
EDGE_WEIGHT_COLOR=(255,255,255)
NODE_NAME_COLOR=(255,0,0)
class Stage:
    def __init__(self,stage_name,nodes_count,edge_count):
        self.nodes_count=nodes_count
        self.stage_name=stage_name
        self.nodes=[]
        self.edges=[]
        self.edge_count=edge_count
    def add_node_in_this_stage(self,node):
        self.nodes.append(node)
    def add_edge_in_this_stage(self,edge):
        self.edges.append(edge)
    def __str__(self) -> str:
        return self.stage_name
class Edge:
    def __str__(self) -> str:
        return f"node1 {self.node1}, node2 {self.node2}"
    def __init__(self,name,node1,node2,weight,stage) -> None:
        self.name=name
        self.node1=node1
        self.node2=node2
        self.weight=weight
        self.stage=stage
        self.is_sol=False
    def get_color(self):
        return {'edge_color':(255,0,0),'weight_color':(255,255,255)}
        if self.node1.y_pos < self.node2.y_pos:
            return {'edge_color':(255,20,147),'weight_color':(255,105,180)}
        elif self.node1.y_pos > self.node2.y_pos:
            return {'edge_color':(255,255,0),'weight_color':(240,230,140)}
        else:
            return {'edge_color':(169,169,169),'weight_color':(220,220,220)}

    def get_draw_coordinates(self,start_x_pos,start_y_pos):
        return (start_x_pos+self.node1.x_pos,start_y_pos+self.node1.y_pos,start_x_pos+self.node2.x_pos,start_y_pos+self.node2.y_pos)
    def get_weight_coordinates(self,start_x_pos,start_y_pos):
        if self.node1.y_pos < self.node2.y_pos:
            return (start_x_pos+(self.node1.x_pos + self.node2.x_pos -NODE_SIZE//2 )/2,start_y_pos+(self.node1.y_pos + self.node2.y_pos -NODE_SIZE)/2)
        elif self.node1.y_pos > self.node2.y_pos:
            return (start_x_pos+(self.node1.x_pos + self.node2.x_pos -NODE_SIZE//2 )/2,start_y_pos+(self.node1.y_pos + self.node2.y_pos +NODE_SIZE//2)/2)
        else:
            return (start_x_pos+(self.node1.x_pos + self.node2.x_pos  )/2,start_y_pos+(self.node1.y_pos + self.node2.y_pos - NODE_SIZE//3)/2)
class Node:
    def __str__(self) -> str:
        return str(self.edges)
    def __init__(self,name,stage,x_pos,y_pos):
        self.name=str(name)
        self.edge_count=0
        self.edges=[]
        self.stage=stage
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.is_source=False
        self.is_destination=False
    def add_edge_in_this_node(self,edge):
        self.edge_count+=1
        self.edges.append(edge)
    def get_draw_coordinate(self,start_x_pos,start_y_pos):
        return (start_x_pos+self.x_pos-NODE_SIZE//2,start_y_pos+self.y_pos-NODE_SIZE//2,start_x_pos+self.x_pos+NODE_SIZE//2,start_y_pos+self.y_pos+NODE_SIZE//2)

class Solution:
    def __init__(self,solution_edges,solution_nodes,cost):
        self.solution_edges=solution_edges
        self.solution_nodes=solution_nodes
        self.cost=cost
stage_count=inputs['stage_count']
Stages=[]
for i in range(stage_count):
    if i==stage_count-1:
        node_count_in_this_stage=1
        edge_count_in_this_stage=0
    elif i==0:
        node_count_in_this_stage=1
        edge_count_in_this_stage=inputs['edge_count'][i]
    else:
        node_count_in_this_stage=inputs['nodes_count'][i]
        edge_count_in_this_stage=inputs['edge_count'][i]
    Stages.append(Stage(stage_name=str(i+1),nodes_count=node_count_in_this_stage,edge_count=edge_count_in_this_stage)) 
current_x_pos=100
current_y_pos=100
a=0
for l in range(len(Stages)):
    stage=Stages[l]
    current_x_pos+=X_DIFF
    current_y_pos=50
    if l==0 or l==len(Stages)-1:
        current_y_pos+=Y_DIFF
    for i in range(stage.nodes_count):
        current_y_pos+=Y_DIFF
        #TODO
        #_node_name=input(f"Enter name of {i+1} node of stage: {stage}" or i)
        _node_name=inputs['nodes_name'][a]
        a+=1
        node=Node(name=_node_name,stage=stage,x_pos=current_x_pos,y_pos=current_y_pos)
        if l==0:
            node.is_source=True
        elif l==len(Stages)-1:
            node.is_destination=True
        stage.add_node_in_this_stage(node)
edge_name=0
for j in range(stage_count):
    if j<stage_count-1:
        no_of_edges_in_this_stage=Stages[j].edge_count
        this_stage=Stages[j]
        next_stage=Stages[j+1]
        for i in range(no_of_edges_in_this_stage):
            edge_name+=1
            name=str(edge_name)
            __node1=str(inputs['edges'][j][i][0])
            __node2=str(inputs['edges'][j][i][1])
            #TODO
            # __node1=input(f"Enter name of starting node for {i+1} edge of stage {this_stage}")
            # __node2=input(f"Enter name of ending node for {i+1} edge of stage {this_stage}")
            # _weight=input(f"enter weight for {name} edge of stage {this_stage} :")
            _node1=[i for i in this_stage.nodes if i.name==__node1][0]
            _node2=[i for i in next_stage.nodes if i.name==__node2][0]
            _weight=inputs['edges'][j][i][2]
            edge=Edge(stage=this_stage,name=name,node1=_node1,node2=_node2,weight=_weight)
            this_stage.add_edge_in_this_stage(edge)
            _node1.add_edge_in_this_node(edge)
            
solution_images=[]
solutions=[]
def get_image(solutions,show_all=False):
    optimal_solutions=[i for i in solutions if i.cost==min(solutions,key=lambda x:x.cost).cost]
    other_solutions=[i for i in solutions if i not in optimal_solutions]
    X_SIZE=int(X_DIFF*3*len(Stages))
    
    Y_SIZE=int(IMAGE_HEIGHT*(len(solutions)+1 if show_all else len(optimal_solutions)+1))+IMAGE_HEIGHT
    img=Image.new("RGBA",(X_SIZE,Y_SIZE),"black")
    draw = ImageDraw.Draw(img)
    X_POS=0
    Y_POS=0
    for stage in Stages:
        for edge in stage.edges:
            draw.line(edge.get_draw_coordinates(X_POS,Y_POS),width= NODE_SIZE//20,fill= edge.get_color()['edge_color'])
            # draw.text(edge.get_weight_coordinates(X_POS,Y_POS), str(edge.weight), edge.get_color()['weight_color'] ,font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
        for node in stage.nodes:
            draw.ellipse(node.get_draw_coordinate(X_POS,Y_POS), fill=(255, 255, 255), outline=(0, 0, 0))
            draw.text((X_POS+node.x_pos - NODE_SIZE//5,Y_POS+node.y_pos - NODE_SIZE//4), node.name, (255, 0, 0),font=ImageFont.truetype("arial.ttf", NODE_SIZE//2))
    for stage in Stages:
        for edge in stage.edges:
            draw.text(edge.get_weight_coordinates(X_POS,Y_POS), str(edge.weight), edge.get_color()['weight_color'] ,font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
        
    draw.line((0,Y_POS+IMAGE_HEIGHT*1.5,X_SIZE,Y_POS+IMAGE_HEIGHT*1.5),width= NODE_SIZE//5,fill=(255,0,0))
    
    for i in range(len(optimal_solutions)):
        if i%2!=0:
            X_POS=X_SIZE//2
        else:
            X_POS=0
            Y_POS+=IMAGE_HEIGHT*1.5
        optimal=optimal_solutions[i]
        solution_edges=optimal.solution_edges
        draw.text((X_POS+ X_SIZE//5,Y_DIFF//1.5+Y_POS), str(f'Optimal Solution, Cost={optimal.cost}'), (255,255,255) ,font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
        for stage in Stages:
                for edge in stage.edges:
                    draw.line(edge.get_draw_coordinates(X_POS,Y_POS),width=NODE_SIZE//10 if edge in solution_edges else  NODE_SIZE//20,fill=(0,0,255)  if edge in solution_edges else edge.get_color()['edge_color'])
                    # draw.text(edge.get_weight_coordinates(X_POS,Y_POS), str(edge.weight), edge.get_color()['weight_color'] ,font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
                for node in stage.nodes:
                    draw.ellipse(node.get_draw_coordinate(X_POS,Y_POS), fill=(255, 255, 255), outline=(0, 0, 0))
                    draw.text((X_POS+node.x_pos - NODE_SIZE//5,Y_POS+node.y_pos - NODE_SIZE//4), node.name, (255, 0, 0),font=ImageFont.truetype("arial.ttf", NODE_SIZE//2))
        for stage in Stages:
            for edge in stage.edges:
                draw.text(edge.get_weight_coordinates(X_POS,Y_POS), str(edge.weight), edge.get_color()['weight_color'] ,font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
        
                # draw.text((X_POS+ node.x_pos-50 ,node.y_pos -100), node.name, (0, 0, 0),font=ImageFont.truetype("arial.ttf", 200))
    

    if show_all:
        
        draw.line((0,Y_POS+IMAGE_HEIGHT*1.5,X_SIZE,Y_POS+IMAGE_HEIGHT*1.5),width= NODE_SIZE//5,fill=(255,0,0))

        for i in range(len(other_solutions)):
            if i%2!=0:
                X_POS=X_SIZE//2
            else:
                X_POS=0
                Y_POS+=IMAGE_HEIGHT*1.5
            other=other_solutions[i]
            solution_edges=other.solution_edges
            draw.text((X_POS+ X_SIZE//5,Y_DIFF//1.5+Y_POS), str(f'Other Solution, Cost={other.cost}'), (255,255,255) ,font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
            for stage in Stages:
                    for edge in stage.edges:
                        draw.line(edge.get_draw_coordinates(X_POS,Y_POS),width=NODE_SIZE//10 if edge in solution_edges else  NODE_SIZE//20,fill=(0,0,255) if edge in solution_edges else edge.get_color()['edge_color'])
                        # draw.text(edge.get_weight_coordinates(X_POS,Y_POS), str(edge.weight), edge.get_color()['weight_color'],font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
                    for node in stage.nodes:
                        draw.ellipse(node.get_draw_coordinate(X_POS,Y_POS), fill=(255, 255, 255), outline=(0, 0, 0))
                        draw.text((X_POS+node.x_pos - NODE_SIZE//5,Y_POS+node.y_pos - NODE_SIZE//4), node.name, (255, 0, 0),font=ImageFont.truetype("arial.ttf", NODE_SIZE//2))
            for stage in Stages:
                for edge in stage.edges:
                    draw.text(edge.get_weight_coordinates(X_POS,Y_POS), str(edge.weight), edge.get_color()['weight_color'] ,font=ImageFont.truetype("arial.ttf", NODE_SIZE//3))
        
    return img
def solution_recur(stage,nodes,edges,cost):
    if stage==0:
        nodes=[Stages[0].nodes[0]]
        cost=0
        solution_recur(stage+1,nodes,edges,cost)
    elif stage==stage_count-1:
        for edge in nodes[-1].edges:
            edges.append(edge)
            cost+=edge.weight
            nodes.append(edge.node2)
        solutions.append(Solution(solution_edges=edges,cost=cost,solution_nodes=nodes))
        return
    else:
        for edge in nodes[-1].edges:
            if len(nodes)>stage:
                nodes=nodes[:stage]
            if len(edges)>stage:
                edges=edges[:stage-1]
            
            edges.append(edge)
            nodes.append(edge.node2)
            solution_recur(stage+1,nodes,edges,cost+edge.weight)
solution_recur(0,[],[],0)
print(len(solutions))
for solution in solutions:
    print('Cost= ',solution.cost,end=',')
    print(' Edges= ',end='')
    for i in solution.solution_edges:
        print(i.name,end=',')
    print(' Nodes= ',end='')
    for i in solution.solution_nodes:
        print(i.name,end=',')
    print()
print(len(solutions))
get_image(solutions,True).save('multistage_graph/graph.png')