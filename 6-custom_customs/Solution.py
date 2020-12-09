# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line)

# function to returns total # of unique answers people said yes to in each group
# time complexity: TODO
# space complexity: TODO
def getUniqueCountPerGroup(responses):
    seen = set()
    uniqueCount = 0
    for response in responses:
        # newline denotes a new group, so add current uniqueCount and reset seen
        if response == '\n':
            uniqueCount += len(seen)
            seen = set()
        else:
            response = response.strip()
            for char in response:
                if char not in seen:
                    seen.add(char)
    # if there was no newline at the end of responses,
    # add the number of elements in seen
    if len(seen) != 0:
        uniqueCount += len(seen)

    return uniqueCount

# function that returns total # of unique answers everyone in each group said yes to
# time complexity: TODO
# space complexity: TODO
def solution2(responses):
    seen = {}
    uniqueCount = 0
    numberOfPeopleInGroup = 0
    for response in responses:
        # newline denotes a new group, so add current uniqueCount and reset seen
        if response == '\n':
            for key in seen.keys():
                # if value for key in seen is equal to the # of people in a group
                # then everyone said yes to it
                if seen[key] == numberOfPeopleInGroup:
                    uniqueCount += 1
            # reset for next group
            numberOfPeopleInGroup = 0
            seen = {}
        # keep track of total people in a group and their responses
        else:
            numberOfPeopleInGroup += 1
            response = response.strip()
            for char in response:
                if char not in seen:
                    seen[char] = 1
                else:
                    seen[char] += 1
    # if there was no newline at the end of responses,
    # add the number of elements in seen
    if len(seen) != 0:
        for key in seen.keys():
            if seen[key] == numberOfPeopleInGroup:
                uniqueCount += 1
                
    return uniqueCount

print(f'Part 1 Solution: {getUniqueCountPerGroup(data)}')

print(f'Part 2 Solution: {solution2(data)}')
