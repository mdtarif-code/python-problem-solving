# Given two sorted lists, return their union without duplicate values.

def union_of_two_sorted_list(num1,num2):

    result = []
    i = 0
    j = 0
    while i<len(num1) and j<len(num2):
        l1 = num1[i]
        l2 = num2[j]

        if l1 < l2:
            result.append(l1)
            i += 1
        elif l2 < l1:
            result.append(l2)
            j +=1
        elif l1 == l2:
            result.append(l1)
            i += 1
            j += 1

    result.extend(num1[i:])
    result.extend(num2[j:])
    return result

list1 = [1, 2, 4, 5, 6]
list2 = [2, 3, 5, 7]
result = union_of_two_sorted_list(list1,list2)
print(result)