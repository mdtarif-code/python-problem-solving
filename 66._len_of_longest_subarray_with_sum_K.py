# Given a list of integers and a target K, 
# find the length of the longest contiguous subarray whose sum is exactly K.

def longest_subarray(numbers,k):
    
    seen = {0:-1}
    running_sum = 0
    lenn = 0
    for i in range(len(numbers)):

        running_sum += numbers[i]

        pre_sum = running_sum-k

        if pre_sum in seen:
            lenn = max(lenn,(i - seen[pre_sum]))
            
        seen[running_sum] = i
    
    return lenn

numbers = [10, 5, 2, 7, 1, 9]
k = 15
result = longest_subarray(numbers,k)
print(result)