numb = int(input("Enter a number: "))
for i in range(numb):
    nameOfMac = input("Enter the name of the MAC address: ").capitalize()
    deviceType = input("Enter the device type: ").upper()
    oc1 = input("Enter octet 1:")
    oc2 = input("Enter octet 2:")
    oc3 = input("Enter octet 3:")
    oc4 = input("Enter octet 4:")
    oc5 = input("Enter octet 5:")
    oc6 = input("Enter octet 6:")

    macAddress = "The MAC address is: " + oc1 + ":" + oc2 + ":" + oc3 + ":" + oc4 + ":" + oc5 + ":" + oc6
    print("Name ", nameOfMac, "||", macAddress+" || Device type: ", deviceType)
    forFile = "Name " + nameOfMac + "\n\t" + macAddress + " || Device type: " + deviceType+"\n"
    print(forFile)
    file = open("C:\\Users\Samuel Killagane\OneDrive\macAddress.txt", "a")
    toFile = str(forFile)
    file.write(toFile)
    file.close()

