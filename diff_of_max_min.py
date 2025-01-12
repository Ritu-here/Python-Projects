def range_of_list(lst):
    return max(lst) - min(lst)

# def range_of_list(lst):
#     lst.sort()
#     return lst[-1] - lst[0]


numbers = [5,2,9,1,7]
range_value = range_of_list(numbers)
print(range_value)