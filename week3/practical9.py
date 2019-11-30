import argparse

parser = argparse.ArgumentParser()
parser.add_argument("var", type=int)
args = parser.parse_args()
set1 = {1,2,3,"hi",True,0}
print("Before:", set1)
set1.remove(args.var)
print("After:", set1)