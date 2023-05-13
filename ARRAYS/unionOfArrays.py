def union(arr1,arr2):
    

    arr1.sort()
    arr2.sort()

    len1 = len(arr1)
    len2 = len(arr2)

    i,j = 0,0

    union = []

    while(i<len1 and j<len2):


        if arr1[i]>=arr2[j]:
            if arr2[j] not in union:
                union.append(arr2[j])
            j+=1

        elif(arr1[i] <= arr2[j]):
            if (arr1[i] not in union):

             union.append(arr1[i])
            i+=1

    
            

    while(i<len1):

        if arr1[i] not in union:
                union.append(arr1[i])
        i+=1

    while(j<len2):
        if arr2[j] not in union:
            union.append(arr2[j])
        j+=1
        
    return union

        

        
        



        















if __name__ =="__main__":

    arr1 = [int(i) for i in input("ARR1 ELEMENTS ").split()]
    arr2 = [int(i) for i in input("ARR2 ELEMENTS ").split()]

    print(union(arr1,arr2))
