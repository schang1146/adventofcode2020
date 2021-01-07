from copy import deepcopy

# initialize problem variables
data = []
example1 = []
example2 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(list(line.strip()))

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(list(line.strip()))

# function TODO
# time complexity: TODO
# space complexity: TODO
def getAdjacentOccupiedSeatCount(state, row, col):
    output = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= row + i < len(state) and 0 <= col + j < len(state[0]) and not (i == 0 and j == 0):
                if state[row + i][col + j] == '#':
                    output += 1

    return output

# function TODO
# time complexity: TODO
# space complexity: TODO
def getLineOfSightOccupiedSeatCount(state, row, col):
    output = 0

# function TODO
# time complexity: TODO
# space complexity: TODO
def solution1(data):
    currState = deepcopy(data)
    numOccupied = 0

    while True:
        newState = deepcopy(currState)
        for i in range(len(currState)):
            for j in range(len(currState[0])):
                if currState[i][j] == 'L':   # if seat is empty
                    if getAdjacentOccupiedSeatCount(currState, i, j) == 0:
                        newState[i][j] = '#'
                        numOccupied += 1
                elif currState[i][j] == '#':  # if seat is occupied
                    if getAdjacentOccupiedSeatCount(currState, i, j) >= 4:
                        newState[i][j] = 'L'
                        numOccupied -= 1

        if currState == newState:
            break
        currState = deepcopy(newState)

    return numOccupied

# function TODO
# time complexity: TODO
# space complexity: TODO
def solution2(data):
    seats = {}
    adjacencyDict = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '.':
                seats[(f'{i},{j}')] = False
                adjacencyDict[f'{i},{j}'] = []
    for key in seats:
        currRow, currCol = key.split(',')
        currRow = int(currRow)
        currCol = int(currCol)

        for col in range(currCol-1, -1, -1):
            if data[currRow][col] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{currRow},{col}')
                break
        for col in range(currCol+1, len(data[0])):
            if data[currRow][col] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{currRow},{col}')
                break
        for row in range(currRow-1, -1, -1):
            if data[row][currCol] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{row},{currCol}')
                break
        for row in range(currRow+1, len(data)):
            if data[row][currCol] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{row},{currCol}')
                break
        i = 1
        while 0 <= currRow + i < len(data) and 0 <= currCol + i < len(data[0]):
            if data[currRow + i][currCol + i] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{currRow + i},{currCol + i}')
                break
            i += 1
        i = 1
        while 0 <= currRow - i < len(data) and 0 <= currCol - i < len(data[0]):
            if data[currRow - i][currCol - i] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{currRow - i},{currCol - i}')
                break
            i += 1
        i = 1
        while 0 <= currRow + i < len(data) and 0 <= currCol - i < len(data[0]):
            if data[currRow + i][currCol - i] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{currRow + i},{currCol - i}')
                break
            i += 1
        i = 1
        while 0 <= currRow - i < len(data) and 0 <= currCol + i < len(data[0]):
            if data[currRow - i][currCol + i] != '.':
                adjacencyDict[f'{currRow},{currCol}'].append(f'{currRow - i},{currCol + i}')
                break
            i += 1

    numOccupied = 0
    forceExit = 0
    while True:
        newSeats = deepcopy(seats)
        for key in seats.keys():
            ct = 0
            for seat in adjacencyDict[key]:
                if seats[seat] == True:
                    ct += 1
            if ct == 0:
                newSeats[key] = True
                numOccupied += 1
            elif ct >= 5:
                newSeats[key] = False
                numOccupied -= 1
        if seats == newSeats:
            break
        seats = deepcopy(newSeats)
        forceExit += 1
    
    n = 0
    for key in seats.keys():
        if seats[key] == True:
            n += 1

    return n


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 37')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be 26')
    print(f'Part 2 Solution: {solution2(data)}')