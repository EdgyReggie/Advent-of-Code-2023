# Open the file, read each line and check every character if its a number and add it to a list.
with open('input') as f:
    lines = []
    for line in f.readlines():
        num_chars = []
        for chars in line: 
            if chars.isdigit():
                num_chars.append(chars)
        lines.append(num_chars)
    
    # For each of the arrays in the list, get the first and last values and append the to the list.
    # This however does create a list of tuples.
    tup_nums = []
    for array in lines:
        if len(array) > 1: 
            first_num = array[0]
            last_num = array[-1]
            tup_nums.append((first_num, last_num))
        elif len(array) == 1:
            first_num = array[0]
            last_num = array[0]
            tup_nums.append((first_num, last_num)) 

    # For each tuple, use the map function to convert the 2 numbers to a string and convert the string
    # into an int.
    result = []
    for tup in tup_nums:
        value = int(''.join(map(str, tup)))
        result.append(value)    
        
    # Print the sum of all the numbers
    print(sum(result))
