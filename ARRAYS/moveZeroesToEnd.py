def moveZeroes(arr): 


    if 0 not in arr:
        print("Returned from first condition")
        return arr

    for i in range(len(arr)):

        if arr[i] == 0:
            j=i
            break
    
    for i in range(j+1,len(arr)):
        if arr[i]!=0:
            arr[j],arr[i] = arr[i],arr[j]
            j+=1
    
    return arr




if __name__== "__main__":

    arr = [int(i) for i in input("Array elements ").split()]

    print(moveZeroes(arr))
