import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="Changes format of the text", type=str)
args = parser.parse_args()

print("The given string:", args.text)
print("All lowercase:", args.text.lower())
print("All uppercase:", args.text.upper())