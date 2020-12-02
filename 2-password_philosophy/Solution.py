# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    rules, password = line.split(':')
    count, letter = rules.split(' ')
    x, y = count.split('-')

    password = password.strip()

    # formatting it as a dictionary/object for easier lookup later
    data.append({
        'x': int(x),
        'y': int(y),
        'letter': letter,
        'password': password
    })

# function to count how many valid passwords are in data
# password is valid if the password contains the required letter between x and y number of occurrences inclusive
# time complexity: O(k); where k is the total number of characters, we gotta count all the characters to know if it's within min/max bounds
# space complexity: O(n)
def countValidPasswords1(data):
    output = 0
    for item in data:
        count = 0
        for char in item['password']:
            if char == item['letter']:
                count += 1
        if count >= item['x'] and count <= item['y']:
            output += 1
    return output

print(f'Part 1 Solution: {countValidPasswords1(data)}')

# function to count how many valid passwords are in data
# password is valid if the password contains the required letter at exactly one of the positions x or y
# time complexity: O(n); we're just looking up two characters in each password string so n referring to number of passwords
# space complexity: O(n)
def countValidPasswords2(data):
    output = 0
    for item in data:
        x = item['x']
        y = item['y']
        password = item['password']
        letter = item['letter']

        letterAtX = False
        letterAtY = False

        if x <= len(password):
            if password[x-1] == letter:
                letterAtX = True

        if y <= len(password):
            if password[y-1] == letter:
                letterAtY = True

        if letterAtX ^ letterAtY:
            output += 1
    return output

print(f'Part 2 Solution: {countValidPasswords2(data)}')