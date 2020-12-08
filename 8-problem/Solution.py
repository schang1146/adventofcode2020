# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line.strip())

def solution(instructions):
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

def solution2(instructions):
    toSwap = []
    for idx in range(len(instructions)):
        if instructions[idx].split(' ')[0] == 'nop':
            toSwap.append((idx, 'nop'))
        elif instructions[idx].split(' ')[0] == 'jmp':
            toSwap.append((idx, 'jmp'))
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

    return 'not possible'

print(f'Part 1 Solution: {solution(data)}')
print(f'Part 2 Solution: {solution2(data)}')