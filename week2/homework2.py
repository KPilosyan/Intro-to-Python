import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text",type=str)
args = parser.parse_args()

if len(args.text) >= 7 and len(args.text)%2 == 1:
    print("The old string:", args.text)
    mid = len(args.text)//2 + 1 
    mid_three = args.text[mid-2:mid+1]
    print("Middle 3 characters", mid_three)
    new_str = args.text.replace(mid_three, mid_three.upper())
    print("The new string:", new_str)
else:
    print("Please insert 7 or more, odd number of characters")