'''Slicing is an operation which is appkicable on only index-based collection 
- Slicing is procedure to divide main list/ a sequence into multiple sub sequences based on our requirement
Syntax:
    collection_name[start:end:step]
where: 
Start end step are integers
'''
name = "SuprikaKottapalli"
print(name[:7])
print(name[6:])
print(name[4:8])
print(name[:-7])
print(name[-7:])
print(name[-9:-5])

name2 = input()
print(name2[::-1])

name3 = input("Enter Name:")
index = len(name3)
#idx = index(name3)
id = (index/2)

#output = "alaJndhar"
print(name3[id::-1],name3[4:9])
name = "jalandhar"
n = len(name)
mid = len(name)//2
print(name[0:mid][::-1]) #reverse only half
print(name[mid:]) 

print(name[:mid][::-1]+name[mid:]) #reverse full


n = len(name)
mid = len(name)//2
print(name[:mid])
print(name[mid:][::-1])
print(name[:mid]+name[mid:][::-1])