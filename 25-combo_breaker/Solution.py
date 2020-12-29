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


def getLoopSize(subjectNum, cardPubKey, doorPubKey):
    card = 1
    cardLoopSize = 0
    door = 1
    doorLoopSize = 0

    while card != cardPubKey:
        card = transformStep(subjectNum, card)
        cardLoopSize += 1

    while door != doorPubKey:
        door = transformStep(subjectNum, door)
        doorLoopSize += 1

    return [cardLoopSize, doorLoopSize]


def transformLoop(subjectNum, loopSize):
    output = 1
    for _ in range(loopSize):
        output *= subjectNum
        output %= 20201227
    return output


def transformStep(subjectNum, currentNum):
    return (currentNum * subjectNum) % 20201227


def solution1(data):
    cardPubKey = int(data[0])
    doorPubKey = int(data[1])
    # print(f'cardPubKey: {cardPubKey} | doorPubKey: {doorPubKey}')

    cardLoopSize, doorLoopSize = getLoopSize(
        7, cardPubKey, doorPubKey)
    # print(f'cardLoopSize: {cardLoopSize} | doorLoopSize: {doorLoopSize}')

    cardEncKey = transformLoop(doorPubKey, cardLoopSize)
    # doorEncKey = transformLoop(cardPubKey, doorLoopSize)
    # print(f'cardEncKey: {cardEncKey} | doorEncKey: {doorEncKey}')

    return cardEncKey


def solution2(data):
    pass


if __name__ == "__main__":

    print(
        f'Sample 1 Part 1 Solution: {solution1(example1)} should be 14897079')
    print(f'Part 1 Solution: {solution1(data)}')
    # print()
    # print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be _')
    # print(f'Part 2 Solution: {solution2(data)}')
