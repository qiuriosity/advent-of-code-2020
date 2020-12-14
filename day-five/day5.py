with open("input.txt", "r") as file:
    seatings = file.readlines()
    # max = 0
    seat_ids = []

    for seating in seatings:
        row = 0
        column = 0

        for c in seating[:7]:
            if c == "F":
                row += row
            else:
                row += row + 1
        
        for c in seating[7:].strip():
            if c == "L":
                column += column
            else:
                column += column + 1
        
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
        # if seat_id > max:
        #     max = seat_id

    for i in seat_ids:
        if i < len(seat_ids) - 2 and (i + 1) not in seat_ids and (i + 2) in seat_ids:
            print(i + 1)
    # print(max)
    