# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(int(line.strip()))

# function to return the # of 1-jolt differences multiplied by the
# # of 3-jolt differences
# time complexity: O(n)
# space complexity: O(1)
def solution1(data):
    diffCount = {}
    data.sort()
    # makes sure there's 0-jolt and max+3-jolt elements in the data array
    if data[0] == 0:
        data += [data[-1] + 3]
    else:
        data = [0] + data + [data[-1] + 3]
    for idx in range(1, len(data)):
        diff = data[idx] - data[idx-1]
        if diff not in diffCount:
            diffCount[diff] = 1
        else:
            diffCount[diff] += 1

    return diffCount[1] * diffCount[3]

# function to return the total number of distinct ways to arrange adapters to
# connect the charging outlet 0-jolt to max+3-jolt
# time complexity: O(n)
# space complexity: O(1)
def solution2(data):
    data.sort()
    # makes sure there's 0-jolt and max+3-jolt elements in the data array
    if data[0] == 0:
        data += [data[-1] + 3]
    else:
        data = [0] + data + [data[-1] + 3]

    seen = {data[-1]: 1}

    for idx in range(len(data) - 2, -1, -1):
        currOutput = 0
        currSeen = {}
        for jdx in range(1,4):
            if idx + jdx < len(data):
                if data[idx + jdx] - data[idx] <= 3:
                    currOutput += seen[data[idx + jdx]]
                    currSeen[data[idx + jdx]] = seen[data[idx + jdx]]
        currSeen[data[idx]] = currOutput
        seen = currSeen

    return seen[0]

print(f'Part 1 Solution: {solution1(data)}')

print(f'Part 2 Solution: {solution2(data)}')