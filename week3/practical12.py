import argparse

parser = argparse.ArgumentParser()
parser.add_argument("var", type=int)
args = parser.parse_args()
set3 = {10,2,3,4,55,6}
if args.var >= min(set3) and args.var <= max(set3):
    print("True")
else:
    print("False")
