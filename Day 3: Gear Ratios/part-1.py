from queue import Queue
import string

def main():
    queue = Queue() 

    # Thank you Chat-GPT 
    with open("example-input", "r") as f:
           lines = f.readlines() 

    # You could probably do this without making everyline the same length
    max_length = max(len(line) for line in lines)
    # adjust the input so that every line is the same length, no sizing issues between the rows 
    schematic = [list(line.strip().ljust(max_length)) for line in lines]

    for row in schematic:
        for char in row:
            if char.isdigit():
                queue.put(char)
            elif char == '.':
                print()
            elif is_special_char(char):
                print()
                
def is_special_char(char):
    return char.isprintable() and not char.isalnum() and char is not string.whitespace

if __name__ == "__main__":
    main()
