list= list(map(int, input().split()))


list = sorted(list)
#big oh for sorted list n * logn

#In this question,for paying minimum price sort the list and getting highest and second highest pairs together.
#We use greedy algorithm for getting maximum pairs to mimimum pairs in order
for i in range (len(list)-1,0,-2):
    print(list[i],list[i-1])
#big oh of for loop n

#total big-oh n*logn

# PROOF
# Our goal is spend the least money,so sum of smaller pairs must be maximum.
#
# So we must pair largest moneys among themselves.
#
# In our greedy algorithm,first we sort the list from higher price to lower price sorted list like ={(n,n-1),(n-2,n-3)...,(2,1)}
# so we dont have to pay every pairs smaller element (n-1,n-3,n-5...)
# we know that from n-1 to 1 if we sum all of that there is no other combination higher than it
# total smaller pairs = (n-1+n-3+...+1)
#
# suppose that(12,10,8,6,4,2)
# n-1,n-3,n-5=10+6+2 is the sum of the smaller pairs highest price