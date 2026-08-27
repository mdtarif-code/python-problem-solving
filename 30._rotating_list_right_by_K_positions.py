def rotate_right(num, k):

    k = k%len(num)

    for i in range(k):  
        p = num.pop()
        num.insert(0,p)

    return num


numbers = [1, 2, 3, 4, 5]
k = 7
result = rotate_right(numbers,k)
print(result)