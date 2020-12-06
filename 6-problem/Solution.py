# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line)


def solution1(responses):
    seen = set()
    uniqueCount = 0
    for response in responses:
        if response == '\n':
            uniqueCount += len(seen)
            seen = set()
        else:
            response = response.strip()
            for char in response:
                if char not in seen:
                    seen.add(char)
    uniqueCount += len(seen)
    return uniqueCount


def solution2(responses):
    seen = {}
    uniqueCount = 0
    numberOfPeopleInGroup = 0
    for response in responses:
        if response == '\n':
            for key in seen.keys():
                if seen[key] == numberOfPeopleInGroup:
                    uniqueCount += 1
            numberOfPeopleInGroup = 0
            seen = {}
        else:
            numberOfPeopleInGroup += 1
            response = response.strip()
            for char in response:
                if char not in seen:
                    seen[char] = 1
                else:
                    seen[char] += 1
    for key in seen.keys():
        if seen[key] == numberOfPeopleInGroup:
            uniqueCount += 1
    return uniqueCount


print(f'Part 1 Solution: {solution1(data)}')
print(f'Part 2 Solution: {solution2(data)}')
