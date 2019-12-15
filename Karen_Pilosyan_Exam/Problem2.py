import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str1", type=str)
parser.add_argument("str2", type=str)
args = parser.parse_args()

list1 = ["hi","b","c","8"]
print(list1)
#assert args.str1 in list1, "The value is not in list1"
if args.str1 not in list1:
    print("The value is not in list1")
else:
    for i in range(len(list1)):
        if args.str1 == list1[i]:
            list1[i]=args.str2
    
print(list1)

