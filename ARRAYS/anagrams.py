def isAnagram(string1,string2):
    
    freq = {}  # empty dict to keep count of frequency

    for i in range(len(string1)):

        index = (ord(string1[i])-ord('A'))

        if index in freq:
            
            freq[index] += 1
        
        else:

            freq[index] = 1



    for i in range(len(string2)):

        index = (ord(string2[i])-ord('A'))

        freq[index] -=1

    
    for i in freq.values():

        if i != 0:
            return False
    
    return True


if __name__ == "__main__":

    str1, str2 = input("ENTER TWO STRINGS SEPERATED BY SPACE ").split()

    print(isAnagram(str1,str2))










        
    



