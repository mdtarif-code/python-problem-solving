def common_elements(list1, list2, list3):

    common = []
    for i in list1:
        if i in list2 and i in list3 and i not in common:
            common.append(i)
    
    return common

list1 = [1, 2, 2, 3]
list2 = [2, 3, 4]
list3 = [2, 3, 5]

result = common_elements(list1, list2, list3)
print("Common elements are:",result)