def sum_of_even_numbers(lst):
    total = 0
    for num in lst:
        if num%2 == 0:
            total = total + num
    return total

numbers = [3, 8, 5, 12, 7, 10]

result = sum_of_even_numbers(numbers)
print(f"The sum of all even numbers is {result}")
