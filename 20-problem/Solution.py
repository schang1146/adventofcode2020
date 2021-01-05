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

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())


def getImageFromNeighbors(neighbors):
    sizeOfImage = int(len(neighbors) ** (1/2))
    image = [['None' for _ in range(sizeOfImage)] for _ in range(sizeOfImage)]
    idUsed = set()

    for row in range(len(image)):
        for col in range(len(image[0])):
            numberOfNeighbors = 4
            if row == 0 or row == len(image) - 1:
                numberOfNeighbors -= 1
            if col == 0 or col == len(image[0]) - 1:
                numberOfNeighbors -= 1

            requiredNeighbors = set()
            if row > 0:
                requiredNeighbors.add(image[row-1][col])
            if col > 0:
                requiredNeighbors.add(image[row][col-1])

            nextValidNeighbor = getNextValidNeighbor(neighbors,
                                                     numberOfNeighbors, requiredNeighbors, idUsed)
            image[row][col] = nextValidNeighbor
            idUsed.add(nextValidNeighbor)

    return image


def getNeighbors(tileId, walls):
    tileIdWallCombinations = set()
    for wall in walls[tileId]:
        tileIdWallCombinations.add(wall)
        tileIdWallCombinations.add(wall[::-1])

    neighbors = set()
    for otherTileId in walls:
        if otherTileId != tileId:
            for otherWall in walls[otherTileId]:
                if otherWall in tileIdWallCombinations:
                    neighbors.add(otherTileId)
                    break

    return neighbors


def getNextValidNeighbor(neighbors, numberOfNeighbors, requiredNeighbors, invalidNeighbors):
    for tileId in neighbors:
        if tileId not in invalidNeighbors and len(neighbors[tileId]) == numberOfNeighbors:
            isValid = True
            for required in requiredNeighbors:
                if required not in neighbors[tileId]:
                    isValid = False
                    break
            if isValid:
                return tileId


def getNumberOfHashesNotPartOfSeaMonster(image):
    totalNumberOfHashes = 0
    tailCoordsToCheck = set()
    for row in range(len(image)):
        for col in range(len(image)):
            if image[row][col] == '#':
                if row >= 1 and row <= len(image) - 2 and col <= len(image[0]) - 20:
                    tailCoordsToCheck.add(f'{row},{col}')
                totalNumberOfHashes += 1

    numberOfSeaMonsters = 0
    iteration = 1
    while numberOfSeaMonsters == 0:
        for coord in tailCoordsToCheck:
            row, col = coord.split(',')
            row = int(row)
            col = int(col)
            if isSeaMonster(row, col, image):
                numberOfSeaMonsters += 1

        if numberOfSeaMonsters == 0:
            if iteration % 4 != 0:
                image = rotate(image, 90)
            else:
                image = flip(image, 'h')

        iteration += 1

    return totalNumberOfHashes - (numberOfSeaMonsters * 15)


def isSeaMonster(row, col, image):
    monsterForm = [
        (0, 0),
        (1, 1),
        (1, 4),
        (0, 5),
        (0, 6),
        (1, 7),
        (1, 10),
        (0, 11),
        (0, 12),
        (1, 13),
        (1, 16),
        (0, 17),
        (-1, 18),
        (0, 18),
        (0, 19),
    ]
    for offset in monsterForm:
        rowOffset, colOffset = offset
        if image[row + rowOffset][col + colOffset] != '#':
            return False
    return True


def getTilesFromData(data):
    tiles = {}
    for line in data:
        if line[0:4] == 'Tile':
            tileId = line.split(' ')[1][:-1]
            tiles[tileId] = []
        elif line != '':
            tiles[tileId].append(line)
    return tiles


def getWallsFromTiles(tiles):
    walls = {}
    for tileId in tiles:
        currentTile = tiles[tileId]
        walls[tileId] = []
        walls[tileId].append(currentTile[0])
        walls[tileId].append(currentTile[-1])
        rightWall = ''
        leftWall = ''
        for row in range(len(currentTile)):
            rightWall += currentTile[row][-1]
            leftWall += currentTile[row][0]
        walls[tileId].append(leftWall)
        walls[tileId].append(rightWall)
    return walls


