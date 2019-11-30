import sys 

list1 = ["hello", 1, True]
list2 = sys.argv[1:]
print("Befor:", list1)
#list1.append(list2)
#print("After:", list1)
for i in list2:
    list1.append(i)
print("After:", list1)
