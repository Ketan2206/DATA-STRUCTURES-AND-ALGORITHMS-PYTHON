arr = [int(i) for i in input("Enter the numbers").split()]


myDict = {}

print(arr)

for item in arr:

    if item in myDict:
        myDict[item] += 1

    else:
        myDict[item] = 1
    


for item , freq in myDict.items():

    print(f"Key {item} : Value {freq}")
#print(myDict)

for item in myDict.keys():

    if myDict[item] == 2:
        print(item)
