callback = [lambda x : x**2 ,lambda x: x**3 , lambda x: x**4]
for bucky in callback:
    x=int(input('enter your fav no \n'))
    print("result:",bucky(x))
