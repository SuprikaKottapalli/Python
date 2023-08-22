#  print the list element which are greater than neighbors of "N" list
# # input :
# # 10
# # 11,21,34,10.9,7,8,6,5,15
# # output:
# # 34,8


def find_elements_greater_than_neighbors(nums):
    result = []
    
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            result.append(nums[i])
    
    return result


input_str = input("Enter a list of numbers separated by commas: ")
num_list = [float(num) for num in input_str.split(',')]

# Find and print elements greater than neighbors
greater_elements = find_elements_greater_than_neighbors(num_list)
output_str = ",".join(str(num) for num in greater_elements)
print("Output:", output_str)

