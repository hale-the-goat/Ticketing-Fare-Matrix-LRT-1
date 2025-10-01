stations = ["North Ave", "Quezon Ave", "GMA Kamuning", "Araneta - Cubao", "Santolan-Annapolis", "Ortigas", "Shaw Blvd.", "Boni", "Guadalupe",
                "Buendia", "Ayala", "Magallanes", "Taft Avenue"]

single_journey =  [
    [0, 15, 20, 20, 25, 25, 25, 25, 30, 30, 35, 35, 35],
    [15, 0, 15, 20, 20, 25, 25, 25, 30, 30, 35, 35, 35],
    [20, 15, 0, 15, 20, 20, 25, 25, 30, 30, 35, 35, 35],
    [20, 20, 15, 0, 15, 20, 20, 25, 30, 30, 35, 35, 35],
    [25, 20, 20, 15, 0, 15, 20, 20, 25, 30, 35, 35, 35],
    [25, 25, 20, 20, 15, 0, 15, 20, 25, 30, 35, 35, 35],
    [25, 25, 25, 20, 20, 15, 0, 15, 20, 25, 30, 35, 35],
    [25, 25, 25, 25, 20, 20, 15, 0, 15, 20, 25, 30, 35],
    [30, 30, 30, 30, 25, 25, 20, 15, 0, 15, 20, 25, 30],
    [30, 30, 30, 30, 30, 30, 25, 20, 15, 0, 15, 20, 25],
    [35, 35, 35, 35, 35, 35, 30, 25, 20, 15, 0, 15, 20],
    [35, 35, 35, 35, 35, 35, 35, 30, 25, 20, 15, 0, 15],
    [35, 35, 35, 35, 35, 35, 35, 35, 30, 25, 20 , 15, 0],
]

stored_value = [
    [0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28, 28],
    [13, 0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28],
    [13, 13, 0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24],
    [16, 13, 13, 0, 13, 13, 16, 16, 20, 20, 20, 24, 24],
    [16, 16, 13, 13, 0, 13, 13, 16, 16, 20, 20, 20, 24],
    [20, 16, 16, 13, 13, 0, 13, 13, 16, 16, 20, 20, 20],
    [20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16, 20, 20],
    [20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16, 20],
    [24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16, 16],
    [24, 24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13, 16],
    [24, 24, 24, 20, 20, 20, 16, 16, 13, 13, 0, 13, 13],
    [28, 24, 24, 24, 20, 20, 20, 16, 16, 13, 13, 0, 13],
    [28, 28, 24, 24, 24, 20, 20, 20, 25, 16, 13, 13, 0]
]

def applydiscount(n):
    return n * 0.50

# DISPLAYS STATIONS
print("===== MRT-3 Stations =====")
for i, station in enumerate(stations, 1):
    print(f"{i}. {station}")

# CARD SELECTION
print(f"\n===== SELECT CARD =====")
print("1. Single Journey Fare Matrix")
print("2. Stored Value Fare Matrix")

ticket = 0
while ticket < 1 or ticket > 2:
    selection1 = int(input("Select Card: "))

    # SINGLE JOURNEY FARE MATRIX
    if selection1 == 1:
        fromDes = 0
        toDes = 0

        # STATION SELECTION
        print(f"\n===== SELECT STATION =====")
        while fromDes < 1 or fromDes > 13:
            fromDes = int(input("From (Station 1-13): "))
        while toDes < 1 or toDes > 13:
            toDes = int(input("To (Station 1-13): "))

        baseprice = single_journey[fromDes - 1][toDes - 1]

        # DISCOUNT SELECTION
        print(f"\n===== SELECT STATUS =====")
        print("1. Student")
        print("2. Senior")

        status = -1
        while status != 0 and status != 1 and status != 2:
            selection2 = int(input("Select status (0 if none of the above): "))

            if selection2 == 1:
                finalprice = applydiscount(baseprice)
            if selection2 == 2:
                finalprice = applydiscount(baseprice)
            if selection2 == 0:
                finalprice = baseprice
            status = selection2

            # DISPLAYS TICKET DETAILS
            print(f"\n===== Ticket Details =====")
            print(f"\nFrom: {stations[fromDes - 1]}")
            print(f"To: {stations[toDes - 1]}")
            print("-----------------------------")
            print(f"Ticket price: ₱{finalprice}")

    # STORED VALUE FARE MATRIX
    if selection1 == 2:
        fromDes = 0
        toDes = 0

        # STATION SELECTION
        print(f"\n===== SELECT STATION =====")
        while fromDes < 1 or fromDes > 13:
            fromDes = int(input("From (Station 1-13): "))
        while toDes < 1 or toDes > 13:
            toDes = int(input("To (Station 1-13): "))

        baseprice = stored_value[fromDes - 1][toDes - 1]

        # DISCOUNT SELECTION
        print(f"\n===== SELECT STATUS =====")
        print("1. Student")
        print("2. Senior")

        status = -1
        while status != 0 and status != 1 and status != 2:
            selection2 = int(input("Select status (0 if none of the above): "))

            if selection2 == 1:
                finalprice = applydiscount(baseprice)
            if selection2 == 2:
                finalprice = applydiscount(baseprice)
            if selection2 == 0:
                finalprice = baseprice
            status = selection2

            # DISPLAYS TICKET DETAILS
            print(f"\n===== Ticket Details =====")
            print(f"From: {stations[fromDes - 1]}")
            print(f"To: {stations[toDes - 1]}")
            print("-----------------------------")
            print(f"Ticket price: ₱{finalprice}")
    ticket = selection1
