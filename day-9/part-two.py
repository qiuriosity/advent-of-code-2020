with open("input.txt", "r") as file:
    lines = file.read().split("\n")[:-1]
    nums = [int(x) for x in lines]

    target = 257342611
    start = 0
    end = 1
    total = nums[start] + nums[end]

    while True:
        if total == target:
            break
        if total < target:
            end += 1
            total += nums[end]
        if total > target:
            total -= nums[start]
            start += 1
    
    segment = nums[start:end + 1]
    print(min(segment) + max(segment))