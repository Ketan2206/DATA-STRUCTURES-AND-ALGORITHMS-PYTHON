def leftRotate(arr,d): #better approach    TC O(n)    SC O(n)

    arrSize = len(arr)

    temp = []

    d = d%arrSize

    if d!=0:

        for i in range(d):

            temp.append(arr[i])

        for i in  range(d,arrSize):

            arr[i-d] = arr[i]
    
        for i in range(arrSize-d,arrSize):

            arr[i] = temp[i-(arrSize-d)]
    
        return arr
    

    return arr



def leftRotate2(arr,d):  #optimal approach      TC O(n)    SC O(1)
    

    arrSize = len(arr)
    d = d%arrSize


    
    arr = reverse_list(arr,0,d)

    arr = reverse_list(arr,d,arrSize)

    arr = reverse_list(arr,0,arrSize)

    
    return arr
    
    





def reverse_list(arr,start,end):
    left = start
    right = end-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr





if __name__ == "__main__":


    arr = [int(i) for i in input(" ENTER ELEMENTS ").split()]

    arr2 = arr.copy()

    numOfRotations = int(input(" ENTER PLACES YOU WANT TO ROTATE "))

    print(leftRotate(arr, numOfRotations))

    print(leftRotate2(arr2,numOfRotations))



