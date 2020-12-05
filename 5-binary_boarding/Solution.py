# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line)

def solution(tickets):
    highestId = 0
    for ticket in tickets:
        parsedTicket = parseTicket(ticket)
        if parsedTicket > highestId:
            highestId = parsedTicket
    return highestId

def parseTicket(ticket):
    low = 0
    high = 127
    for char in ticket[:7]:
        if char == 'F':     # lower half
            high = (low + high + 1) // 2
        elif char == 'B':   # upper half
            low = (low + high + 1) // 2

    l = 0
    h = 7
    for char in ticket[7:]:
        if char == 'L':     # lower half
            h = (l + h + 1) // 2
        elif char == 'R':   # upper half
            l = (l + h + 1) // 2

    return low * 8 + l

def solution2(tickets):
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

print(parseTicket('FBFBBFFRLR'))

print(f"Part 1 Solution: {solution(data)}")



print(f"Part 2 Solution: {solution2(data)}")