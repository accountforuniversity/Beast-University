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
# inputs={
# 'stage_count':4,
# 'nodes_count':[1,2,2,1],
# 'edge_count':[2,4,2,0],
# 'nodes_name':[3,6,7,8,9,10],
# 'edges':[
#     [[3,6,24],[3,7,5]],
#     [[6,9,3],[6,10,4],[7,9,4],[7,10,7]],
#     [[9,12,3],[10,12,1]],
#     ]
# }
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
#TODO
a=0
for l in range(len(Stages)):
    stage=Stages[l]
    current_x_pos+=X_DIFF
    current_y_pos=100
    if l==0 or l==len(Stages)-1:
        current_y_pos+=Y_DIFF
    for i in range(stage.nodes_count):
        # Y_DIFF=Y_SIZE/(stage.nodes_count+1)
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
        print(f"-----Stage {j+1} -----")
        no_of_edges_in_this_stage=Stages[j].edge_count
        this_stage=Stages[j]
        next_stage=Stages[j+1]
        for i in range(no_of_edges_in_this_stage):
            edge_name+=1
            name=str(edge_name)
            __node1=str(inputs['edges'][j][i][0])
            __node2=str(inputs['edges'][j][i][1])
            print(__node1,__node2)
            print([i.name for i in  this_stage.nodes])
            #TODO
            # __node1=input(f"Enter name of starting node for {i+1} edge of stage {this_stage}")
            # __node2=input(f"Enter name of ending node for {i+1} edge of stage {this_stage}")
            # _weight=input(f"enter weight for {name} edge of stage {this_stage} :")
            _node1=[i for i in this_stage.nodes if i.name==__node1][0]
            _node2=[i for i in next_stage.nodes if i.name==__node2][0]
            _weight=inputs['edges'][j][i][2]
            edge=Edge(stage=this_stage,name=name,node1=_node1,node2=_node2,weight=_weight)
            
            print(edge.name)
            this_stage.add_edge_in_this_stage(edge)
            _node1.add_edge_in_this_node(edge)






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
        draw.line(edge.get_draw_coordinates(),width=10,fill=(255,0,0))
        draw.text(edge.get_weight_coordinates(), str(edge.weight),(0, 0, 255) if edge.is_sol else (255,255,255) ,font=ImageFont.truetype("arial.ttf", 200))
    for node in stage.nodes:
        draw.ellipse(node.get_draw_coordinate(), fill=(255, 255, 255), outline=(0, 0, 0))
        draw.text((node.x_pos-50 ,node.y_pos -100), node.name, (0, 0, 0),font=ImageFont.truetype("arial.ttf", 200))
        

for i in range(len(Stages)):
    stage=Stages[i]
    for edge in stage.edges:
        pass

img.show()




class Solution:
    def __init__(self) -> None:
        self.solution_edges=[]
        self.solution_nodes=[Stages[0].nodes[0]]
        self.cost=0
        self.stage=Stages[0]
        
solutions=[]

# while 

# def a(stageNum):
#     solution=Solution()
#     if stageNum==stage_count-1:
#         return
#     a(stageNum+1)
# # for i in range(10):
# for i in range(10):
#     currently_at_node=Stages[0].nodes[0]
#     sol=Solution()
currently_at_node=Stages[0].nodes[0]
cost=0
solution=[]
def sol_recur(stage):
    if stage==stage_count-1:
        return
    for i in Stages:
        for j in i.nodes:
            for k in j.edges:
                return sol_recur(stage,)
        sol_recur(stage+1)
    
for i in range(10):
    currently_at_node=Stages[0].nodes[0]
    for j in range(len(Stages)):
        if  j<len(Stages)-1:
            stage=Stages[j]
            for k in range(currently_at_node.edge_count):


for i in range(len(Stages)):
    if i <len(Stages)-1:
        edge=currently_at_node.edges[0]
        cost+=edge.weight
        solution.append(edge)
        currently_at_node=edge.node2
solutions.append(solution)
o=solutions[0]
for i in o:
    print(i.name,end=',')

print('------------')

currently_at_node=Stages[0].nodes[0]
cost=0
solution=[]
for i in range(len(Stages)):
    if i <len(Stages)-1:
        edge=currently_at_node.edges[1]
        cost+=edge.weight
        solution.append(edge)
        currently_at_node=edge.node2
