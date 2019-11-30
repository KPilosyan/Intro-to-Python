import sys 

list1 = ["hello", 1, True]
new_list1 = list1
list2 = sys.argv[1:]
print("Befor:", list1)
for i in list2:
    new_list1.append(i)
print("After:", new_list1)
