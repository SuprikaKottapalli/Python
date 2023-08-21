#Iterating the list
l1 = [1,2,3,4,7]
for i in l1:
    print(i)

#iterating list with index
l2 = [1,2,3,4,5]
for i in range(len(l2)):
    print(l2[i])

#Reading n element into a list -- iterative method
n = int(input("Enter the size of list:"))
lst = []
for i in range(n):
    x = int(input("Enter the num in list:"))
    lst.append(x)

#another method
n = int(input("Enter the size of List:"))
lst = list(map(int,input("Enter elements:"),split()[:n]))
print(lst)

# find the greatest elements of odd index values of given n elements 
# input:
#         enter size of list: 14
#         enter elements : 4 6 7 8 9 14 3 11 10 5
# Output:
#        Greatest num :14

n = int(input("Enter the size of List:"))
nums = list(map(int,input("Enter elements:").split()[:n]))
maxNum = nums[1]
for i in range(n):
    if i % 2 != 0 :
        if maxNum < nums[i]:
            maxNum = nums[i]
print(maxNum)

n = int(input("Enter the size of List:"))
nums = list(map(int,input("Enter elements:").split()[:n]))
maxNum = nums[1]
for i in range(3,n,2):
    if maxNum<nums[i]:
        maxNum = nums[i]
print(maxNum)

n = int(input("Enter the size of List:"))
nums = list(map(int,input("Enter elements:").split()[:n]))

print("Sorted order is: ",sorted(nums))
for i in reversed(nums):
    print(i,end=" ")


list1 = ['a','b','c','d','e']
list2 = [1,2,3,4,5]
print(list1)
print(list2)
list1.extend(list2)
print(list1)
print(list2)


list3 = [1,2,3,4,5,6]
list4 = [3,4,5,6,7,8,3]
print(list3 + list4)

Deletion
list5 = [1,2,3,4,5,6,7,5,3]
print(list5)
del(list5[6])
print(list5)
del(list5[:2])
print(list5)