# Given two sorted lists, find the elements that appear in both lists.

def elements_appearing_in_both_list(num1,num2):
    common = set()
    i = 0
    j = 0
    while i<len(num1) and j<len(num2):
        l1 = num1[i]
        l2 = num2[j]

        if l1==l2:
            common.add(l1)
            i += 1
            j += 1
        elif l1<l2:
            i += 1
        elif l1>l2:
            j += 1
        
    return common

list1 = [1, 2, 4, 5, 6]
list2 = [2, 3, 5, 7]
result = elements_appearing_in_both_list(list1,list2)
print(result)