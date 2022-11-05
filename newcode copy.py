from sqlite3 import adapt


def getDataSet(filename):
    carpark_dataset = []
    file = open(filename, 'r')
    cardataset = [line.strip('\n') for line in file]
    carpark_dataset = []
    for i in cardataset:
        y = [j for j in i]
        carpark_dataset.append(y)
    file.close()
    return carpark_dataset


def display(dataset):
    print('  ABCD EFGH')
    row_no = 1
    for row in dataset:
        if row:
            print(row_no, end=' ')
            row_no += 1
        for column in row:
            print(column, end='')
        print(' ')


def updateDataSetFile(dataset):
    open('carpark.txt', 'w')
    file = open('carpark.txt', 'a')
    for row in dataset:
        data = ""
        for column in row:
            data += column
        file.write(data+"\n")


def assign_slot(dataset, row, column):
    if(column > 8 or row > 13):
        print('Parking slot is not available')
    elif(dataset[row][column] == 'X'):
        print('\nParking slot is already occupied\n')
    else:
        dataset[row][column] = 'X'
        # update dateset and file
        updateDataSetFile(dataset)
        print('\nParking slot booked successfully!\n')


def availableSlots(carpark_dataset):
    cols = {0: 'A', 1: 'B', 2: 'C', 3: 'D',
            4: 'E', 5: 'D', 6: 'F', 7: 'G', 8: 'H'}
    available_slots = []
    for rowIndex, row in enumerate(carpark_dataset):
        for columnIndex, column in enumerate(row):
            rowIndex+1
            if column == "O":
                slots = str(rowIndex)+cols[columnIndex]
                available_slots.append(slots)
    return available_slots


while(True):
    carpark_dataset = getDataSet('carpark.txt')
    print()
    print('Select your choice from the menu:')
    print('D to display current status of the car park')
    print('R to reserve an empty slot in the car park')
    print('S to display % occupancy of the car park')
    print('Q to quit')
    choice = input()
    choice = choice.upper()
    if(choice == 'Q'):
        break
    elif(choice == 'D'):
        display(carpark_dataset)

    elif(choice == 'R'):
        # suggest the clossest  car park
        available_slots = availableSlots(carpark_dataset)
        print()
        quest = input(
            f"Closest available slot is {available_slots[0]}, do you want to reserve it (y/n)? ")
        quest.lower()
        if quest == 'y':
            cols = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                    'E': 4, 'D': 5, 'F': 6, 'G': 7, 'H': 8}
            column = cols[available_slots[0][1]]
            row = int(available_slots[0][0])
            print(row, column)
            assign_slot(carpark_dataset, row, column)
        elif quest == 'n':
            row = int(input('Row: '))
            column = int(input('column: '))
            assign_slot(carpark_dataset, row, column)

    elif(a == 'S'):
        count = 0
        total = 80
        for row in carpark_dataset:
            for column in row:
                if(column == 'X'):
                    count += 1
        print('Occupancy % : ', end='')
        print((count * 100) / total)
