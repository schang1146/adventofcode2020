# initialize problem variables
data = []
example1 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(line.strip())

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())


def cycle3d(active):
    newActiveCubes = set(active)

    cubesWithActiveNeighbor = {}

    for cube in active:
        row, col, zed = cube.split(',')
        row = int(row)
        col = int(col)
        zed = int(zed)

        numActiveNeighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if not (i == 0 and j == 0 and k == 0):
                        neighbor = f'{row-i},{col-j},{zed-k}'
                        if neighbor in active:
                            numActiveNeighbors += 1
                        else:
                            if neighbor in cubesWithActiveNeighbor:
                                cubesWithActiveNeighbor[neighbor] += 1
                            else:
                                cubesWithActiveNeighbor[neighbor] = 1

        if numActiveNeighbors < 2 or numActiveNeighbors > 3:
            newActiveCubes.remove(cube)

    for cube in cubesWithActiveNeighbor:
        if cubesWithActiveNeighbor[cube] == 3:
            newActiveCubes.add(cube)

    return newActiveCubes


def cycle4d(active):
    newActiveCubes = set(active)

    cubesWithActiveNeighbor = {}

    for cube in active:
        a, b, c, d = cube.split(',')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        numActiveNeighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if not (i == 0 and j == 0 and k == 0 and l == 0):
                            neighbor = f'{a-i},{b-j},{c-k},{d-l}'
                            if neighbor in active:
                                numActiveNeighbors += 1
                            else:
                                if neighbor in cubesWithActiveNeighbor:
                                    cubesWithActiveNeighbor[neighbor] += 1
                                else:
                                    cubesWithActiveNeighbor[neighbor] = 1

        if numActiveNeighbors < 2 or numActiveNeighbors > 3:
            newActiveCubes.remove(cube)

    for cube in cubesWithActiveNeighbor:
        if cubesWithActiveNeighbor[cube] == 3:
            newActiveCubes.add(cube)

    return newActiveCubes


def solution1(data, nCycles):
    active = set()  # coordinates saved as string 'row,col,zed'
    for col in range(len(data[0])):
        for row in range(len(data)):
            if data[row][col] == '#':
                active.add(f'{row},{col},{0}')

    for currentCycle in range(nCycles):
        active = cycle3d(active)

    return len(active)


def solution2(data, nCycles):
    active = set()  # coordinates saved as string 'a,b,c,d'
    for b in range(len(data[0])):
        for a in range(len(data)):
            if data[a][b] == '#':
                active.add(f'{a},{b},{0},{0}')

    for currentCycle in range(nCycles):
        active = cycle4d(active)

    return len(active)


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1, 6)} should be 112')
    print(f'Part 1 Solution: {solution1(data, 6)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1, 6)} should be 848')
    print(f'Part 2 Solution: {solution2(data, 6)}')
