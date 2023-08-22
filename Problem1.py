# def MinMax(list1):
#     a = min(list1)
#     b = max(list1)
#     c = a+b
#     print(c)

# list1 = [1,2,3,4,5,6,7,8,9,10,11]
# MinMax(list1)
# print(min(list1)+max(list1))

# def sumMinMax(nums):
#     minimum = maxmimum = nums [0]
#     for x in nums:
#         if x<minimum:
#             minimum = x
#         if x>maxmimum:
#             maxmimum = x
#     return maxmimum+minimum


# N = int(input())
# nums = list (map(int , input().split()[:N]))
# print(sumMinMax(nums))

def problem(list3):

# print the list element which are greater than neighbors of "N" list
# input :
# 10
# 11,21,34,10.9,7,8,6,5,15
# output:
# 34,8