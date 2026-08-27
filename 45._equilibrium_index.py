# Sum of all elements to the left = Sum of all elements to the right

def equilibrium_index(numbers):
    total = sum(numbers)
    left = 0
    for i in range(len(numbers)):
        current = numbers[i]

        right = total - current - left

        if left==right:
            return i

        left += current

    return -1

numbers = [1, 3, 5, 2]
result = equilibrium_index(numbers)
print(result)