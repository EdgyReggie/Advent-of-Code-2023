with open('input') as f:
    lines = []
    for line in f.readlines():
        numChars = []
        for chars in line: 
            if chars.isdigit():
                numChars.append(chars)
        lines.append(numChars)
    
    nums = []
    
    for array in lines:
        numbers = ''.join(map(str, array))
        nums.append(numbers)

    print(nums)
