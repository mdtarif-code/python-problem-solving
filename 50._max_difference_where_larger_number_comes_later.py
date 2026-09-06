def max_difference(numbers):
    largest_diff = float('-inf')
    smallest_current = numbers[0]
    for num in numbers[1:]:
        
        diff = num - smallest_current

        if diff>largest_diff:
            largest_diff=diff

        if smallest_current>num:
            smallest_current=num

    return largest_diff
    
numbers = [7, 1, 5, 3, 6, 4]
result = max_difference(numbers)
print(result)