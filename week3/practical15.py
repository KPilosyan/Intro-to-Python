import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key", type=str)
parser.add_argument("value", type=str)
args = parser.parse_args()

dict1 = {"key1": "val1", "key2": 10}
print(dict1)
dict1.update({args.key:args.value})
print(dict1)

