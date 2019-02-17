
#maxDistance exercise 13


def maxDistance(x,  mylist):
    sum = 0
    for z in range(0, len(mylist)):

        if mylist[z] + sum > sum and mylist[z] + sum <= x:
            sum1 = sum + mylist[z]

        elif mylist[z] > x:
            del mylist[z]
            #print(mylist)

        if sum1 > sum and sum1 <= x:
            sum = sum1


    print(sum)

print('Enter a integer:')
x = int(input())
print("Enter a list numbers separated by space: ")
mylist = [int(x) for x in input().split()]

maxDistance(x, mylist)
