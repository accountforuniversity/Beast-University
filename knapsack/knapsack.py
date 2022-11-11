from random import randint

class Object():
    def __init__(self,name,profit,weight):
        self.profit=profit
        self.name=name
        self.weight=weight
    def getProfitPerUnitweight(self):
        return self.profit/self.weight
noOfObjects=int(input("How many type of objects are there? ")or randint(1, 100))
capacity=int(input("Capacity of knapsack: ") or randint(50, 1000))
print(f'Capacity is: {capacity}')
objects=[]
for i in range(noOfObjects):
    name=input(f"Enter name of {i+1} object: ") or f"P{i+1}"
    profit=int(input(f"Profit of {name} object: ")or randint(1, 100)) 
    weight=int(input(f"Weight of {name} object: ")or randint(1, 100)) 
    objects.append(Object(name=name,weight=weight,profit=profit))
    
print("Objects are :-")
for i in objects:
    print(f"Name: {i.name}, Profit: {i.profit}, Weight: {i.weight}")

objects.sort(key=lambda x:x.getProfitPerUnitweight(),reverse=True)
sack=[]
profit=0
current_weight=0
for object in objects:
    if(capacity>current_weight):
        if capacity>=current_weight+object.weight:
            current_weight= current_weight+object.weight
            sack.append(f"1 * {object.name}")
            profit+=object.profit
        
        elif capacity-current_weight<=object.weight:
            diff=capacity-current_weight
            current_weight= current_weight+ diff *  object.weight
            sack.append(f"{diff / object.weight} * {object.name}")
            profit+= diff/object.weight * object.profit
        else:
            break


print(f"Optimal Solution: {sack}")
print(f"Max Profit: {profit}")