solutions.append(solution)
o=solutions[0]
for i in o:
    print(i.name,end=',')
# while True:
#     currently_at_node=Stages[0].nodes[0]
#     cost=0
#     for i in range(len(Stages)):
#         stage=Stages[i]
        
#         for k in range(stage.edge_count):
#             edge=stage.edges[k]
#             cost+=edge.weight
#             dest_node=edge.node2
#             for i in range(dest_node.edge_count):
                




#             node=stage.nodes[k]
#             node_edges=node.edges
#             for node in node_edges:
#                 print(node.name)
#     break
        


























# from PIL import Image,ImageDraw,ImageFont
# inputs={
# 'stage_count':5,
# 'nodes_count':[1,4,3,3,1],
# 'edge_count':[4,8,7,3,0],
# 'nodes_name':[1,2,3,4,5,6,7,8,9,10,11,12],
# 'edges':[
#     [[1,2,3],[1,3,8],[1,4,4],[1,5,5]],
#     [[2,6,4],[2,7,3],[3,6,4],[3,7,5],[4,7,3],[4,8,2],[5,7,2],[5,8,1]],
#     [[6,9,3],[6,10,4],[7,9,4],[7,10,7],[7,11,6],[8,10,8],[8,11,7]],
#     [[9,12,3],[10,12,1],[11,12,4]],
#     ]
# }
# X_DIFF=2000
# Y_DIFF=2000
# Y_SIZE=10000
# NODE_COLOR=(255,255,255)
# EDGE_COLOR=(255,0,0)
# img=Image.new("RGBA",(20000,10000),"black")
# draw = ImageDraw.Draw(img)
# class Stage:
#     def __init__(self,stage_name,nodes_count,edge_count):
#         self.nodes_count=nodes_count
#         self.stage_name=stage_name
#         self.nodes=[]
#         self.edges=[]
#         self.edge_count=edge_count
#     def add_node_in_this_stage(self,node):
#         self.nodes.append(node)
#     def add_edge_in_this_stage(self,edge):
#         self.edges.append(edge)
#     def __str__(self) -> str:
#         return self.stage_name
# class Edge:
#     def __init__(self,name,node1,node2,weight,stage) -> None:
#         self.name=name
#         self.node1=node1
#         self.node2=node2
#         self.weight=weight
#         self.stage=stage
#         self.is_sol=False
#     def get_draw_coordinates(self):
#         print(self.node1.x_pos,self.node1.y_pos,self.node2.x_pos,self.node2.y_pos)
#         return (self.node1.x_pos,self.node1.y_pos,self.node2.x_pos,self.node2.y_pos)
#     def get_weight_coordinates(self):
#         if self.node1.y_pos < self.node2.y_pos:
#             return ((self.node1.x_pos + self.node2.x_pos -600 )/2,(self.node1.y_pos + self.node2.y_pos -300)/2)
#         elif self.node1.y_pos > self.node2.y_pos:
#             return ((self.node1.x_pos + self.node2.x_pos -600 )/2,(self.node1.y_pos + self.node2.y_pos +300)/2)
#         else:
            
#             return ((self.node1.x_pos + self.node2.x_pos  +600)/2,(self.node1.y_pos + self.node2.y_pos)/2)
# class Node:
#     def __init__(self,name,stage,x_pos,y_pos,edge_count):
#         self.name=str(name)
#         self.edge_count=edge_count
#         self.edges=[]
#         self.stage=stage
#         self.x_pos=x_pos
#         self.y_pos=y_pos
#         self.is_source=False
#         self.is_destination=False
#     def add_edge_in_this_stage(self,edge):
#         self.edges.append(edge)
#     def get_draw_coordinate(self):
#         return (self.x_pos-300,self.y_pos-300,self.x_pos+300,self.y_pos+300)

# #TODO
# # stage_count=int(input('Enter no of stages: ') or 2)
# stage_count=inputs['stage_count']
# Stages=[]
# for i in range(stage_count):
    
