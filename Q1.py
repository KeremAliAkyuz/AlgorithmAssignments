#Getting İnput
input_count=input().split()
tasks=[]

for i in range(0,int(input_count[0])):
    task_dict={}
    task_prop = input().split()
    task_dict["taskId"] = int(task_prop[0])
    task_dict["deadline"] = int(task_prop[1])
    task_dict["profit"] = int(task_prop[2])

    tasks.append(task_dict)

total_pos=[]


#Getting all the possible combination of the input.Big oh=(n!)
def heapPermutation(tasks, size):

    if size == 1:

        for j in range(1,len(tasks)+1):

               total_pos.append(tasks[j-1])

        return

    for i in range(size):

        heapPermutation(tasks, size - 1)

        if size & 1:
            tasks[0], tasks[size - 1] = tasks[size - 1], tasks[0]
        else:
            tasks[i], tasks[size - 1] = tasks[size - 1], tasks[i]



n = len(tasks)
heapPermutation(tasks, n)

first=True
temp=0
answer_arr=[]
temp_answer_arr=[]



for s in range(0, n):
    answer_arr.append(0)
    temp_answer_arr.append(0)

#Check all the posibilites and pick the maximum profit among them.Big oh=(n)
for i in range(0,int(len(total_pos)/n)):
    if(first):
        high=0
    if(temp>high):
        high=temp
        for s in range(0,n):
            answer_arr[s]=temp_answer_arr[s]


    temp=0

    for j in range(1,n+1):
        first=False
        if(j<=total_pos[i*n+j-1]["deadline"]):
            temp = temp + total_pos[i*n+j-1]["profit"]
            temp_answer_arr[j-1] = total_pos[i*n+j-1]["taskId"]
        else:
            temp_answer_arr[j-1] = 0


for i in range(0,n):
    if(answer_arr[i]!=0):
        print("ID:",answer_arr[i])

print("Total Profit:",high)

#In Conculusion,worst-case is n*n!

