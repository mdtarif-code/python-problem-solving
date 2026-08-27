def zeros_at_end(numbers):
    zeros = 0
    while 0 in numbers:
        numbers.remove(0)
        zeros += 1
    for i in range(zeros):
        numbers.append(0)

    return numbers

numbers = [0, 0, 0, 3, 12]
result = zeros_at_end(numbers)
print(result)