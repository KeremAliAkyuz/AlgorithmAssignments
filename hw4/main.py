import sys
#Getting input
input = list(map(int, input().split()))
N=input[0]
M=input[1]
#defining memo array
MAX = 1000
memo = [[-1 for i in range(MAX)] for j in range(MAX)]
#TOP-DOWN function
def skyscraper(floor,snookerBall):
    #if there are already visited nodes checks and return
    if (memo[floor][snookerBall] != -1):
        return memo[floor][snookerBall]
    #if we have 1 floor then 1 trial at worst,if we have 0 floor 0 trial so return floor
    if(floor == 1 or floor == 0):
        return floor
    #if we have 1 snooker ball,we have to try every floor in worst case so retrun floor
    if(snookerBall == 1):
        return floor

    min = sys.maxsize
    ans = 0
    #spesific floor can be every floor so we do it for all floors zero to N
    for i in range(1,floor+1):
        #there is two possibility snooker ball breaks or not break
        #if snooker ball breaks spesific floor must have been one of the lower floors
        #if snooker ball not breaks spesific floor must have been one of the upper floors
        #we want to choose worst of our solutions so getting maximum all of them
        ans = max(skyscraper(i - 1, snookerBall - 1), skyscraper(floor - i, snookerBall))

        if (ans < min):
            min = ans
    #Save the node in memo
    memo[floor][snookerBall] = min + 1
    return min + 1

print(skyscraper(N,M))
