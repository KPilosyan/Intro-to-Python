count_a=0
count_b=0
count_c=0
count_d=0
count_e=0
text1 = input("Input text: \n")
for i in text1:
    if i == 'a':
        count_a+=1
    if i =='b':
        count_b+=1
    if i =='c':
        count_c+=1
    if i =='d':
        count_d+=1
    if i =='e':
        count_e+=1

print("The given text:", text1)
print("# of a:", count_a)
print("# of b:", count_b)
print("# of c:", count_c)
print("# of d:", count_d)
print("# of e:", count_e)