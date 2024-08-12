print("Event host only!")
eventName = input("Please enter the event name: ")
totalNumTickets = input("Please enter total number of tickets to be sold: ")

totalNumGeneral = input("Please enter total number  of General tickets to be sold: ")
totalNumVip = input("Please enter total number of VIP tickets to be sold: ")
totalNumVvip = input("Please enter total number of VVIP tickets to be sold: ")

numGeneral = (int(totalNumTickets) - int(totalNumVip)- int(totalNumVvip))
numVip = int(totalNumTickets) - int(totalNumGeneral) - int(totalNumVvip)
numVvip = int(totalNumTickets) - int(totalNumGeneral)  - int(totalNumVip)

ticketPrice = 0.00

print("1. General")
print("2. VIP")
print("3. VVIP")
print("\n")

for i in range(int(totalNumTickets)):

    ticketOption = int(input("Please enter option number from the above list: "))

    name = input("Please enter your first name: ")
    while name.isalpha() == False:
      print("\n")
      print("The first name provided contains numbers")
      name = input("Please enter your first name: ")

    surname = input("Pleas enter your last name: ")
    while surname.isalpha() == False:
      print("\n")
      print("The surname provided contains numbers")
      surname = input("Please enter your last name: ")
        
    if ticketOption == 1:
      ticketName = "General"
      ticketPrice = 100
    elif ticketOption == 2:
      ticketName = "VIP"
      ticketPrice = 120
    elif ticketOption == 3:
      ticketName = "VVIP"
      ticketPrice = 200
    else:
      print("Option you have entered is not available")

    if ticketName == "General":
      numGeneral = int(totalNumGeneral) - 1
      totalNumTickets = int(totalNumTickets) - 1

    elif ticketName == "VIP":
      numVip = int(totalNumVip) - 1
      totalNumTickets = int(totalNumTickets) - 1
    
    else:
      numVvip = int(totalNumVvip) - 1
      totalNumTickets = int(totalNumTickets) - 1
      

    print("\n")
    print("************"+ eventName +"************")
    print("Ticket Type: "+ ticketName)
    print("Ticket Price: "+ str(ticketPrice))
    print("Customer Name: "+ name +" "+ surname)
    print("\n")

    print("The number of general tickets remaining are: "+ str(numGeneral))
    print("The number of VIP tickets remaining are:" + str(numVip))
    print("The number of VVIP tickets remaining are:" + str(numVvip))
    print("The total number of tickets remaining are: " + str(totalNumTickets))

    print("\n")
    print("1. General")
    print("2. VIP")
    print("3. VVIP")
    print("\n")

