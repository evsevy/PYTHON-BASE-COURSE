arr = {"Один": "one", "Два": "two", "Три": "three"}
print(" _________________ ")
print("|  Rus   :  Eng   |")
print("|-----------------|")
for key, value in arr.items():
    print("|  {r:5s} :  {w:5s} |".format(r = key, w = value))
print("|-----------------|")
