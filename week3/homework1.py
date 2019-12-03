#2)
a = [1, 4, 5, 7, 8, -2, 0, -1]
print("Initial List", a)
#2)
print("3rd:",a[3])
print("5th:",a[5])
#3)
a_sorted = a
a_sorted.sort(reverse=True)
print("Sorted:",a_sorted)
#4)
print(a_sorted[1:4])
print(a_sorted[2:7])
#5)
del a_sorted[2]
del a_sorted[2]
#6)
print(a_sorted)
#7)
b =["grapes", "Potatoes", "tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
print("List b:", b)
b_sorted = b
b_sorted.sort()
print("Sorted:", b_sorted)
#8)
c = [a[1], a[2], a[3], b[4:7]]
print(c)