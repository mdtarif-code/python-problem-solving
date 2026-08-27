def longest_subarray_with_sum_k(num,k):

    add = 0
    lenght = 0
    for i in range(len(num)-1):
        add = 0
        for j in range(i,len(num)):
            add += num[j]
            if add == k :
                current_lenght = j - i + 1
                if current_lenght>lenght:
                    lenght = current_lenght
                
    return lenght


numbers = [10, 5, 2, 7, 1, 9]
k = 15
result = longest_subarray_with_sum_k(numbers,k)
print(result)