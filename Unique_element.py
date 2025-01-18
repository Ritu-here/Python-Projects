# def unique_element(lst):
#     unique_lst = []
#     for element in lst:
#         if element not in unique_lst:
#             unique_lst.append(element)
#             return unique_lst
        
# numbers = [1,2,3,2,3,2,3,4,5,5,4,3,7,8,5,9,8,21]
# unique_nums = unique_element(numbers)
# print(unique_nums)/

def unique_element(lst):
    return list(set(lst))

numbers = [1,2,3,4,3,2,1,5,6,4,5,9]
unique_nums = unique_element(numbers)
print(unique_nums)