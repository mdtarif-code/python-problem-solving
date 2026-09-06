# Given a list of numbers, find the element that appears more than n/2 times.

def majority_element(numbers):

    if len(numbers) == 0:
        return None

    candidate = None
    count = 0

    for num in numbers:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


numbers = [2, 2, 1, 1, 1, 2, 2]

result = majority_element(numbers)

print(result)