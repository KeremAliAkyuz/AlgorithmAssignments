#Getting İnput(for getting input you should put blank space at end of input)
licenses=[]
flag=True
while flag:

    company_dict={}
    company_prop = input().split()
    if not company_prop:
        flag=False
        break
    if(flag):
        company_dict["company"] = int(company_prop[0])
        company_dict["price"] = int(company_prop[1])
        licenses.append(company_dict)
#-----------------------------------------------------------------
highest=0
order=0
ansArr=[]
#For this question,beacuse of increasing prices we tend to choose first highest price of all of them,then do it same the rest licenses.
#We use greedy algorithm pick highest cost to lowest cost.
for i in range(0,len(licenses)):
    for j in range(0,len(licenses)):
        if licenses[j]["price"]>highest:
            highest=licenses[j]["price"]
            order=j

    ansArr.append(licenses[order]["company"])
    licenses.pop(order)
    highest=0

print(*ansArr)

#total cost big-oh(n*n)

# PROOF
# Our goal is paying least money
#
# Greedy algorithm of this question tend to pay highest cost to lowest cost because the price doubles itself so it becoming getting larger rapidly
#
# Sorted list highest to lowest A={p1,p2,..,pn}
#
# we know that list is highest to lowest ,so for getting minimum price=p1*(2**0)+p2*(2**1)+...+pn*(2**n-1)
# if we change the placement of elements price going to be higher according to price equation,so we have to choose lowest price element to highest price element