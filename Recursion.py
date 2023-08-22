def printTable(N,i):
    if i<=10:
        print(N,'*',i,'=',N*i)
        i+=1
        printTable(N,i)
N = int(input())
printTable(N,1)

def PrintTable(N):
    for i in range(1,11):
        print(N,'*',i,'=',N*i)
        PrintTable(10)

PrintTable()