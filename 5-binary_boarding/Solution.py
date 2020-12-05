# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line)

# function to get highest seat id on a boarding pass
# returns highest seat id
# time complexity: O(n)
# space complexity: O(1)
def getHighestSeatId(tickets):
    highestId = 0
    for ticket in tickets:
        parsedTicket = parseTicket(ticket)
        if parsedTicket > highestId:
            highestId = parsedTicket
    return highestId

# function to get your seat id, there are an unknown # of seats that do not exist from beginning and end of the plane
# returns your seat id
# time complexity: O(1)
# space complexity: O(1)
def getYourSeatId(tickets):
    seen = set()
    highest = -1
    lowest = -1
    for ticket in tickets:
        parsedTicket = parseTicket(ticket)
        if lowest == -1 or parsedTicket < lowest:
            lowest = parsedTicket
        if highest == -1 or parsedTicket > highest:
            highest = parsedTicket
        seen.add(parsedTicket)
    
    for id in range(lowest, highest + 1):
        if id not in seen:
            return id

# function to parse seat id on a boarding pass
# returns seat id
# time complexity: O(1)
# space complexity: O(1)
def parseTicket(ticket):
    # tickets are always the same length
    # the first 8 characters specifies row #
    # the last 3 characters specifies col #

    # there are 128 rows numbered from 0 thru 127
    # 'F' -> take the lower half
    # 'B' -> take the upper half
    rowLow = 0
    rowHigh = 127
    for char in ticket[:7]:
        if char == 'F':     # lower half
            rowHigh = (rowLow + rowHigh + 1) // 2
        elif char == 'B':   # upper half
            rowLow = (rowLow + rowHigh + 1) // 2

    # there are 8 columns numbered from 0 thru 7
    # 'L' -> take the lower half
    # 'R' -> take the upper half
    colLow = 0
    colHigh = 7
    for char in ticket[7:]:
        if char == 'L':     # lower half
            colHigh = (colLow + colHigh + 1) // 2
        elif char == 'R':   # upper half
            colLow = (colLow + colHigh + 1) // 2

    # rowLow == rowHigh and colLow == colHigh
    # seatId = row * 8 + col
    return rowLow * 8 + colLow

print(f"Part 1 Solution: {getHighestSeatId(data)}")

print(f"Part 2 Solution: {getYourSeatId(data)}")