


from PIL import Image,ImageDraw,ImageFont
X_DIFF=1000
Y_DIFF=1000
Y_SIZE=10000
img=Image.new("RGBA",(10000,10000),"black")
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
    def __init__(self,name,node1,node2,weight,stage) -> None:
        self.name=name
        self.node1=node1
        self.node2=node2
        self.weight=weight
        self.stage=stage
    def get_draw_coordinates(self):
        print(self.node1.x_pos,self.node1.y_pos,self.node2.x_pos,self.node2.y_pos)
        return (self.node1.x_pos,self.node1.y_pos,self.node2.x_pos,self.node2.y_pos)
class Node:
    def __init__(self,name,stage,x_pos,y_pos):
        self.name=str(name)
        self.stage=stage
        self.x_pos=x_pos
        self.y_pos=y_pos
    def get_draw_coordinate(self):
        return (self.x_pos-200,self.y_pos-200,self.x_pos+200,self.y_pos+200)


stage_count=int(input('Enter no of stages: ') or 2)
Stages=[]
for i in range(stage_count):
    if i==stage_count-1:
        node_count_in_this_stage=1
        edge_count_in_this_stage=0
    else:
        node_count_in_this_stage=int(input(f'Enter no of nodes in Stage {i+1}: ') or 2)
        edge_count_in_this_stage=int(input(f'Enter no of edges in Stage {i+1} going to next Stage: ') or 2)
    Stages.append(Stage(stage_name=str(i+1),nodes_count=node_count_in_this_stage,edge_count=edge_count_in_this_stage)) 
current_x_pos=100
current_y_pos=100
for stage in Stages:
    current_x_pos+=X_DIFF
    current_y_pos=100
    for i in range(stage.nodes_count):
        Y_DIFF=Y_SIZE/(stage.nodes_count+1)
        current_y_pos+=Y_DIFF
        _node_name=input(f"Enter name of {i+1} node of stage: {stage}" or i)
        node=Node(name=_node_name,stage=stage,x_pos=current_x_pos,y_pos=current_y_pos)
        stage.add_node_in_this_stage(node)
for j in range(stage_count):
    if j<stage_count-1:
        print(f"-----Stage {j+1} -----")
        no_of_edges_in_this_stage=Stages[j].edge_count
        this_stage=Stages[j]
        next_stage=Stages[j+1]
        for i in range(no_of_edges_in_this_stage):
            name=str(i+1)
            __node1=input(f"Enter name of starting node for {i+1} edge of stage {this_stage}")
            __node2=input(f"Enter name of ending node for {i+1} edge of stage {this_stage}")
            _weight=input(f"enter weight for {name} edge of stage {this_stage} :")
            _node1=[i for i in this_stage.nodes if i.name==__node1][0]
            _node2=[i for i in next_stage.nodes if i.name==__node2][0]
            edge=Edge(stage=this_stage,name=name,node1=_node1,node2=_node2,weight=_weight)
            this_stage.add_edge_in_this_stage(edge)
# for stage in Stages:
    # for i in range(stage.edge_count):
    #     name=str(i+1)
    #     __node1=input(f"Enter name of starting node for {i+1} edge")
    #     __node2=input(f"Enter name of ending node for {i+1} edge")
    #     _weight=input(f"enter weight for {name} edge of stage: {stage}")
    #     _node1=[i for i in stage.nodes if i.name==__node1][0]
    #     _node2=[i for i in stage.nodes if i.name==__node2][0]
    #     edge=Edge(stage=stage,name=name,node1=_node1,node2=_node2,weight=_weight)
    #     stage.add_edge_in_this_stage(edge)


# NO_OF_EDGES=int(input("Enter total No of edges: "))
# for i in range(NO_OF_EDGES):
#     name=str(i+1)
#     _node1=input(f"Enter name of starting node for {i+1} edge")
#     _node2=input(f"Enter name of ending node for {i+1} edge")



for stage in Stages:
    for edge in stage.edges:
        draw.line(edge.get_draw_coordinates(),width=40,fill=(255,0,0))
    for node in stage.nodes:
        draw.ellipse(node.get_draw_coordinate(), fill=(255, 255, 255), outline=(0, 0, 0))
        draw.text((node.x_pos,node.y_pos), node.name, (0, 0, 0),font=ImageFont.truetype("arial.ttf", 100))


img.show()