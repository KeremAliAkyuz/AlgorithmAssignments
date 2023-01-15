#For getting input,must blank line end of the file
#Creating Node
class Node:
  def __init__(self, id,name,adjaceny,idAdjaceny,path,totalRoad,isTraversed):

    self.id = id
    self.name=name
    self.adjaceny = adjaceny
    self.idAdjaceny=idAdjaceny
    self.path=path
    self.totalRoad=totalRoad
    self.isTraversed=isTraversed


input_count=input().split()
edges=[[0 for column in range(len(input_count))]for row in range(len(input_count))]#Store All edges as n*n matrix
nodes=[]#Store all nodes
#Getting input
for i in range(0,len(input_count)):
    adj_list = input().split()
    node_adj_name = []
    node_adj_id = []
    for j in range(0,len(adj_list)):
        if int(adj_list[j])>0:
            int(adj_list[j])
            edges[i][j]=int(adj_list[j])
            node_adj_name.append(input_count[j])
            node_adj_id.append(j)

    nodes.append(Node(i,input_count[i],node_adj_name,node_adj_id,"",0,False))



weigth=0
minTotalRoad=10000000
mainPath=""

#Main Function
def Airport(start,end,parentNode,totalEdge,path,parentWeigth):
    global minTotalRoad
    global mainPath
    global edges

    if totalEdge>4: #Flight can fly max 4 edge so if edge greater than 4 return

        return

    if start.id==end.id: #If start point equals finish point,road has completed so return
        weight = edges[start.id][parentNode.id] + parentWeigth #Weight equals parent node's weight + edge between parent node and current node

        path=path+end.name
        if(weight<minTotalRoad): #If current weight smaller than last smallest weight it is the smallest weight
            minTotalRoad=weight
            mainPath=path #So,path of the the smallest path changes

        return

    else:

        weight=edges[start.id][parentNode.id]+parentWeigth #Weight equals parent node's weight + edge between parent node and current node


    for i in start.idAdjaceny:#Travel all adjacent nodes
        Airport(nodes[i],end,start,totalEdge+1,path+start.name+" ",weight)#next nodes are adjacent nodes

#In worst case scenerio,All nodes adjacent to other nodes so every node has n-1 adjacent node.
#Traverse the graph till 4th edge so (big-Oh=n**4)

#Printing output
inputArr=[]
flag=True
while flag:

    inputs = input().split()

    if not inputs:
        flag=False
        break
    if(flag):
        inputNode1 = inputs[0]
        inputNode2 = inputs[1]
        for i in nodes:
            if (inputNode1 == i.name):
                nodeStart = i
            if (inputNode2 == i.name):
                nodeEnd = i

        Airport(nodeStart, nodeEnd, nodeStart, 0, "", 0)
        inputArr.append(mainPath)
        mainPath=""
        minTotalRoad=10000000

for i in inputArr:
    print(i)
