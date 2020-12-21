import numpy as np

with open("input.txt", "r") as file:
    lines = file.read().split("\n")[:-1]
    nums = [int(x) for x in lines]
    preamble = nums[0:25]

    # print(preamble)
    sums = []

    for n in preamble:
        row = list(map(lambda x: x + n, preamble))
        sums.append(row)
    
    sums = np.triu(np.asmatrix(sums), 1)
    # print(sums)
    # print(34 in sums)

    for i in range(25, len(nums)):
        num = nums[i]
        if num not in sums:
            print(num)
            break

        preamble.pop(0)
        sums = np.delete(sums, 0, 0)
        sums = np.delete(sums, 0, 1)
        # print(sums)

        col = np.array(list(map(lambda x: [x + num], preamble)))
        row = np.zeros((1, len(preamble) + 1), int)
        sums = np.append(sums, col, 1)
        sums = np.append(sums, row, 0)

        preamble.append(num)

