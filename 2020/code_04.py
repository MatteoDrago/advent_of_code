### PART 1

file = open('input_04.txt')

passport = []
passport_list = []
for el in file:
    el = el.strip()
    if el == "":
        if len(passport) > 1:
            joined_psp = ' '.join(passport)
            passport = joined_psp
        else:
            passport = passport[0]
        passport_list.append(passport)
        passport = []
    else:
        passport.append(el)

if len(passport) > 0:
    if len(passport) > 1:
        joined_psp = ' '.join(passport)
        passport = joined_psp
    else:
        passport = passport[0]
    passport_list.append(passport)

file.close()

required_fields = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
expected_fields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

count = 0
total = 0
for el in passport_list:
    total += 1
    splitted = el.split()
    splitted.sort()
    present = []
    for fld in splitted:
        present.append(fld.split(':')[0])
    if (present == required_fields) or (present == expected_fields):
        count += 1

print(f'We have',count,'valid passports over a total of',total,'.')

### PART 2

import re

count = 0
total = 0

ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for el in passport_list:
    total += 1
    splitted = el.split()
    splitted.sort()
    present = []
    fields = []

    for fld in splitted:
        fields_split = fld.split(':')
        present.append(fields_split[0])
        fields.append(fields_split[1])

    if present == required_fields:
        del present[1]
        del fields[1]

    if present == expected_fields:
        byr = int(fields[0])
        ecl = fields[1]
        eyr = int(fields[2])
        hcl = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', fields[3])
        hgt_cm = re.search(r'1[5-9][0-9]cm', fields[4])
        hgt_in = re.search(r'[5-7][0-9]in', fields[4])
        iyr = int(fields[5])
        pin = re.search(r'[0-9]{9,9}$', fields[6])
        if byr < 1920 or byr > 2002:
            continue
        elif ecl not in ecl_list:
            continue
        elif eyr < 2020 or eyr > 2030:
            continue
        elif not hcl:
            continue
        elif iyr < 2010 or iyr > 2020:
            continue
        elif not pin or len(fields[6]) > 9:
            continue
        elif not hgt_cm and not hgt_in:
            continue
        else:
            if hgt_cm:
                numb = int(fields[4][0:3])
                if numb < 150 or numb > 193:
                    continue
                else:
                    count += 1
                    #print(f'byr:', byr,' ecl', ecl,' eyr', eyr,' hcl', fields[3],' hgt', fields[4],' iyr', iyr,' pin', fields[6])
            if hgt_in:
                numb = int(fields[4][0:2])
                if numb < 59 or numb > 76:
                    continue
                else:
                    count += 1
                    #print(f'byr:', byr,' ecl', ecl,' eyr', eyr,' hcl', fields[3],' hgt', fields[4],' iyr', iyr,' pin', fields[6])


print(f'We have', count,' valid passports over a total of',total,'.')
