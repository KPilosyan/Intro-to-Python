import argparse

parser = argparse.ArgumentParser()
parser.add_argument("var", type=int)
# What about type = str or bool ?
args = parser.parse_args()

list4 = [1,2,3,4,1]
print("Befor:", list4)
if args.var in list4:
    list4.remove(args.var)
print("After:", list4)