#     if i==stage_count-1:
#         node_count_in_this_stage=1
#         edge_count_in_this_stage=0
#     elif i==0:
#         node_count_in_this_stage=1
#         # edge_count_in_this_stage=int(input(f'Enter no of edges in Stage {i+1} going to next Stage: ') or 2)
#         edge_count_in_this_stage=inputs['edge_count'][i]
#     else:
#         #TODO
#         # node_count_in_this_stage=int(input(f'Enter no of nodes in Stage {i+1}: ') or 2)
#         # edge_count_in_this_stage=int(input(f'Enter no of edges in Stage {i+1} going to next Stage: ') or 2)
#         node_count_in_this_stage=inputs['nodes_count'][i]
#         edge_count_in_this_stage=inputs['edge_count'][i]
#     Stages.append(Stage(stage_name=str(i+1),nodes_count=node_count_in_this_stage,edge_count=edge_count_in_this_stage)) 
# current_x_pos=100
# current_y_pos=100
# #TODO
# a=0
# for l in range(len(Stages)):
#     stage=Stages[l]
#     current_x_pos+=X_DIFF
#     current_y_pos=100

#     if l==0 or l==len(Stages)-1:
#         current_y_pos+=Y_DIFF
#     for i in range(stage.nodes_count):
#         # Y_DIFF=Y_SIZE/(stage.nodes_count+1)
#         current_y_pos+=Y_DIFF
#         #TODO
#         #_node_name=input(f"Enter name of {i+1} node of stage: {stage}" or i)
#         _node_name=inputs['nodes_name'][a]
#         a+=1
#         node=Node(name=_node_name,stage=stage,x_pos=current_x_pos,y_pos=current_y_pos)
#         if l==0:
#             node.is_source=True
#         elif l==len(Stages)-1:
#             node.is_destination=True
#         stage.add_node_in_this_stage(node)
# for j in range(stage_count):
#     if j<stage_count-1:
#         print(f"-----Stage {j+1} -----")
#         no_of_edges_in_this_stage=Stages[j].edge_count
#         this_stage=Stages[j]
#         next_stage=Stages[j+1]
#         for i in range(no_of_edges_in_this_stage):
#             name=str(i+1)
#             __node1=str(inputs['edges'][j][i][0])
#             __node2=str(inputs['edges'][j][i][1])
#             print(__node1,__node2)
#             print([i.name for i in  this_stage.nodes])
#             #TODO
#             # __node1=input(f"Enter name of starting node for {i+1} edge of stage {this_stage}")
#             # __node2=input(f"Enter name of ending node for {i+1} edge of stage {this_stage}")
#             # _weight=input(f"enter weight for {name} edge of stage {this_stage} :")
#             _node1=[i for i in this_stage.nodes if i.name==__node1][0]
#             _node2=[i for i in next_stage.nodes if i.name==__node2][0]
#             _weight=inputs['edges'][j][i][2]
#             edge=Edge(stage=this_stage,name=name,node1=_node1,node2=_node2,weight=_weight)
#             this_stage.add_edge_in_this_stage(edge)
# # for stage in Stages:
#     # for i in range(stage.edge_count):
#     #     name=str(i+1)
#     #     __node1=input(f"Enter name of starting node for {i+1} edge")
#     #     __node2=input(f"Enter name of ending node for {i+1} edge")
#     #     _weight=input(f"enter weight for {name} edge of stage: {stage}")
#     #     _node1=[i for i in stage.nodes if i.name==__node1][0]
#     #     _node2=[i for i in stage.nodes if i.name==__node2][0]
#     #     edge=Edge(stage=stage,name=name,node1=_node1,node2=_node2,weight=_weight)
#     #     stage.add_edge_in_this_stage(edge)


# # NO_OF_EDGES=int(input("Enter total No of edges: "))
# # for i in range(NO_OF_EDGES):
# #     name=str(i+1)
# #     _node1=input(f"Enter name of starting node for {i+1} edge")
# #     _node2=input(f"Enter name of ending node for {i+1} edge")



# for stage in Stages:
#     for edge in stage.edges:
#         draw.line(edge.get_draw_coordinates(),width=10,fill=(255,0,0))
#         draw.text(edge.get_weight_coordinates(), str(edge.weight),(0, 0, 255) if edge.is_sol else (255,255,255) ,font=ImageFont.truetype("arial.ttf", 200))
#     for node in stage.nodes:
#         draw.ellipse(node.get_draw_coordinate(), fill=(255, 255, 255), outline=(0, 0, 0))
#         draw.text((node.x_pos-50 ,node.y_pos -100), node.name, (0, 0, 0),font=ImageFont.truetype("arial.ttf", 200))
        

# for i in range(len(Stages)):
#     stage=Stages[i]
#     for edge in stage.edges:
#         pass
# img.show()