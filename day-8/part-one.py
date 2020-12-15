with open("input.txt", "r") as file:
    instructions = file.readlines()
    log = []
    index = 0
    accumulator = 0

    while True:
        current = instructions[index]
        if index in log:
            break
        log.append(index)
        operation = current[:3]
        argument = int(current[4:])

        if operation == "jmp":
            index += argument
            print(index)
            continue
        if operation == "acc":
            accumulator += argument
        
        index += 1
    
    print(accumulator)
