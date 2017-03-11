n = int(input())
l=[]
for i in range(n):
    l.append(input())
print("#1")
q = int(input())
m=[]
c=0
for i in range(q):
    l.append(input())
print("#2")
for x in m:
    print("#3")
    for y in l:
        c = c + y.count(x)
        print("#4")
    print(c)
    c=0
