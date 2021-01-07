# initialize problem variables
data = []
example1 = []
target = 2020

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(int(line.strip()))

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(int(line.strip()))


def two_sum(nums, target):
    """Find two numbers that add up to the target given a list of integers

    Returns a sorted list of two numbers that add to the target
    Returns False if no two numbers could be found

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    output = False
    seen = set()
    for num in nums:
        if target - num in seen:
            output = sorted([(target - num), num])
            break
        else:
            seen.add(num)
    return output


def three_sum(nums, target):
    """Find three numbers that add up to the target given a list of integers
    (Uses two_sum())

    Returns a sorted list of three numbers that add to the target
    Returns False if no three numbers could be found

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    output = False
    for idx in range(len(nums)):
        two_sum_output = two_sum(
            nums[:idx] + nums[idx + 1:], target - nums[idx])
        if two_sum_output:
            return two_sum_output + [nums[idx]]
    return output


def solution1(data, target):
    """Finds the product of the two entries in data that sum up to 2020"""
    answer = 1
    for num in two_sum(data, target):
        answer *= num
    return answer


def solution2(data, target):
    """Finds the product of the three entries in data that sum up to 2020"""
    answer = 1
    for num in three_sum(data, target):
        answer *= num
    return answer


if __name__ == "__main__":

    print(
        f'Sample 1 Part 1 Solution: {solution1(example1, target)} should be 514579')
    print(f'Part 1 Solution: {solution1(data, target)}')
    print()
    print(
        f'Sample 1 Part 2 Solution: {solution2(example1, target)} should be 241861950')
    print(f'Part 2 Solution: {solution2(data, target)}')
