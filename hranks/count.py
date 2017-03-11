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
for i in m:
    print("#3")
    for j in l:
        c = c + j.count(m)
        print("#4")
    print(c)
    c=0
