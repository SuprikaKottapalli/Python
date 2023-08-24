#print all even num of list at left
'''Move all even num of giveb n list of num 
note occraence order should preserve
ex: input:10
1 2 3 4 5 5 6 7 8 9
output: 2 4 6 8 1 3 5 5 7 9'''

def rearrange(nums):
    even = []
    odd = []
    
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    rearranged = even + odd
    
    return rearranged

n = int(input("Enter the size of list u want:"))
num = list(map(int, input("Enter nums (split by comma): ").split(",")))

result = rearrange(num)

for num in result:
    print(num, end=' ')


#write a program to move all vowels to the left of string Note the occurance order 