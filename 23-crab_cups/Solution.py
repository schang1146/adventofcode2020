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


class ListNode():
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode


def addMoreNodes(head, maxVal):
    start = head

    currMax = head.value
    pointer = head.nextNode
    while pointer != start:
        if pointer.value > currMax:
            currMax = pointer.value
        pointer = pointer.nextNode

    pointer = head
    while pointer.nextNode != start:
        pointer = pointer.nextNode

    for num in range(currMax + 1, maxVal + 1):
        pointer.nextNode = ListNode(num)
        pointer = pointer.nextNode

    pointer.nextNode = start

    return head


def buildLinkedList(string):
    head = ListNode(None)
    currentNode = head
    for strNum in string:
        currentNode.nextNode = ListNode(int(strNum))
        currentNode = currentNode.nextNode
    head = head.nextNode
    currentNode.nextNode = head
    return head


def buildLookupTable(string, maxVal=None):
    lookupTable = {}
    currMax = None
    for idx in range(len(string)):
        if idx < len(string) - 1:
            lookupTable[int(string[idx])] = int(string[idx + 1])
        else:
            lookupTable[int(string[idx])] = int(string[0])

        if currMax is None or int(string[idx]) > currMax:
            currMax = int(string[idx])

    if maxVal is not None and maxVal > currMax:
        lookupTable[int(string[-1])] = currMax + 1
        for num in range(currMax + 1, maxVal + 1):
            if num < maxVal:
                lookupTable[num] = num + 1
            else:
                lookupTable[num] = int(string[0])

    return lookupTable


def getNodesAfter1(head):
    outputStr = ""
    while head.value != 1:
        head = head.nextNode
    head = head.nextNode
    while head.value != 1:
        outputStr += str(head.value)
        head = head.nextNode
    return outputStr


def get2NodesAfter1(head):
    while head.value != 1:
        head = head.nextNode

    return [head.nextNode, head.nextNode.nextNode]


def printLinkedList(head):
    outputStr = ""
    start = head
    flag = False
    while head is not None and flag is False:
        outputStr += f"{head.value} -> "
        head = head.nextNode
        if head == start:
            flag = True
    print(outputStr)


def printLookupTable(lookupTable, start=3):
    outputStr = ""
    current = start
    flag = False
    while flag is False:
        outputStr += f"{current} -> "
        current = lookupTable[current]
        if current == start:
            flag = True
    print(outputStr)


def solution1(data, numMoves):
    # build linked list
    head = buildLinkedList(data[0])

    currentCup = head
    for z in range(numMoves):
        left = currentCup.nextNode
        right = currentCup.nextNode.nextNode.nextNode

        # change nextNode pointer of currentCup to "get rid of next 3 cups"
        currentCup.nextNode = right.nextNode

        removedSet = set([currentCup.value, left.value, left.nextNode.value,
                          left.nextNode.nextNode.value])

        # calc target value of destination cup
        targetValue = currentCup.value
        while targetValue in removedSet:
            if targetValue == 1:
                targetValue = 9
            else:
                targetValue -= 1

        # find destination cup
        destinationCup = currentCup
        while destinationCup.value != targetValue:
            destinationCup = destinationCup.nextNode

        # insert the 3 cups after the destination cup
        right.nextNode = destinationCup.nextNode
        destinationCup.nextNode = left

        # change current cup
        currentCup = currentCup.nextNode

    return getNodesAfter1(head)


def solution2(data, numMoves, maxVal):
    # build lookup table
    lookupTable = buildLookupTable(data[0], maxVal)

    currentCup = int(data[0][0])
    for move in range(numMoves):
        left = lookupTable[currentCup]
        right = lookupTable[lookupTable[lookupTable[currentCup]]]

        # calc destination cup
        removedSet = set([currentCup, left, lookupTable[left], right])
        destinationCup = currentCup
        while destinationCup in removedSet:
            if destinationCup == 1:
                destinationCup = maxVal
            else:
                destinationCup -= 1

        lookupTable[currentCup] = lookupTable[right]
        lookupTable[right] = lookupTable[destinationCup]
        lookupTable[destinationCup] = left

        currentCup = lookupTable[currentCup]

    return lookupTable[1] * lookupTable[lookupTable[1]]


if __name__ == "__main__":
    print(
        f'Sample 1 Part 1 Solution: {solution1(example1, 10)} should be 92658374')
    print(
        f'Sample 2 Part 1 Solution: {solution1(example1, 100)} should be 67384529')
    print(f'Part 1 Solution: {solution1(data, 100)}')
    print()
    print(
        f'Sample 1 Part 2 Solution: {solution2(example1, 10000000, 1000000)} should be 149245887792')
    print(f'Part 2 Solution: {solution2(data, 10000000, 1000000)}')
