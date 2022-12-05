def read_file():
    with open('data/day05.txt', 'r') as file:
        lines = file.readlines()
        
    starting_stacks = []
    moves = []

    is_stack = True

    for line in lines:
        cleaned_line = line.replace('\n', '')

        if is_stack:
            is_stack = cleaned_line != ''
            starting_stacks.append(cleaned_line)
        else:
            moves.append(cleaned_line)
            
    starting_stacks.pop() # Removing empty line
    starting_stacks.pop() # Remove line for elves
    
    return starting_stacks, moves

def clean_crate(crate):
    if crate == '   ':
        return ''
    else:
        return crate[1]

def parse_stack_line(line):
    N = len(line)
    count = 0
    
    stacks = []
    while count < N:
        crate = line[count : count + 3]
        stacks.append(clean_crate(crate))
        count += 4
    
    return stacks
