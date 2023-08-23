# # Find the name of given n list of names contains lenght>5 no of vowels in their name
# 6 
# name1 name 2 nmae3 name 4 nmae5 name6

# def listStarts(name):
#     vowels = 'a e i o u'
#     if count(vowels) in name > 5 :
#         return name
#         # print(name[1])
#     # return name[ ] == 'a','e','i','o','u'
# name = list(map(str,input().split(',')))
# result = map(listStarts,name)
# print(list(result))


def count_vowels(name):
    vowels = 'aeiou'
    count = 0
    for char in name:
        if char.lower() in vowels:
            count += 1
    return count

def filter_names(name):
    return len(name) > 5 and count_vowels(name) > 5

input_names = input().split()

filtered_result = list(filter(filter_names, input_names))
print(filtered_result)
