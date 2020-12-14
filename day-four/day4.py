def validate(passport):
    if len(passport["byr"]) != 4 or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
        return False
    if len(passport["iyr"]) != 4 or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
        return False
    if len(passport["eyr"]) != 4 or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
        return False
    
    if passport["hgt"][-2:] == "cm":
        if int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193:
            return False
    elif passport["hgt"][-2:] == "in":
        if int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
            return False
    else:
        return False
    
    if passport["hcl"][0] == "#":
        hclchars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        hex = passport["hcl"][1:]
        for c in hex:
            if c not in hclchars:
                return False
    else:
        return False

    eclopts = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if passport["ecl"] not in eclopts:
        return False

    if len(passport["pid"]) != 9:
        return False

    return True    

with open("input.txt", "r") as file:
    lines = file.readlines()
    passports = []
    pass_data = {}
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0

    for line in lines:
        if line == "\n":
            passports.append(pass_data)
            pass_data = {}
            continue

        pd = line.split(" ")
        for data in pd:
            pair = data.split(":")
            # print(pair)
            pass_data[pair[0]] = pair[1].strip()
    passports.append(pass_data)

    for passport in passports:
        # print(passport)
        if not all(field in passport for field in fields):
            continue
        
        if validate(passport):
            valid += 1

    print(valid)
