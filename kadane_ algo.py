'''program to find the the largest contiguous sub array in a given array'''
list1 = list(map(int,input("enter the list:").split()))
real_sum = 0 
temp = 0 
flag = 0
temp1 = 0
if  list1[0] < 0 :
    temp = list1[0]
for i in list1:
    if i < 0 and i > temp:
        temp = i
        flag = -1

    temp1 = temp1 + i

    if temp1 < 0:
        temp1 = 0
    if temp1 >=real_sum:
        real_sum = temp1    

if flag is -1:
    print("only for negative number! {}".format(temp))
else:
    print("the largest sub-arry is {}".format(real_sum))    