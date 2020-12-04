# initialize problem variables
data = []
validFields = {
    'byr',  # birth year
    'iyr',  # issue year
    'eyr',  # expiration year
    'hgt',  # height
    'hcl',  # hair color
    'ecl',  # eye color
    'pid',  # passport id
    'cid',  # country id
}

# populate data from input file
# time complexity: O(k + n) where k is the number of lines in the file
# space complexity: O(n) where n is the number of passports in the file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
passport = {}
for line in lines:

    # parse current line's key/val pair into passport dictionary
    if line != '\n':
        for field in line.strip().split(' '):
            key, val = field.split(':')
            if key in validFields:
                passport[key] = val

    # if empty line, save current passport data and start a new passport
    else:
        data.append(passport)
        passport = {}
data.append(passport)

# function to count the number of valid passports in the given file
# returns number of valid passports
# time complexity: O(n)
# space complexity: O(1)
def numValidPassports(passports, validationRequired = False, relevantFields = validFields):
    output = 0
    for passport in passports:
        numValidated = 0

        # iterate through fields in current passport
        for field in passport.keys():
        
            # check if field is relevant and if validation of value is required, validates field
            if field in relevantFields:
                if validationRequired:
                    if validateField(field, passport[field]):
                        numValidated += 1
                else:
                    numValidated += 1
        
        # if we validated the same amount of fields that are relevant, passport is valid
        if numValidated == len(relevantFields):
            output += 1

    return output

# function to validate a field and it's value
# returns True if valid, otherwise False
# time complexity: O(1)
# space complexity: O(1)
def validateField(key, val):
    # birth year
    if key == 'byr':
        if len(val) == 4 and val.isdecimal() and int(val) >= 1920 and int(val) <= 2002:
            return True
    # issue year
    elif key == 'iyr':
        if len(val) == 4 and val.isdecimal() and int(val) >= 2010 and int(val) <= 2020:
            return True
    # expiration year
    elif key == 'eyr':
        if len(val) == 4 and val.isdecimal() and int(val) >= 2020 and int(val) <= 2030:
            return True
    # height
    elif key == 'hgt':
        if val[-2:] == 'cm':
            if val[:-2].isdecimal() and int(val[:-2]) >= 150 and int(val[:-2]) <= 193:
                return True
        elif val[-2:] == 'in':
            if val[:-2].isdecimal() and int(val[:-2]) >= 59 and int(val[:-2]) <= 76:
                return True
    # hair color
    elif key == 'hcl':
        if val[0] == '#':
            for char in val[1:]:
                if char.isdecimal() or (ord(char) >= ord('a') and ord(char) <= ord('z')):
                    return True
    # eye color
    elif key == 'ecl':
        validColors = {
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth'
        }
        if val in validColors:
            return True
    # passport id
    elif key == 'pid':
        if len(val) == 9 and val.isdecimal():
            return True
    # return false by default
    return False

pt1RelevantFields = validFields.copy()
pt1RelevantFields.remove('cid')

pt2RelevantFields = validFields.copy()
pt2RelevantFields.remove('cid')

print(f"Part 1 Solution: {numValidPassports(data, False, pt1RelevantFields)}")
print(f"Part 2 Solution: {numValidPassports(data, True, pt2RelevantFields)}")