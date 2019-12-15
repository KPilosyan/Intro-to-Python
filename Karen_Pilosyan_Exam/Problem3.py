l = ["a",0,2,True,"hi"]
try:
    print(l[10])
#except Exception:
#    print("Sorry, the list index is out of range")
except IndexError as e:
    print(e)