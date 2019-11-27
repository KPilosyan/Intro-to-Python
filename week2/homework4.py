import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", type=str)
args = parser.parse_args()

print("The given string:", args.text)
list1 = args.text.split()
count1=0
count2=0
for i in list1:
    if i == "USA":
        count1+=1
    if i == "usa":
        count2+=1
print("The USA/usa count is:", count1 + count2)

if "USA" not in list1 and "usa" not in list1:
   exit()

args.text = args.text.replace("USA","Armenia")
print("The new string:", args.text.replace("usa", "Armenia"))

