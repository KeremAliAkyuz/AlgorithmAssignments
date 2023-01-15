#Getting input
frogA = list(map(int, input().split()))
frogB = list(map(int, input().split()))
#For ending the loop add -1 to the input lists
frogA.insert(0, -1)
frogB.insert(0, -1)
#Defining memo array for memoization
MAX = 1000
memo = [[-1 for i in range(MAX)] for j in range(MAX)]
#TOP-DOWN
#Function calculates total road of frogs can travel
def frogs(n, m, memo):
    #if there are already visited nodes checks and return
    if memo[n][m] != -1:
        return memo[n][m]
    #if frog A's or frog B's first element is -1,there is no road to go so return 0
    if frogA[n] < 0 or frogB[m] < 0:
        return 0
    #if frog A's or frog B's elements are 0,they reach the start point so there is a path so return 1
    if frogA[n] == 0 and frogB[m] == 0:
        return 1
    #if absolute value of distance between frog A and frog B is travel all nodes recursively and save it to memo array and return 1
    if abs(frogA[n] - frogB[m]) <= 100:
        memo[n][m] = frogs(n - 1, m, memo) + frogs(n, m - 1, memo)
        return memo[n][m]
    #else return 0
    else:
        return 0

#For calculating total roads call the function
totalRoads=frogs(len(frogA)-1, len(frogB)-1, memo)
#if total roads higher than 0, there is at least 1 road so print true
if totalRoads>0:
    print("true")
#else print false
else:
    print("false")

#With the help of the memoization we travel m*n nodes instead of 2**m+n


#--------------------------------------------------------------------------------------------------
#WITHOUT MEMOIZATION

# def frogs(n,m):
#     if frogA[n] < 0 or frogB[m] < 0:
#         return 0
#     if frogA[n] == 0 and frogB[m] == 0:
#         return 1
#
#     if abs(frogA[n] - frogB[m]) <= 100:
#
#         return frogs(n - 1, m) + frogs(n, m - 1)
#     else:
#         return 0
#
# print(frogs(len(frogA)-1, len(frogB)-1))