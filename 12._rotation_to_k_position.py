
def rotate(num, k):
    for i in range(k):
        temp = num.pop(len(num)-1)
        num.insert(0,temp)

    return num

numbers = [1, 2, 3, 4, 5]
k = 2
result = rotate(numbers,k)
print(result)   