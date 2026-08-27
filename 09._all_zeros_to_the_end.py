def all_zeros_at_end(number):

    non_zeros = [x for x in number if x!=0]
    zeros = [x for x in number if x==0]
    return non_zeros + zeros

numbers = [0, 1, 0, 3, 12]
result = all_zeros_at_end(numbers)
print(result)





