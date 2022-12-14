from utils import display, readParkingData, statistics, reserve

# Main execution
# create menu
filename = 'carpark.txt'
menu = "\n(D) Display the current status"
menu += "\n(R) Reserve an empty slot"
menu += "\n(S) Show Percent(%) occupancy"
menu += "\n(Q) Quit"
menu += "\nSelect your choice : "
# read file for parking data information
headers, parkingData = readParkingData(filename)
# loop until user enters Q(Quit)
while (True):
    choice = input(menu)
    choice = choice.upper()
    if choice == 'D':
        display(filename)
    elif choice == 'R':
        reserve(filename, headers, parkingData)
    elif choice == 'S':
        print("Occupancy % = ", statistics(parkingData))
    elif choice == 'Q':
        break
