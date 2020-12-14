with open("input.txt", "r") as file:
    passwords = file.readlines()
    directory = {}

    valid = 0

    for password in passwords:
        p1 = password.split(": ")
        pw = p1[1]
        limits = []
        limstring = p1[0].split("-")
        limits.append(int(limstring[0]))
        limits.append(int(limstring[1].split(" ")[0]))
        letter = p1[0].split(" ")[1]

        # count = 0
        # start = pw.find(letter)
        # while start != -1:
        #     count += 1
        #     pw = pw[(start + 1):]
        #     print(pw)
        #     start = pw.find(letter)
        #
        # if count >= int(limits[0]) and count <= int(limits[1]):
        #     valid += 1
        #     print("yes")

        isValid = (pw[limits[0] - 1] == letter or pw[limits[1] - 1] == letter) and not (pw[limits[0] - 1] == letter and pw[limits[1] - 1] == letter)
        if isValid:
            valid += 1

    print(valid)
