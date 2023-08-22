# Merge Sort
# Sorted()
list1 = [2,5,6,7,8]
list2 = [1,4,3,9,10]
print("Result:",sorted(list1+list2))


#Method 2
list1.extend(list2)
for i in sorted(list1):
    print(i,end=" ")

# method 3

list1 = [2, 5, 6, 7, 8]
list2 = [1, 4, 3, 9, 10]

result = []
i = j = k = 0

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

# Append the remaining elements from both lists, if any
result.extend(list1[i:])
result.extend(list2[j:])

print(result)


#Method 4
list1 = [2, 5, 6, 7, 8]
list2 = [1, 4, 3, 9, 10]

result = []
i = j = 0

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

Append the remaining elements from both lists, if any
while i < len(list1):
    result.append(list1[i])
    i += 1

while j < len(list2):
    result.append(list2[j])
    j += 1

print(result)


 
