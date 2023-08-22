'''Store and print the Squres andd cubes of each number in dictionay'''


N = int(input("Enter num: "))
num_sq_cb  = {}


for i in range(1,N):
    sq = i**2
    cb = i**3
    num_sq_cb[i] = [sq,cb]

for n,sq_cb in num_sq_cb.items():
    print(n,':',[sq_cb[0],sq_cb[1]])