def concatenate_strings(lst):
    result = ''
    for string in lst:
        result += string + ''
    return result.strip()

strings = ['Hello' , 'world' , 'python' , 'is' , 'awesome']
concatenated_string = concatenate_strings(strings)
print(concatenated_string)