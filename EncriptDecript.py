#input_text = "i am going to college"
# vowels = "aeiouAEIOU"
# next_letters = "eiouaEIOUA"
# translation_table = str.maketrans(vowels, next_letters)
# converted_text = input_text.translate(translation_table)

# print(converted_text)


#esay method
msg = input("Enter the name:")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMOPQRSTUVWXYZ"
for ch in msg:
    if ch in "aeiouAEIOU":
        idx = chars.index(ch)
        print(chars[idx+1],end="")
    else:
        print(ch,end="")