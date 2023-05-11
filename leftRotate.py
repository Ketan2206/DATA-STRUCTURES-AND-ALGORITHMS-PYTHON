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
    
    print("jumped directly here")
    return arr



def leftRotate2(arr,n): #optimal approach      TC O(n)    SC O(1)
    pass 













if __name__ == "__main__":


    arr = [int(i) for i in input(" ENTER ELEMENTS ").split()]

    numOfRotations = int(input(" ENTER PLACES YOU WANT TO ROTATE "))

    print(leftRotate(arr, numOfRotations))



