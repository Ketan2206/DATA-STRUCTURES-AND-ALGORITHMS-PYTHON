
def twoSum (arr, target):



    sumDict = set()
    for i in range(len(arr)):

        more = target - arr[i]

        if more in sumDict:
            print(sumDict)
            return arr[i] , more
    
        else:
            sumDict.add(arr[i])

    print(sumDict)

    return None, None 
    

if __name__ == "__main__":



    arr = [int(i) for i in input(" ENTER THE ARRAY ELEMENTS ").split()]
    target = int(input("ENTER TARGET SUM "))
    firstVal, SecondVal = twoSum(arr,target)

    print(f"{firstVal}, {SecondVal}")
    

        

        
