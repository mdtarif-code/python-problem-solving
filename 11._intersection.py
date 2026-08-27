def intersection(num1,num2):
    inter = []
    for i in num1:
        if i in num2 and i not in inter:
            inter.append(i)
    return inter

list1 = [1, 2, 2, 4, 5]
list2 = [4, 2, 2, 7]

result = intersection(list1,list2)
print(result)
