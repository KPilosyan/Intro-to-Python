import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", help="display a square of a given number",type=int)

parser.add_argument("text", help="some text", type=str)

parser.add_argument("--cube", help="display a cube of a given number", type=int)

parser.add_argument("--cube1", help="display a cube of a given number", type=int)

args = parser.parse_args()

print('square: ', args.square**2)
print(args.text)
if args.cube:
    print(args.cube**3)
if args.cube1:
    print(args.cube1**3)