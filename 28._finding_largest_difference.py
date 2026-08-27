def largest_difference(num):

    largest = 0
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            diff = num[j] - num[i]
            if diff>largest and num[i]<num[j]:
                largest = diff

    return largest

numbers = [7, 1, 5, 3, 6, 4]
result = largest_difference(numbers)
print("The largest difference of two elements where first element is less than second is:",result)