with open("input4.txt") as file:
    data = file.read()

{"byr": lambda x: 1920 <= int(x) <= 2002, "iyr": lambda x: }



# get separate passports

raw_passports = data.split("\n\n")


# it will be easier to parse as single-line strings

cleaned_passports = []

for passport in raw_passports:
    clean_passport = passport.replace("\n", " ")

    cleaned_passports.append(clean_passport)

valid_passport_counter = 0

for passport in cleaned_passports:

    passport_dict = dict(pair.split(":") for pair in passport.split())

    if len(set(list(passport_dict.keys())) - set(["cid"])) == 7:
        valid_passport_counter += 1

print(valid_passport_counter)
print(len(cleaned_passports))