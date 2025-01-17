def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return  False
    
numbers = [1,2,3,4,5]
print(is_sorted(numbers))