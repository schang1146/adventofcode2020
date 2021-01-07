# initialize problem variables
data = []
example1 = []
valid_fields = {
    'byr',  # birth year
    'iyr',  # issue year
    'eyr',  # expiration year
    'hgt',  # height
    'hcl',  # hair color
    'ecl',  # eye color
    'pid',  # passport id
    'cid',  # country id
}

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


def get_passports_from_data(data):
    """Parse all passports from the given raw data

    Returns a list of passport dictionaries where the key is the field and value is the value of the field

    Time Complexity: O(n); where n is the number of passports given
    Space Complexity: O(n)
    """
    passports = []
    current_passport = {}
    for line in data:
        if line != '':
            for field in line.strip().split(' '):
                key, val = field.split(':')
                if key in valid_fields:
                    current_passport[key] = val
        else:
            passports.append(current_passport)
            current_passport = {}

    passports.append(current_passport)  # add last passport
    return passports


def is_valid_passport(passport, validation_required=False, relevant_fields=valid_fields):
    """Check if a given passport is valid

    Returns True if valid, otherwise returns False

    Time Complexity: O(1) (there can only be at most 8 fields to check for per passport)
    Space Complexity: O(1)
    """
    num_valid = 0

    # iterate through fields in current passport
    for field in passport.keys():

        # check if field is relevant and if validation of value is required, validates field
        if field in relevant_fields:
            if validation_required:
                if validate_field(field, passport[field]):
                    num_valid += 1
            else:
                num_valid += 1

    # if we validated the same amount of fields that are relevant, passport is valid
    if num_valid == len(relevant_fields):
        return True

    return False


def validate_field(key, val):
    """Check if a given field and it's assigned value is valid

    Returns True if valid, otherwise returns False

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
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
        valid_colors = {
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth'
        }
        if val in valid_colors:
            return True
    # passport id
    elif key == 'pid':
        if len(val) == 9 and val.isdecimal():
            return True
    # return false by default
    return False


def solution1(data, valid_fields):
    """Counts the number of valid passports by checking that they have all required fields"""
    passports = get_passports_from_data(data)

    relevant_fields = valid_fields.copy()
    relevant_fields.remove('cid')

    answer = 0
    for passport in passports:
        if is_valid_passport(passport, False, relevant_fields):
            answer += 1

    return answer


def solution2(data, valid_fields):
    """Counts the number of valid passports by checking that they have all required fields AND valid values"""
    passports = get_passports_from_data(data)

    relevant_fields = valid_fields.copy()
    relevant_fields.remove('cid')

    answer = 0
    for passport in passports:
        if is_valid_passport(passport, True, relevant_fields):
            answer += 1

    return answer


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1, valid_fields)} should be 2')
    print(f'Part 1 Solution: {solution1(data, valid_fields)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1, valid_fields)} should be 2')
    print(f'Part 2 Solution: {solution2(data, valid_fields)}')
