


#Getting İnput

people=[]
first=input().split()
length=len(first)
person_dict={}
person_dict["number"]=0
for j in range(0, length):

    if (int(first[j]) == 1):
        person_dict["know"] = j
        break
    else:
        person_dict["know"] = 0
people.append(person_dict)

for i in range(0,length-1):
    person_dict={}
    person_prop = input().split()

    person_dict["number"] = i+1
    for j in range(0,length):
        if(int(person_prop[j])==1):
            person_dict["know"] = j
            break
        else:
            person_dict["know"] = 0

    people.append(person_dict)

print(people)
knowCount=0
celebrity=True

# Check there is a celebrity.Big Oh(n)
for i in people:

    if(i["know"]==0):
        knowCount=knowCount+1
    if(knowCount>=2):
        celebrity=False
        break


# #(Decrease-by-One)alogorithm is used.Pop 2 people from stack,compare them and push one of them to the stack.Do it till only celebrity people left in stack.
# # Big oh(n)
if(celebrity):
    while(len(people)>1):
        A=people.pop()
        B=people.pop()
        print(A,B)
        if(A["know"]==B["number"] and A["know"]!=0):
            people.append(B)
        else:
            people.append(A)
    if(people[0]["know"]==0):
        print(people[0]["number"])
    else:
        print("-1")
else:
    print("-1")
#total bigOh(n)