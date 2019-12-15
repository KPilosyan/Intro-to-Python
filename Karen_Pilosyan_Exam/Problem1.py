string = input("Input a strong")
d=0
l=0
for i in string:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1

print("Given string:", string)
print("Digits:", d)
print("Non-digits:", l)
