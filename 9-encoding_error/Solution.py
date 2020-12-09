# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(int(line.strip()))

# function to find two numbers in the iterable data struture that adds to the target
# if a pair is found, returns True
# if no pair exists, returns False
# time complexity: O(n)
# space complexity: O(n)
def twoSum(iterable, target):
    seen = set()
    for num in iterable:
        if target - num in seen:
            return True
        else:
            seen.add(num)
    return False

# function that returns the first number from index k to the end that can't be made
# by adding two numbers from k length numbers before it
# if all numbers can be made by adding two previous numbers, returns -1
# time complexity: O(n)
# space complexity: O(1)
def getFirstInvalidPreambleNum(data, preambleLength):
    # initialize preamble
    preamble = set()
    for num in data[:preambleLength]:
        preamble.add(num)

    # check numbers after preamble
    for idx in range(preambleLength, len(data)):
        if not twoSum(data[idx-preambleLength : idx], data[idx]):
            return data[idx]

    return -1

# function that returns the sum of the minimum and maximum number from a window of
# consecutive numbers that adds up to a target
# time complexity: O(n)
# space complexity: O(1)
def getEncryptionWeakness(data):
    target = getFirstInvalidPreambleNum(data, 25)
    left = 0
    currentSum = data[left]

    for right in range(1, len(data)):
        currentSum += data[right]
        
        while currentSum > target:
            currentSum -= data[left]
            left += 1

        if currentSum == target:
            break
    
    smallest = data[left]
    largest = data[left]
    for num in data[left+1:right+1]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest + largest


print(f'Part 1 Solution {getFirstInvalidPreambleNum(data, 25)}')

print(f'Part 2 Solution {getEncryptionWeakness(data)}')