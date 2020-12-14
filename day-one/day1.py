with open("input.txt", "r") as file:
    nums = file.readlines()
    directory = {}

    for num in nums:
        directory[int(num)] = 2020 - int(num)

    for num in nums:
        if (2020 - int(num)) in directory:
            print(int(num) * (2020 - int(num)))