def printImageById(image):
    for row in image:
        print(row)


def getFinalImageByTile(image, tiles):

    for row in range(len(image) - 1):
        for col in range(len(image[0])):
            currentTileId = image[row][col]
            nextTileId = image[row+1][col]
            currentTile = tiles[currentTileId]
            nextTile = tiles[nextTileId]

            # print(
            #     f'currentTileId = {currentTileId} | nextTileId = {nextTileId}')

            currentTileSides = {}
            nextTileSides = {}

            currentTileSides[currentTile[0]] = 'n'
            currentTileSides[currentTile[-1]] = 's'
            nextTileSides[nextTile[0]] = 'n'
            nextTileSides[nextTile[-1]] = 's'
            currentEastKey = ''
            currentWestKey = ''
            nextEastKey = ''
            nextWestKey = ''
            for sideRowIdx in range(len(currentTile)):
                currentEastKey += (currentTile[sideRowIdx][-1])
                currentWestKey += (currentTile[sideRowIdx][0])
                nextEastKey += (nextTile[sideRowIdx][-1])
                nextWestKey += (nextTile[sideRowIdx][0])
            currentTileSides[currentEastKey] = 'e'
            currentTileSides[currentWestKey] = 'w'
            nextTileSides[nextEastKey] = 'e'
            nextTileSides[nextWestKey] = 'w'

            # print(f'currentTileSides = {currentTileSides}')
            # print(f'nextTileSides = {nextTileSides}')

            for nextTileSide in nextTileSides.keys():
                if nextTileSide in currentTileSides:
                    if row == 0:
                        if currentTileSides[nextTileSide] == 'n':
                            tiles[currentTileId] = rotate(
                                tiles[currentTileId], 180)
                        elif currentTileSides[nextTileSide] == 'e':
                            tiles[currentTileId] = rotate(
                                tiles[currentTileId], 90)
                        elif currentTileSides[nextTileSide] == 's':
                            pass
                        elif currentTileSides[nextTileSide] == 'w':
                            tiles[currentTileId] = rotate(
                                tiles[currentTileId], -90)

                    if nextTileSides[nextTileSide] == 'n':
                        pass
                    elif nextTileSides[nextTileSide] == 'e':
                        tiles[nextTileId] = rotate(tiles[nextTileId], -90)
                    elif nextTileSides[nextTileSide] == 's':
                        tiles[nextTileId] = rotate(tiles[nextTileId], 180)
                    elif nextTileSides[nextTileSide] == 'w':
                        tiles[nextTileId] = rotate(tiles[nextTileId], 90)

                elif nextTileSide[::-1] in currentTileSides:
                    if row == 0:
                        if currentTileSides[nextTileSide[::-1]] == 'n':
                            tiles[currentTileId] = rotate(
                                tiles[currentTileId], 180)
                        elif currentTileSides[nextTileSide[::-1]] == 'e':
                            tiles[currentTileId] = rotate(
                                tiles[currentTileId], 90)
                        elif currentTileSides[nextTileSide[::-1]] == 's':
                            pass
                        elif currentTileSides[nextTileSide[::-1]] == 'w':
                            tiles[currentTileId] = rotate(
                                tiles[currentTileId], -90)

                    if nextTileSides[nextTileSide] == 'n':
                        pass
                    elif nextTileSides[nextTileSide] == 'e':
                        tiles[nextTileId] = rotate(tiles[nextTileId], -90)
                    elif nextTileSides[nextTileSide] == 's':
                        tiles[nextTileId] = rotate(tiles[nextTileId], 180)
                    elif nextTileSides[nextTileSide] == 'w':
                        tiles[nextTileId] = rotate(tiles[nextTileId], 90)

            if tiles[currentTileId][-1] == tiles[nextTileId][0][::-1]:
                tiles[nextTileId] = flip(tiles[nextTileId], 'v')

    for col in range(len(image[0]) - 1):
        currentTileId = image[0][col]
        nextTileId = image[0][col+1]
        currentTile = tiles[currentTileId]
        nextTile = tiles[nextTileId]

        currentTileSides = {}
        nextTileSides = {}

        currentEastKey = ''
        currentWestKey = ''
        nextEastKey = ''
        nextWestKey = ''
        for sideRowIdx in range(len(currentTile)):
            currentEastKey += (currentTile[sideRowIdx][-1])
            currentWestKey += (currentTile[sideRowIdx][0])
            nextEastKey += (nextTile[sideRowIdx][-1])
            nextWestKey += (nextTile[sideRowIdx][0])
        currentTileSides[currentEastKey] = 'e'
        currentTileSides[currentWestKey] = 'w'
        nextTileSides[nextEastKey] = 'e'
        nextTileSides[nextWestKey] = 'w'

        for currentTileSide in currentTileSides:
            for nextTileSide in nextTileSides:
                if currentTileSide == nextTileSide:
                    currentSide = currentTileSides[currentTileSide]
                    nextSide = nextTileSides[nextTileSide]

                    if currentSide == 'w' and nextSide == 'w':
                        for fRow in range(len(image)):
                            tileIdToFlip1 = image[fRow][col]
                            tiles[tileIdToFlip1] = flip(
                                tiles[tileIdToFlip1], 'v')
                    elif currentSide == 'w' and nextSide == 'e':
                        for fRow in range(len(image)):
                            tileIdToFlip1 = image[fRow][col]
                            tiles[tileIdToFlip1] = flip(
                                tiles[tileIdToFlip1], 'v')
                            tileIdToFlip2 = image[fRow][col+1]
                            tiles[tileIdToFlip2] = flip(
                                tiles[tileIdToFlip2], 'v')
                    elif currentSide == 'e' and nextSide == 'w':
                        pass
                    elif currentSide == 'e' and nextSide == 'e':
                        for fRow in range(len(image)):
                            tileIdToFlip2 = image[fRow][col+1]
                            tiles[tileIdToFlip2] = flip(
                                tiles[tileIdToFlip2], 'v')

    # print("IMAGE BEFORE REMOVING FRAMES:==========(START)")
    # cCol = 0
    # for cRow in range(len(image)):
    #     id0 = image[cRow][cCol+0]
    #     id1 = image[cRow][cCol+1]
    #     id2 = image[cRow][cCol+2]
    #     id3 = image[cRow][cCol+3]
    #     id4 = image[cRow][cCol+4]
    #     id5 = image[cRow][cCol+5]
    #     id6 = image[cRow][cCol+6]
    #     id7 = image[cRow][cCol+7]
    #     id8 = image[cRow][cCol+8]
    #     id9 = image[cRow][cCol+9]
    #     id10 = image[cRow][cCol+10]
    #     id11 = image[cRow][cCol+11]
    #     for idx in range(len(tiles[id1])):
    #         print(
    #             f'{tiles[id0][idx]}  {tiles[id1][idx]}  {tiles[id2][idx]}  {tiles[id3][idx]}  {tiles[id4][idx]}  {tiles[id5][idx]}')
    #     if cRow < len(image) - 1:
    #         print()
    # print("IMAGE BEFORE REMOVING FRAMES:==========(END)")

    finalImageSize = len(image) * (len(tiles[image[0][0]]) - 2)
    finalImage = ['' for _ in range(finalImageSize)]
    rowOffset = 0
    for row in range(len(image)):
        if row > 0:
            rowOffset += len(tiles[image[0][0]]) - 2
        for col in range(len(image[0])):
            currentTileId = image[row][col]
            currentTile = tiles[currentTileId]

            currentTile = currentTile[1:-1]

            for tileRowIdx in range(len(currentTile)):
                finalImage[rowOffset +
                           tileRowIdx] += currentTile[tileRowIdx][1:-1]

    # print("IMAGE AFTER REMOVING FRAMES:==========(START)")
    # for cRow in range(len(finalImage)):
    #     print(finalImage[cRow])
    # print("IMAGE AFTER REMOVING FRAMES:==========(END)")

    return finalImage


