
#Getting İnput
class Node:
  def __init__(self, id,adjaceny,color,parent,time):

    self.id = id
    self.adjaceny = adjaceny
    self.color=color
    self.parent=parent
    self.time=time

input_count=input().split()
nodes=[]


for i in range(0,int(input_count[0])):

    node_adj = input().split()

    adj_list = []
    for j in range(1,int(input_count[0])+1):
        if(int(node_adj[j - 1])>0):

            adj_list.append(j)
    nodes.append(Node(i+1,adj_list,"white",0,0))



oddCycle="false"
#check all the edges
def checkOddLengthCycle(node):
    global oddCycle
    for i in node.adjaceny:

        if(nodes[i-1].color=="gray" and (nodes[i-1].time+node.time)%2==0):
            oddCycle="true"


time=0
#search all nodes in a graph with the help of Depth First Search.
def DFS(node):

    global time
    time=time+1
    node.time=time
    node.color="gray"
    # now check the back edge with help of this function.If back edge has found, the found back edge node's time and current node's time's sum is even;
    # than the odd cycle found!
    checkOddLengthCycle(node)
    for i in node.adjaceny:
         if(nodes[i-1].color=="white"):
            nodes[i-1].parent=node
            DFS(nodes[i-1])

    node.color="black"
    time=time+1


for i in nodes:

    if(i.color=="white"):
        DFS(i)

print(oddCycle)

#in conclusion,searching all nodes and edges in a graph so big-Oh(E+V)
