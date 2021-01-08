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


def get_unanimous_count(responses):
    """Counts the number of characters that show up in every response of a group

    Returns the count of unanimous answers

    Time Complexity: O(n) where n is the total number of characters in the response group
    Space Complexity: O(n)
    """
    seen = {}
    for response in responses:
        for char in response:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

    unanimous_count = 0
    for char in seen.keys():
        if seen[char] == len(responses):
            unanimous_count += 1

    return unanimous_count


# function to returns total # of unique answers people said yes to in each group
# time complexity: TODO
# space complexity: TODO


def get_unique_count(responses):
    """Count the number of unique characters in a response group

    Returns a count of the unique characters

    Time Complexity: O(n) where n is the total number of characters in the response group
    Space Complexity: O(n)
    """
    seen = set()
    unique_count = 0
    for response in responses:
        # newline denotes a new group, so add current unique_count and reset seen
        if response == '\n':
            unique_count += len(seen)
            seen = set()
        else:
            response = response.strip()
            for char in response:
                if char not in seen:
                    seen.add(char)
    # if there was no newline at the end of responses,
    # add the number of elements in seen
    if len(seen) != 0:
        unique_count += len(seen)

    return unique_count


def parse_data(data):
    """Parses the raw data into a list of response groups

    Returns a list of response groups that contain the responses in each group

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    response_groups = []
    current_group = []
    for line in data:
        if line == "":
            response_groups.append(current_group)
            current_group = []
        else:
            current_group.append(line)
    response_groups.append(current_group)
    return response_groups


def solution1(data):
    """Sums the number of unique characters that are chosen for each group"""
    response_groups = parse_data(data)
    answer = 0
    for responses in response_groups:
        answer += get_unique_count(responses)
    return answer


def solution2(data):
    """Sums the number of characters that are unanimously chosen for each group"""
    response_groups = parse_data(data)
    answer = 0
    for responses in response_groups:
        answer += get_unanimous_count(responses)
    return answer


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 11')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be 6')
    print(f'Part 2 Solution: {solution2(data)}')
