#write a program to move all vowels to the left of string Note the occurance order 
def move_vowels_to_left(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    result = list(input_string)

    # Count the number of vowels
    for char in result:
        if char in vowels:
            vowel_count += 1

    # Move vowels to the left
    i = 0
    j = vowel_count
    while j < len(result):
        if result[i] in vowels:
            i += 1
            j += 1
        elif result[j] in vowels:
            result[i], result[j] = result[j], result[i]
            i += 1
            j += 1
        else:
            i += 1
            j += 1

    return "".join(result)

# Input string
input_str = input("Enter a string: ")
result_str = move_vowels_to_left(input_str)
print("Modified string:", result_str)
