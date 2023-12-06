from queue import Queue
import string

def main():
    queue = Queue() 
    total = 0

    # Thank you Chat-GPT 
    with open("example-input", "r") as f:
           lines = f.readlines() 

    max_length = max(len(line) for line in lines)
    # adjust the input so that every line is the same length, no sizing issues between the rows 
    schematic = [list(line.strip().ljust(max_length)) for line in lines]

    for i, row in enumerate(schematic):
        for  j, char in enumerate(row):
            element = ""
            if char.isdigit():
                queue.put(char)
            elif char == '.' and not queue.empty():
                while not queue.empty():
                    element += queue.get()
                    if is_part_number(schematic, i, j):
                        total += element
            elif is_special_char(char) and not char == '.': # TODO: Move this if statement 
                print()
            elif char == '.' and queue.empty():
                print()
    
    print(total)

def is_part_number(schematic, i, j):   
    if i == 0:
        # Top row
    elif: i == len(schematic):
        # Bottom row 
    elif: j == 0:
        # 1 digit number - i.e starts and finishes within the first column
    elif: j == len(schematic.index(i):
                   # The number finishes at the very last column of the line

def is_special_char(char):
    return char.isprintable() and not char.isalnum() and char not in string.whitespace

if __name__ == "__main__":
    main()
