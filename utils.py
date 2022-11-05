# update specified file with the given parking dictionary
def updateFile(filename, headers, parkingData):
    f = open(filename, "w")  # open file in write mode to update the file
    # iterate through dictionary for writing all rows into the file
    for idx, i in enumerate(parkingData):
        row = ""  # initialize row string for each row
        for j in parkingData[i]:  # iterate through row specific dictionary
            cs = parkingData[i].get(j)
            if not cs:
                cs = " "
            row += cs  # append to row
        # write each row into file
        if idx != 0:
            f.write('\n')
        f.write(' '.join(row[i:i + 4] for i in range(0, len(row), 4)))
    f.close()  # close file


# check slot availability for given row and column
def checkAvailability(parkingData, row, column):
    # if row and column in given parking Information
    if (row in parkingData) and (column in parkingData[row]):
        if parkingData[row][column] == 'X':  # if not available return 0
            return 0
        else:
            return 1  # if available return 1
    else:
        return -1  # if row, column does not exist in dictionary , denotes out of bounds


# get occupancy percentage
def getOccupancyPercentage(parkingData):
    total = 0  # initialize total to 0 , to count total slots
    occupied = 0  # initialize occupied to 0 , to count occupied slots
    for i in parkingData:  # iterate through parking data
        for j in parkingData[i]:
            # check if slot is occupied if yes - increment count of occipied
            if parkingData[i][j] == 'X':
                occupied += 1
            total += 1  # increment total slots
    return (occupied * 100) / total  # count percentage of occupancy


# get nearest available slots
def getNearestAvailableSlot(headers, parkingData):
    for cnt in range(1, 9):
        iCnt = 1  # increment counter
        for i in range(1, cnt + 1):  # logic return to iterate in cnt*cnt matrix
            jCnt = 1
            for j in headers:  # iterate through headers in the parkingData
                # check if slot available then return corresponding position
                cs = parkingData[i].get(j)
                if not cs:
                    cs = " "
                if cs == 'O':
                    return i, j
                jCnt += 1  # increment column counter

                # if column count > cnt skip to next row
                if jCnt > cnt:
                    break
            # increment row cnt
            iCnt += 1
            # if row count > cnt skip to next matrix
            if iCnt > cnt:
                break
    # if no available slot in 8*8 matrix , return -1,-1 denoting to enter manually row,column
    return -1, -1


# method to reserve the parking slot
def reserve(filename, headers, parkingData):
    # get nearest available slots
    row, column = getNearestAvailableSlot(headers, parkingData)
    # if row or column is -1 - denotes the no slots available nearby
    if row == -1 or column == -1:
        print("No nearest slots available")
    else:
        # if slots available ask user to continue with available slots
        print('Nearest available slots from building entrance are row:%d, column :%s' % (
            row, column))
        choice = input(
            '\n Do you want to continue with nearest available slot?(y/n)')
        choice = choice.upper()
        if choice == 'Y':  # if yes , reserve the available slots otherwise read slot position from usre
            parkingData[row][column] = 'X'
            updateFile(filename, headers, parkingData)
            return

    row = int(input("\nEnter row number : "))  # read manual row from user
    column = input("\nEnter column letter : ")  # read manual column from usre
    # check availability of entered row, column slot
    flag = checkAvailability(parkingData, row, column)
    if flag == 1:  # if available ,reserve
        parkingData[row][column] = 'X'
        updateFile(filename, headers, parkingData)  # update file
    elif flag == 0:
        # if row , column is reserved show message to user
        print("Entered row and column postion is not available")
    elif flag == -1:
        print(
            "Entered row and column postion is out of range")  # if entered row column is out of bounds show error message to user

# read parking information from specified file in dictionary and return dictionary


def readParkingData(filename):
    parkingData = {}  # initialize dictionary for storing parking information
    with open(filename) as f:  # open file to read parking information
        # read first line into headers list and remove white spaces using strip()
        # headers = list(f.readline().replace(" ", "").strip())
        headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        index = 1  # initialize index to 1 for keeping row record
        for line in f:  # iterate line by line
            # read all rows in the file and remove white spaces and store into dictionary in format {row:{column:'X'}}
            parkingData[index] = dict(
                zip(headers, list(line.replace(" ", "").strip())))
            index += 1  # increment row counter
    # return headers and  parking dictionary
    return headers, parkingData


# display status of current
def displayStatus(filename):
    # read parking information from file
    headers, parkingData = readParkingData(filename)
    # join headers
    displayString = ''.join(headers)
    # format the display to show parking stuatus in readable format with keeping 4 precision for first column with empty path
    displayString = '{0: <4}'.format(
        ' ') + ' '.join(displayString[i:i + 4] for i in range(0, len(displayString), 4))
    print(headers)
    # print each row data
    for r in parkingData:
        displayString += "\n" + '{0: <4}'.format(str(r))
        row = ""
        for c in headers:
            cs = parkingData[r].get(c)
            if not cs:
                cs = " "
            row += cs
        displayString += ' '.join(row[i:i + 4] for i in range(0, len(row), 4))
    print(displayString)
