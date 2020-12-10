# initialize problem variables
data = []
example1 = []
example2 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(int(line.strip()))
filename = 'example2.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example2.append(int(line.strip()))

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(int(line.strip()))

# function TODO
# time complexity: TODO
# space complexity: TODO
def solution1(data):
    pass

# function TODO
# time complexity: TODO
# space complexity: TODO
def solution2(data):
    pass

if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be _')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be _')
    print(f'Part 2 Solution: {solution2(data)}')