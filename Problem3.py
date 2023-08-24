#method1


# n = int(input())
# nums = list(map(int,input().split()[:n]))
# target = int(input())
# result=[]
# for i in range(len(nums)):
#     if target-nums[i] in nums:
#         print('[',i,)

# method 2
n = int(input())
nums = list(map(int,input().split()[:n]))
target = int(input())
result=[]
visited = []
for i in range(len(nums)):
    if target-nums[i] not in visited:
        visited.append(target-nums[i])
        visited.append(nums[i])
        result.append(nums[i])
        result.append([i,nums.index(target-nums[i])])
print(result)
