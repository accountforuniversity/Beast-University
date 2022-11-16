from PIL import Image,ImageDraw,ImageFont
inputs={
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
}
X_DIFF=2000
Y_DIFF=2000
Y_SIZE=10000
NODE_COLOR=(255,255,255)
EDGE_COLOR=(255,0,0)
img=Image.new("RGBA",(20000,10000),"black")
draw = ImageDraw.Draw(img)
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
    def get_draw_coordinates(self):
        print(self.node1.x_pos,self.node1.y_pos,self.node2.x_pos,self.node2.y_pos)
        return (self.node1.x_pos,self.node1.y_pos,self.node2.x_pos,self.node2.y_pos)
    def get_weight_coordinates(self):
        if self.node1.y_pos < self.node2.y_pos:
            return ((self.node1.x_pos + self.node2.x_pos -600 )/2,(self.node1.y_pos + self.node2.y_pos -300)/2)
        elif self.node1.y_pos > self.node2.y_pos:
            return ((self.node1.x_pos + self.node2.x_pos -600 )/2,(self.node1.y_pos + self.node2.y_pos +300)/2)
        else:
            
            return ((self.node1.x_pos + self.node2.x_pos  +600)/2,(self.node1.y_pos + self.node2.y_pos)/2)
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
    def get_draw_coordinate(self):
        return (self.x_pos-300,self.y_pos-300,self.x_pos+300,self.y_pos+300)

class Solution:
    def __init__(self,solution_edges,solution_nodes,cost):
        self.solution_edges=solution_edges
        self.solution_nodes=solution_nodes
        self.cost=cost
        self.stage=Stages[0]
        
#TODO
# stage_count=int(input('Enter no of stages: ') or 2)
stage_count=inputs['stage_count']
Stages=[]
for i in range(stage_count):
    
    if i==stage_count-1:
        node_count_in_this_stage=1
        edge_count_in_this_stage=0
    elif i==0:
        node_count_in_this_stage=1
        # edge_count_in_this_stage=int(input(f'Enter no of edges in Stage {i+1} going to next Stage: ') or 2)
        edge_count_in_this_stage=inputs['edge_count'][i]
    else:
        #TODO
        # node_count_in_this_stage=int(input(f'Enter no of nodes in Stage {i+1}: ') or 2)
        # edge_count_in_this_stage=int(input(f'Enter no of edges in Stage {i+1} going to next Stage: ') or 2)
        node_count_in_this_stage=inputs['nodes_count'][i]
        edge_count_in_this_stage=inputs['edge_count'][i]
    Stages.append(Stage(stage_name=str(i+1),nodes_count=node_count_in_this_stage,edge_count=edge_count_in_this_stage)) 
current_x_pos=100
current_y_pos=100
a=0
for l in range(len(Stages)):
    stage=Stages[l]
    current_x_pos+=X_DIFF
    current_y_pos=100
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
            

solutions=[]
def show_image():
    for stage in Stages:
        for edge in stage.edges:
            draw.line(edge.get_draw_coordinates(),width=10,fill=(255,0,0))
            draw.text(edge.get_weight_coordinates(), str(edge.weight),(0, 0, 255) if edge.is_sol else (255,255,255) ,font=ImageFont.truetype("arial.ttf", 200))
        for node in stage.nodes:
            draw.ellipse(node.get_draw_coordinate(), fill=(255, 255, 255), outline=(0, 0, 0))
            draw.text((node.x_pos-50 ,node.y_pos -100), node.name, (0, 0, 0),font=ImageFont.truetype("arial.ttf", 200))
    img.show()
show_image()
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
for solution in solutions:
    print('Cost= ',solution.cost,end=',')
    print('Edges= ',end='')
    for i in solution.solution_edges:
        print(i.name,end=',')
    print('Nodes= ',end='')
    for i in solution.solution_nodes:
        print(i.name,end=',')
    print()

for i in solutions[0].solution_edges:
        i.is_sol=True

show_image()