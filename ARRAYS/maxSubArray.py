
arr = [int(i) for i in input("Enter numbers seperated by space ").split()]

maxSum = float('-inf') 
sum = 0

print(maxSum)

for i in range(len(arr)):

    if sum == 0 :

        startIndex = i
        
    sum = sum + arr[i]

    if maxSum < sum:

        maxSum = sum
        endIndex = i
    
    if sum < 0:

        sum = 0
    
print(maxSum) 
print(f" {startIndex} {endIndex}")