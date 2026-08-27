def second_smallest_distinct_number(number):

    seen = []
    for i in number:
        if i not in seen:
            seen.append(i)
    
    if len(seen)<=1:
        second_smallest = None
        return second_smallest
    
    smallest = seen[0]
    second_smallest = seen[1]
    for i in seen:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i !=smallest:
            second_smallest = i

    return second_smallest


numbers = [1,2,3]
result = second_smallest_distinct_number(numbers)
print(result)