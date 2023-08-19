input_name = input("Enter a name: ")

vowels = ''
consonants = ''

for char in input_name:
    if char.lower() in 'aeiou':
        vowels += char
    else:
        consonants += char

output = vowels + consonants
print(output)
