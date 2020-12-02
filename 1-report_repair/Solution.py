# initialize problem variables
data = []
target = 2020

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(int(line))

# function to find two numbers that add up to a target number given a nums list and a target int
# returns False if no pair could be found
# time complexity: O(n)
# space complexity: O(n)
def twoSum(nums, target):
    output = False
    seen = set()
    for num in nums:
        if target - num in seen:
            output = sorted([(target - num), num])
            break
        else:
            seen.add(num)
    file.close()
    return output

# print part 1 solution
answer = 1
for num in twoSum(data, target):
    answer *= num
print(f'Part 1 Solution: {answer}')

# function to find three numbers that add up to a target number given a nums list and a target int
# returns False if no triplet could be found
# time complexity: O(n^2)
# space complexity: O(n)
def threeSum(nums, target):
    output = -1
    for idx in range(len(nums)):
        two_sum_output = twoSum(nums[:idx] + nums[idx + 1:], target - nums[idx])
        if two_sum_output:
            return two_sum_output + [nums[idx]]

# print part 2 solution
answer = 1
for num in threeSum(data, target):
    answer *= num
print(f'Part 2 Solution: {answer}')