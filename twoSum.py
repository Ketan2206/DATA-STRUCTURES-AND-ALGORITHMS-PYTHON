arr = [int(i) for i in input(" ENTER THE ARRAY ELEMENTS ").split()]
pointerStart = 0
pointerEnd = len(arr)-1 

target = int(input("ENTER TARGET SUM "))

while pointerStart < pointerEnd :

    if arr[pointerStart] + arr[pointerEnd] == target:

        print(f"{arr[pointerStart]} {arr[pointerEnd]}")
        break
 


    if arr[pointerStart] + arr[pointerEnd] < target:

        pointerStart+=1

    if arr[pointerStart] + arr[pointerEnd] > target:

        pointerEnd -=1





