# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line.strip())

# function to find how many trees are in the path given a slope
# returns number of trees encountered
# time complexity:
# space complexity:
def countTreesEncountered(x, y, terrain):
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

print(f'Part 1 Solution: {countTreesEncountered(3, 1, data)}')

a = countTreesEncountered(1, 1, data)
b = countTreesEncountered(3, 1, data)
c = countTreesEncountered(5, 1, data)
d = countTreesEncountered(7, 1, data)
e = countTreesEncountered(1, 2, data)

print(f'Part 2 Solution: {a * b * c * d * e}')