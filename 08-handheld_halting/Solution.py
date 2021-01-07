# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line.strip())

# function to run through instructions and exits either if it hits the end or repeats
# time complexity: O(n)
# space complexity: O(n)
def runProgramExitOnRepeat(instructions):
    seen = set()
    accumulator = 0
    processCounter = 0
    while processCounter != len(instructions) - 1:
        op, arg = instructions[processCounter].split(' ')
        if processCounter in seen:
            break
        else:
            seen.add(processCounter)
            if op == 'nop':
                processCounter += 1
            elif op == 'acc':
                if arg[0] == '+':
                    arg = int(arg[1:])
                elif arg[0] == '-':
                    arg = int(arg[1:]) * -1
                accumulator += arg
                processCounter += 1
            elif op == 'jmp':
                if arg[0] == '+':
                    arg = int(arg[1:])
                elif arg[0] == '-':
                    arg = int(arg[1:]) * -1
                processCounter += arg

    return accumulator

# function to find and fix an instruction (either NOP or JMP) and return
# the fixed program's output
# time complexity: O(n^2) TODO: double check later on
# space complexity: O(n) TODO: double check later on
def fixProgramAndRun(instructions):
    # find all possible indices to be swapped
    toSwap = []
    for idx in range(len(instructions)):
        if instructions[idx].split(' ')[0] == 'nop':
            toSwap.append((idx, 'nop'))
        elif instructions[idx].split(' ')[0] == 'jmp':
            toSwap.append((idx, 'jmp'))

    # check each index found and see if it runs to the end of the instructions
    for swapInfo in toSwap:
        idx, normalInstruction = swapInfo
        endedEarly = False

        seen = set()
        accumulator = 0
        processCounter = 0
        while processCounter != len(instructions) - 1:
            op, arg = instructions[processCounter].split(' ')
            if processCounter in seen:
                endedEarly = True
                break
            else:
                seen.add(processCounter)
                if op == 'nop':
                    if processCounter == idx:
                        if arg[0] == '+':
                            arg = int(arg[1:])
                        elif arg[0] == '-':
                            arg = int(arg[1:]) * -1
                        processCounter += arg
                    else:
                        processCounter += 1
                elif op == 'acc':
                    if arg[0] == '+':
                        arg = int(arg[1:])
                    elif arg[0] == '-':
                        arg = int(arg[1:]) * -1
                    accumulator += arg
                    processCounter += 1
                elif op == 'jmp':
                    if processCounter == idx:
                        processCounter += 1
                    else:
                        if arg[0] == '+':
                            arg = int(arg[1:])
                        elif arg[0] == '-':
                            arg = int(arg[1:]) * -1
                        processCounter += arg
        
        if not endedEarly:
            return accumulator

    # if instructions always ends early, return -1
    return -1

print(f'Part 1 Solution: {runProgramExitOnRepeat(data)}')

print(f'Part 2 Solution: {fixProgramAndRun(data)}')