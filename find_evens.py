def find_even_numbers(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = find_even_numbers(numbers)
print(even_numbers)