import numpy as np

print("Enter distances separated by space all in one line: ") # 5 11 26 39 3 7
mylist1 = np.array([int(x) for x in input().split()])
row = int(len(mylist1) / 2)
mylist2 = mylist1.reshape(row, 2)
print(mylist2)
def sumIntervals(mylist2):
    sum = 0
    for i in range(0, len(mylist2)):
        sum += mylist2[i][1] - mylist2[i][0]
        if mylist2[i] == mylist2[i+1]:
            sum += mylist2[i+1][i+1] - mylist2[i+1][i]
        #elif
    print(sum)


sumIntervals(mylist2)
