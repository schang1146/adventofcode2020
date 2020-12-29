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


def getBlackTiles(flips):
    blackTileCoords = set()
    for flip in flips:
        coords = [0, 0]
        pointer = 0
        while pointer < len(flip):
            if flip[pointer] == 's':
                coords[1] -= 1
                if flip[pointer + 1] == 'e':
                    coords[0] += 1
                pointer += 2
            elif flip[pointer] == 'n':
                coords[1] += 1
                if flip[pointer + 1] == 'w':
                    coords[0] -= 1
                pointer += 2
            elif flip[pointer] == 'e':
                coords[0] += 1
                pointer += 1
            elif flip[pointer] == 'w':
                coords[0] -= 1
                pointer += 1

        if str(coords) in blackTileCoords:
            blackTileCoords.remove(str(coords))
        else:
            blackTileCoords.add(str(coords))

    return blackTileCoords


def runArtExhibit(blacks, days):
    for _ in range(days):
        oldState = blacks.copy()
        neighbors = {}
        for tile in oldState:
            tileCoords = tile[1:-1].split(',')
            tileCoords[0] = int(tileCoords[0].strip())
            tileCoords[1] = int(tileCoords[1].strip())
            numBlackNeighbors = 0

            coordE = [tileCoords[0] + 1, tileCoords[1]]
            coordW = [tileCoords[0] - 1, tileCoords[1]]
            coordNE = [tileCoords[0], tileCoords[1] + 1]
            coordNW = [tileCoords[0] - 1, tileCoords[1] + 1]
            coordSE = [tileCoords[0] + 1, tileCoords[1] - 1]
            coordSW = [tileCoords[0], tileCoords[1] - 1]

            # e
            if str(coordE) in oldState:
                numBlackNeighbors += 1
            else:
                if str(coordE) in neighbors:
                    neighbors[str(coordE)] += 1
                else:
                    neighbors[str(coordE)] = 1
            # w
            if str(coordW) in oldState:
                numBlackNeighbors += 1
            else:
                if str(coordW) in neighbors:
                    neighbors[str(coordW)] += 1
                else:
                    neighbors[str(coordW)] = 1
            # ne
            if str(coordNE) in oldState:
                numBlackNeighbors += 1
            else:
                if str(coordNE) in neighbors:
                    neighbors[str(coordNE)] += 1
                else:
                    neighbors[str(coordNE)] = 1
            # nw
            if str(coordNW) in oldState:
                numBlackNeighbors += 1
            else:
                if str(coordNW) in neighbors:
                    neighbors[str(coordNW)] += 1
                else:
                    neighbors[str(coordNW)] = 1
            # se
            if str(coordSE) in oldState:
                numBlackNeighbors += 1
            else:
                if str(coordSE) in neighbors:
                    neighbors[str(coordSE)] += 1
                else:
                    neighbors[str(coordSE)] = 1
            # sw
            if str(coordSW) in oldState:
                numBlackNeighbors += 1
            else:
                if str(coordSW) in neighbors:
                    neighbors[str(coordSW)] += 1
                else:
                    neighbors[str(coordSW)] = 1

            if numBlackNeighbors == 0 or numBlackNeighbors > 2:
                blacks.remove(tile)

        for tile in neighbors:
            if neighbors[tile] == 2:
                blacks.add(tile)

    return blacks


def solution1(data):
    blackTileCoords = getBlackTiles(data)
    return len(blackTileCoords)


def solution2(data):
    blackTileCoords = getBlackTiles(data)
    blackTileCoords = runArtExhibit(blackTileCoords, 100)
    return len(blackTileCoords)


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 10')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be 2208')
    print(f'Part 2 Solution: {solution2(data)}')
