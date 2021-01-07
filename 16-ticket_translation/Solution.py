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


def parseData(data):
    # 1st section before 1st empty line
    descriptions = {}
    for idx in range(len(data)):
        if data[idx] == '':
            break
        else:
            descriptor, bounds = data[idx].split(': ')
            bounds = bounds.split(' or ')
            for bound in bounds:
                low, high = bound.split('-')
                if descriptor in descriptions:
                    descriptions[descriptor].append([int(low), int(high)])
                else:
                    descriptions[descriptor] = [[int(low), int(high)]]

    # 2nd section between 1st empty line and 2nd empty line
    yourTicket = data[idx+2].split(',')

    # 3rd section after 2nd empty line
    nearbyTickets = []
    for idx in range(idx+5, len(data)):
        nearbyTickets.append(data[idx].split(','))

    return [descriptions, yourTicket, nearbyTickets]


def getTargetInfo(yourTicket, validNearbyTickets, target, descriptions):
    descriptorToRowIdx = {}
    for descriptor in descriptions:
        descriptorToRowIdx[descriptor] = len(descriptorToRowIdx)

    matrix = [[0 for _ in range(len(descriptorToRowIdx))]
              for _ in range(len(descriptorToRowIdx))]

    for descriptor in descriptions:
        for col in range(len(validNearbyTickets[0])):
            isDescriptorValidForField = True
            for row in range(len(validNearbyTickets)):
                if not isNumValidForDescription(int(validNearbyTickets[row][col]), descriptor, descriptions):
                    isDescriptorValidForField = False
                    break
            if isDescriptorValidForField:
                matrix[descriptorToRowIdx[descriptor]][col] = 1

    # solve matrix - possibly horribly inefficient
    changeMade = True
    rowsFixed = set()
    while changeMade:
        changeMade = False
        for row in range(len(matrix)):
            if row not in rowsFixed:
                idxOfValid = []
                for col in range(len(matrix[0])):
                    if matrix[row][col] == 1:
                        idxOfValid.append(col)

                if len(idxOfValid) == 1:
                    changeMade = True
                    rowsFixed.add(row)
                    for rowDel in range(len(matrix)):
                        if rowDel != row:
                            matrix[rowDel][idxOfValid[0]] = 0

    output = {}
    for descriptor in descriptorToRowIdx.keys():
        if target in descriptor:
            for field in range(len(yourTicket)):
                if matrix[descriptorToRowIdx[descriptor]][field]:
                    output[descriptor] = int(yourTicket[field])

    return output


def getTicketScanningErrorRate(descriptions, nearbyTickets):
    output = 0
    for ticket in nearbyTickets:
        for num in ticket:
            if not isNumValidForTicket(num, descriptions):
                output += int(num)

    return output


def getValidNearbyTickets(descriptions, nearbyTickets):
    validNearbyTickets = []
    for ticket in nearbyTickets:
        isValid = True
        for num in ticket:
            if not isNumValidForTicket(num, descriptions):
                isValid = False
                break
        if isValid:
            validNearbyTickets.append(ticket)
    return validNearbyTickets


def isNumValidForTicket(num, descriptions):
    for descriptor in descriptions.keys():
        for bound in descriptions[descriptor]:
            if bound[0] <= int(num) <= bound[1]:
                return True
    return False


def isNumValidForDescription(num, descriptor, descriptions):
    for bound in descriptions[descriptor]:
        if bound[0] <= num <= bound[1]:
            return True
    return False


def solution1(data):
    descriptions, yourTicket, nearbyTickets = parseData(data)
    return getTicketScanningErrorRate(descriptions, nearbyTickets)


def solution2(data, target):
    descriptions, yourTicket, nearbyTickets = parseData(data)
    validNearbyTickets = getValidNearbyTickets(descriptions, nearbyTickets)
    departureInfo = getTargetInfo(
        yourTicket, validNearbyTickets, target, descriptions)
    output = 1
    for field in departureInfo:
        output *= departureInfo[field]
    return output


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 71')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(
        f'Sample 1 Part 2 Solution: {solution2(example2, "class")} should be 12')
    print(f'Part 2 Solution: {solution2(data, "departure")}')
