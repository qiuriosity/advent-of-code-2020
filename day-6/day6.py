with open("input.txt", "r") as file:
    inputs = file.read().split("\n\n")
    responses = []
    total = 0
    # print(inputs)

    for input in inputs:
        # combined = set(input.replace("\n", ""))
        # total += len(combined)
        entries = input.strip().split("\n")
        combined = entries[0]

        for i in range(1, len(entries)):
            combined = list(set(combined) & set(entries[i]))
            print(combined)
        
        total += len(combined)
    
    print(total)