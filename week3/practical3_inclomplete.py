import argparse

parser = argparse.ArgumentParser()
parser.add_argument("var", type=int)
# What about type = str or bool ?
args = parser.parse_args()

list2 = [1, 5, True, "str", 5, 10, "str"]
count=0
for i in list2:
    if args.var == i:
        count+=1

print("list2 =", list2)
print("Number of", str(args.var) + "s =", str(count))

