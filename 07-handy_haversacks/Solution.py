# initialize problem variables
data = []
example1 = []
example2 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(line.strip())
filename = 'example2.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example2.append(line.strip())

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())


def parseData(data):
    """Parses raw data

    Returns:
    - containers = set of all of the colors of bags available
    - rules = dictionary where key is the color of the outer bag and the value is a dictionary of contained bags

    Time Complexity: O(v + e) where v == # of vertices and e == # of edges
    Space Complexity: O(v)
    (vertices -> bag colors; edges -> bag container relationships)
    """
    containers = set()
    rules = {}
    for line in data:
        container, contents = line.split('contain')
        container = container.strip()[:-5]
        contents = contents.split(',')

        containers.add(container)
        rules[container] = {}
        for content in contents:
            if content.strip()[:2] != 'no':
                numBags, bag = content.strip().split(' ', 1)
                contentDescription = bag.rstrip('.').rsplit(' ', 1)[0]
                rules[container][contentDescription] = int(numBags)

    return [containers, rules]


def count_bags_can_contain_shiny_gold_bag(rules):
    """Count the total number of bags that can contain a shiny gold bag given a set of rules

    Returns the number of bags that can contain a shiny gold bag

    Time Complexity: O(v + e) where v == # of vertices and e == # of edges
    Space Complexity: O(v)
    (vertices -> bag colors; edges -> bag container relationships)
    """
    seen = set()
    stack = [[color] for color in rules.keys()]
    canContainGold = set()
    while len(stack) > 0:
        currentPath = stack.pop(-1)
        currentColor = currentPath[-1]
        seen.add(currentColor)

        for color in rules[currentColor].keys():
            if color == 'shiny gold':
                for history in currentPath:
                    canContainGold.add(history)

            elif color not in seen:
                stack.append(currentPath + [color])

            else:
                if color in canContainGold:
                    for history in currentPath:
                        canContainGold.add(history)

    return len(canContainGold)


def count_bags_in_shiny_gold_bag(rules):
    """Count the total number of bags inside one shiny gold bag given a set of rules

    Returns the number of bags inside one shiny gold bag

    Time Complexity: O(v + e) where v == # of vertices and e == # of edges
    Space Complexity: O(v)
    (vertices -> bag colors; edges -> bag container relationships)
    """
    totalBags = 0
    stack = [('shiny gold', 1)]
    while len(stack) > 0:
        currentColor, currentMultiplier = stack.pop()

        for color in rules[currentColor].keys():
            totalBags += rules[currentColor][color] * currentMultiplier
            stack.append((color, currentMultiplier * rules[currentColor][color]))

    return totalBags


def solution1(data):
    containers, rules = parseData(data)
    return count_bags_can_contain_shiny_gold_bag(rules)


def solution2(data):
    containers, rules = parseData(data)
    return count_bags_in_shiny_gold_bag(rules)


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 4')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example2)} should be 126')
    print(f'Part 2 Solution: {solution2(data)}')
