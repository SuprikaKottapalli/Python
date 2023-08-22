d1 = {}
d2 = {1234:"Suppi", 2134:"abc"}
print(type(d1))
print(type(d2))


Stubents = {}
N = int(input("Enter num: "))
for i in range(N):
    rno = int(input(("Enter roll num: " )))
    name = input("Name:")
    Stubents[rno] = name
    print(Stubents)