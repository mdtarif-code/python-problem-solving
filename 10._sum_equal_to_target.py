
def sum_equal_to_target(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            add = num[i] + num[j]
            if add==target:
                return [i,j]
            
#numbers = [2, 7, 11, 15]
numbers = [2,1,4,5,3]
target = 9
result = sum_equal_to_target(numbers)
print(result)


