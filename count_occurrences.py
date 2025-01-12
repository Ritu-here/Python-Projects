def count_occurrences(lst , value):
    count = 0
    for element in lst:
        if element == value:
            count += 1 
    return count 
numbers = [ 1,2,3,4,5,6,2,2,8,2,6,2,9]
target = 2 
occurrences = count_occurrences(numbers , target)
print(occurrences)