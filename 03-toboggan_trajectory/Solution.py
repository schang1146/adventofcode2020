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


def countTreesEncountered(x, y, terrain):
    """Count trees encountered given a slope

    Returns the number of trees (#) encountered

    Time Complexity: O(n/y) where n is the number of rows in terrain
    Space Complexity: O(1)
    """
    # +x => moves right
    # -x => moves left
    # +y => moves down
    # -y => moves up

    # initialize starting point
    answer = 0
    xCurr = 0
    yCurr = 0

    # iterate through terrain array and count number of times '#' comes up
    while yCurr < len(terrain):
        if terrain[yCurr][xCurr] == '#':
            answer += 1
        # updated coordinates
        xCurr = (xCurr + x) % len(terrain[0])
        yCurr = yCurr + y

    return answer


def solution1(data):
    """Calculates the number of trees encountered for a slope of right 3 and down 1"""
    return countTreesEncountered(3, 1, data)


def solution2(data):
    """Calculates the product of the number of trees hit for different given slopes"""
    a = countTreesEncountered(1, 1, data)
    b = countTreesEncountered(3, 1, data)
    c = countTreesEncountered(5, 1, data)
    d = countTreesEncountered(7, 1, data)
    e = countTreesEncountered(1, 2, data)
    return a * b * c * d * e


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 7')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be 336')
    print(f'Part 2 Solution: {solution2(data)}')
