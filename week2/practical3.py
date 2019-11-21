import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Prints user name")
args = parser.parse_args()

print("Welcome,", args.name + "!")