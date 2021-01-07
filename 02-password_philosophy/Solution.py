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


def is_valid_password_ver1(x, y, letter, password):
    """Checks if the password passed in is valid or not according to part 1's rules

    A password is valid if it contains the required letter between x and y number of occurrences (inclusive)

    Time Complexity: O(k); where k is the total number of characters in the password
    Space Complexity: O(1)
    """
    count = 0
    for char in password:
        if char == letter:
            count += 1
    if count >= x and count <= y:
        return True
    return False


def is_valid_password_ver2(x, y, letter, password):
    """Checks if the password passed in is valid or not according to part 2's rules

    A password is valid if only one position x or y is the required letter (XOR)
    (x and y counts starting with 1, NOT 0)

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    letterAtX = False
    letterAtY = False

    if x <= len(password):
        if password[x-1] == letter:
            letterAtX = True

    if y <= len(password):
        if password[y-1] == letter:
            letterAtY = True

    if letterAtX ^ letterAtY:
        return True
    return False


def parse_line_in_data(line):
    rules, password = line.split(': ')
    count, letter = rules.split(' ')
    x, y = count.split('-')
    return [x, y, letter, password]


def solution1(data):
    answer = 0
    for line in data:
        [x, y, letter, password] = parse_line_in_data(line)
        x = int(x)
        y = int(y)
        if is_valid_password_ver1(x, y, letter, password):
            answer += 1
    return answer


def solution2(data):
    answer = 0
    for line in data:
        [x, y, letter, password] = parse_line_in_data(line)
        x = int(x)
        y = int(y)
        if is_valid_password_ver2(x, y, letter, password):
            answer += 1
    return answer


if __name__ == "__main__":

    print(
        f'Sample 1 Part 1 Solution: {solution1(example1)} should be 2')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(
        f'Sample 1 Part 2 Solution: {solution2(example1)} should be 1')
    print(f'Part 2 Solution: {solution2(data)}')
