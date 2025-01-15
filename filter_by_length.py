def filter_by_length(lst , length):
    result = []
    for string in lst:
        if len(string) > length:
            result.append(string)
    return result
        
str = [ "apple" ,"banana" , "kiwi" ,"pear"]
length = 4
filtered_str = filter_by_length(str , 4)
print(filtered_str)