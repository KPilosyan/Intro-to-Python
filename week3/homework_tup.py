#1)
t1 = (1, True, "a", -2, "Anna")
#2)
l1 = list(t1)
del l1[1]
t1 = tuple(l1)
print(t1)
#3)
t2 = (1,2,3,4,5)
#4)
t3 = (t1[0], t1[1], t2[0], t2[1], t2[2])
print("t3:", t3)
#5)
print(t3[2])
#6) 
t4 = [(1,3,5), (8,9), ("Anna", "Bob", "Alice")]
print(t4[0][1])