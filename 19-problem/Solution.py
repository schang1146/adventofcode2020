import re

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


def getAllCombinations(parsedRules):
    combinations = set()
    stack = [[parsedRules["0"][0], ""]]

    while len(stack) > 0:
        currKey, currCombo = stack.pop(-1)

        for code in parsedRules[currKey[0]]:
            if code.isalpha():
                newCombo = currCombo + code
                if len(currKey) == 1:
                    combinations.add(newCombo)
                else:
                    stack.append((currKey[1:], newCombo))
            else:
                stack.append((code+currKey[1:], currCombo))

    return combinations


def parseRulesIntoDictionary(rules):
    rulesDictionary = {}
    for rule in rules:
        id, routes = rule.split(': ')
        rulesDictionary[id] = routes
    return rulesDictionary


def parseRulesIntoRegex(rulesDictionary, ruleId):
    route = rulesDictionary[ruleId]
    if '"' in route:
        return route[1:-1]
    for subRoute in route.split(' | '):
        for num in subRoute.split(' '):
            numRoute = parseRulesIntoRegex(rulesDictionary, num)
            if ('|') in numRoute:
                numRoute = f'({numRoute})'
            route = route.replace(num, numRoute, 1)
    route = route.replace(' ', '')

    return route


def solution1(data):
    rulesRaw = []
    for idx in range(len(data)):
        if data[idx] != '':
            rulesRaw.append(data[idx])
        else:
            break

    parsedDictionaryRules = parseRulesIntoDictionary(rulesRaw)

    parsedRegexRule = parseRulesIntoRegex(parsedDictionaryRules, '0')

    messages = []
    for idy in range(idx + 1, len(data)):
        messages.append(data[idy])

    output = 0
    for message in messages:
        if re.match(f'^{parsedRegexRule}$', message):
            output += 1

    return output


def solution2(data):
    rulesRaw = []
    for idx in range(len(data)):
        if data[idx] != '':
            rulesRaw.append(data[idx])
        else:
            break

    parsedDictionaryRules = parseRulesIntoDictionary(rulesRaw)

    parsedDictionaryRules['8'] = '42 | 42 8'
    parsedDictionaryRules['11'] = '42 31 | 42 11 31'

    r42 = parseRulesIntoRegex(parsedDictionaryRules, '42')
    r31 = parseRulesIntoRegex(parsedDictionaryRules, '31')

    parsedRegexRule = f'(({r42})+)('
    arbitraryNumber = 10
    for i in range(1, arbitraryNumber+1):
        if i < arbitraryNumber:
            parsedRegexRule += f'({r42}){{{i}}}({r31}){{{i}}}|'
        else:
            parsedRegexRule += f'({r42}){{{i}}}({r31}){{{i}}}'
    parsedRegexRule += ')'

    messages = []
    for idy in range(idx + 1, len(data)):
        messages.append(data[idy])

    output = 0
    for message in messages:
        if re.match(f'^{parsedRegexRule}$', message):
            output += 1

    return output


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example2)} should be 3')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example2)} should be 12')
    print(f'Part 2 Solution: {solution2(data)}')
