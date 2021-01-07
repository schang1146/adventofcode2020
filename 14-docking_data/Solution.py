# initialize problem variables
data = []
example1 = []
example2 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(line.strip())
filename = 'example2.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example2.append(line.strip())

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())


def parseMask(mask):
    parsedMask = {}
    for idx in range(len(mask)):
        if mask[-1-idx] != 'X':
            parsedMask[idx] = mask[-1-idx]
    return parsedMask


def applyMask(parsedMask, num):
    binNum = format(num, 'b')
    binNum = list('0' * (36 - len(binNum)) + binNum)
    for key in parsedMask.keys():
        binNum[-key-1] = parsedMask[key]
    return int(''.join(binNum), 2)


def solution1(data):
    mem = {}
    parsedMask = {}

    for instruction in data:
        address, val = instruction.split(' = ')
        if address == 'mask':
            parsedMask = parseMask(val)
        else:
            mem[address] = applyMask(parsedMask, int(val))

    output = 0
    for key in mem.keys():
        output += mem[key]
    return output


def parseMaskv2(mask):
    parsedMask = {}
    for idx in range(len(mask)):
        if mask[-1-idx] != '0':
            parsedMask[idx] = mask[-1-idx]
    return parsedMask


def maskAddress(parsedMask, addr):
    maskedAddr = []
    binAddr = format(int(addr), 'b')
    binListAddr = list('0' * (36 - len(binAddr)) + binAddr)
    for key in parsedMask.keys():
        binListAddr[-1-key] = parsedMask[key]

    if binListAddr[0] == 'X':
        stack = ['0', '1']
    else:
        stack = [binListAddr[0]]
    while len(stack) > 0:
        currAddr = stack.pop(0)

        if len(currAddr) == 36:
            maskedAddr.append(currAddr)
        else:
            if binListAddr[len(currAddr)] == 'X':
                stack.append(currAddr + '1')
                stack.append(currAddr + '0')
            else:
                stack.append(currAddr + binListAddr[len(currAddr)])

    return maskedAddr


def solution2(data):
    mem = {}
    parsedMask = None
    for instruction in data:
        left, right = instruction.split(' = ')
        if left[:4] == 'mask':
            mask = right
            parsedMask = parseMaskv2(mask)
        elif left[:3] == 'mem':
            addr = left[4:-1]
            val = int(right)
            maskedAddr = maskAddress(parsedMask, addr)

            for addr in maskedAddr:
                mem[int(addr, 2)] = val

    output = 0
    for key in mem.keys():
        output += mem[key]
    return output


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 165')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example2)} should be 208')
    print(f'Part 2 Solution: {solution2(data)}')