def printTile(tile):
    for row in tile:
        print(row)


def flip(tile, flipDirection):
    if flipDirection in set(['h', 'horiz', 'horizontal']):
        for idx in range(len(tile) // 2):
            tile[idx], tile[-idx-1] = tile[-idx-1], tile[idx]
    elif flipDirection in set(['v', 'vert', 'vertical']):
        for idx in range(len(tile)):
            tile[idx] = tile[idx][::-1]
    return tile


def rotate(tile, deg):
    # POSITIVE == CLOCKWISE
    for row in range(len(tile)):
        tile[row] = list(tile[row])
    if deg == 90 or deg == -270:
        for layer in range(len(tile) // 2):
            sizeOfLayer = len(tile) - (2 * layer)
            for I in range(sizeOfLayer-1):
                temp = tile[0 + layer][0 + layer + I]
                tile[0 + layer][0 + layer +
                                I] = tile[len(tile) - 1 - layer - I][0 + layer]
                tile[len(tile) - 1 - layer - I][0 + layer] = tile[len(tile) -
                                                                  1 - layer][len(tile) - 1 - layer - I]
                tile[len(tile) - 1 - layer][len(tile) - 1 - layer -
                                            I] = tile[0 + layer + I][len(tile) - 1 - layer]
                tile[0 + layer + I][len(tile) - 1 - layer] = temp
    elif deg == 180 or deg == -180:
        tile = rotate(rotate(tile, 90), 90)
    elif deg == 270 or deg == -90:
        for layer in range(len(tile) // 2):
            sizeOfLayer = len(tile) - (2 * layer)
            for I in range(sizeOfLayer-1):
                temp = tile[0 + layer][0 + layer + I]
                tile[0 + layer][0 + layer + I] = tile[0 +
                                                      layer + I][len(tile) - 1 - layer]
                tile[0 + layer + I][len(tile) - 1 - layer] = tile[len(tile) -
                                                                  1 - layer][len(tile) - 1 - layer - I]
                tile[len(tile) - 1 - layer][len(tile) - 1 - layer -
                                            I] = tile[len(tile) - 1 - layer - I][0 + layer]
                tile[len(tile) - 1 - layer - I][0 + layer] = temp
    for row in range(len(tile)):
        tile[row] = ''.join(tile[row])
    return tile


def debug(currentState):
    for row in range(len(currentState)):
        currentState[row] = ''.join(currentState[row])
    printTile(currentState)
    print()


def solution1(data):
    tiles = getTilesFromData(data)

    walls = getWallsFromTiles(tiles)

    output = 1
    for tileId in walls:
        if len(getNeighbors(tileId, walls)) == 2:
            output *= int(tileId)

    return output


def solution2(data):
    tiles = getTilesFromData(data)

    walls = getWallsFromTiles(tiles)

    neighbors = {}
    for tileId in tiles:
        neighbors[tileId] = getNeighbors(tileId, walls)

    image = getImageFromNeighbors(neighbors)
    # test = []
    # for row in range(len(image)):
    #     for col in range(len(image[0])):
    #         if row == 0 or col == 0 or row == len(image) - 1 or col == len(image[0]) - 1:
    #             test.append(image[row][col])
    # print(sorted(test))

    finalImage = getFinalImageByTile(image, tiles)

    return getNumberOfHashesNotPartOfSeaMonster(finalImage)


if __name__ == "__main__":

    print(
        f'Sample 1 Part 1 Solution: {solution1(example1)} should be 20899048083289')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be 273')
    print(f'Part 2 Solution: {solution2(data)}')
