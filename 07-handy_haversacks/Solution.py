# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line)

# function that parses the input data and returns a set of containers
# and a hashmap of the rules
# time complexity: O(v + e) where v == # of vertices and e = # of edges
# space complexity: O(v)
def parseData(data):
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

containers, rules = parseData(data)

# function returns the total number of bags that can contain a shiny gold bag
# time complexity: O(v + e) where v == # of vertices and e = # of edges
# space complexity: O(v)
def totalBagsCanContainShinyGoldBag(rules):
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

# function returns the total # of bags inside the a shiny gold bag if
# the rules passed in described the # of bags inside each other bag
# time complexity: O(v + e) where v == # of vertices and e = # of edges
# space complexity: O(v)
def totalBagsInShinyGoldBag(rules):
    totalBags = 0
    stack = [('shiny gold', 1)]
    while len(stack) > 0:
        currentColor, currentMultiplier = stack.pop()

        for color in rules[currentColor].keys():
            totalBags += rules[currentColor][color] * currentMultiplier
            stack.append((color, currentMultiplier * rules[currentColor][color]))

    return totalBags



print(f"Part 1 Solution: {totalBagsCanContainShinyGoldBag(rules)}")

print(f"Part 2 Solution: {totalBagsInShinyGoldBag(rules)}")