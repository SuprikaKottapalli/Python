name = input("Enter your name:")
for i in range(len(name)):
    print(name[i],end=" ")

#Reverse
for ch in reversed(name):
    print(ch,end=' ')
print(name)

#Sorted
print(sorted(name))
print(name)

#Repication
print(name*4)

#Counting
ch = 'a'
print(name.count('a'))

#Validation
name.isalnum()