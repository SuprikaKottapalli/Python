num = int(input("Enter the num:"))

i = 2
while i <= num:
    if i % 2 == 0:
        print(i, end=' ')
        i += 2

i=1
while i <= num:
    if i % 2 != 0:
        print(i, end=' ')
        i += 2

