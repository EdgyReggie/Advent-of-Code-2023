with open('input') as f:
    lines = []
    for line in f.readlines():
        newLines = []
        for chars in line: 
            newLines.append(chars)
        lines.append(newLines)
        print(lines)
