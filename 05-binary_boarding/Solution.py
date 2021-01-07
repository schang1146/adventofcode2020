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

# function to get highest seat id on a boarding pass
# returns highest seat id
# time complexity: O(n)
# space complexity: O(1)


def get_highest_seat_id(tickets):
    """Get the highest seat id in a given list of tickets

    Returns highest seat id

    Time Complexity: O(n); where n is the number of given tickets
    Space Complexity: O(1)
    """
    highestId = 0
    for ticket in tickets:
        parsed_ticket = parse_ticket(ticket)
        if parsed_ticket > highestId:
            highestId = parsed_ticket
    return highestId

# function to get your seat id, there are an unknown # of seats that do not exist from beginning and end of the plane
# returns your seat id


def get_your_seat_id(tickets):
    """Get your seat id in a given list of tickets

    Returns the missing ticket id assuming only one ticket is missing from the middle of the given list

    Method 1:
    Time Complexity: O(n)
    Space Complexity: O(1)

    Method 2:
    Time Complexity: O(n logn)
    Space Complexity: O(1)
    """
    # Method 1:
    seen = set()
    highest = -1
    lowest = -1
    for ticket in tickets:
        parsed_ticket = parse_ticket(ticket)
        if lowest == -1 or parsed_ticket < lowest:
            lowest = parsed_ticket
        if highest == -1 or parsed_ticket > highest:
            highest = parsed_ticket
        seen.add(parsed_ticket)

    for id in range(lowest, highest + 1):
        if id not in seen:
            return id

    # Method 2:
    # parsed_tickets = [parse_ticket(ticket) for ticket in tickets]
    # parsed_tickets.sort()
    # for idx in range(len(tickets)):
    #     if parsed_tickets[idx] - idx != parsed_tickets[0]:
    #         return parsed_tickets[0] + idx


def parse_ticket(ticket):
    """Parse seat id from a ticket

    Returns an id by calculating row * 8 + col

    The tickets are assumed to always be the same length where:
        - The first 8 characters specifies row number
        - The last 3 characters specifies col number

    Time Complexity: O(1)
    Space Complexity: O(1)
    """

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


def solution1(data):
    """Finds the highest seat id from the input data"""
    return get_highest_seat_id(data)


def solution2(data):
    """ Finds your seat id from the input data"""
    return get_your_seat_id(data)


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 357')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print('Sample 1 Part 2 Solution: No example given for part 2')
    print(f'Part 2 Solution: {solution2(data)}')
