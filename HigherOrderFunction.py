# #Lamda function
# output = lambda name:name.upper()
# name = input()
# print(output(name))

# #filter function
# n = int(input())
# nums = list(map(int,input().split()))
# result = filter(lambda x:n%x==0,nums)
# print([x for x in result])

#map function
def listStarts(name):
    return name[0] == 'r'
name = list(map(str,input().split(',')))
result = map(listStarts,name)
print(list(result))