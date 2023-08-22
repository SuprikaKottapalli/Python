def UniqueNames(*Name):
    result = []
    for i in Name :
        if Name.count(Name) == 1:
            result.append(Name)
    return result
N = int(input())
Name = list(map(str,input().split()[:N]))
print(UniqueNames(*Name))