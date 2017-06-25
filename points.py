''' program to find if a given points lie inside or outside of a given line'''
m= map(int,input("enter the value of m:"))
c= map(int,input("enter the value of c:"))
x,y = map(int,input("enter the value of the tuple :").split())
if m!=0 and c!=0:
    if x < (-c/m) and y<c :
        print("the points lie inside")
    else:
        print("the points lie outside")
elif c ==0:
    if y< m*x and x < y/m:
        print('the points lie inside')
    else:
        print("the points lie outside")
elif m ==0:
if y < c or x < x :
    print("the points lie inside ")
else:
    print("the point lie outside")    