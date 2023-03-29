def search(nparray,column):
    found = False
    #run until valid value is entered
    while not found:
        print("Items in "+column+": ", nparray)
        value = input("Enter "+column+": ")
        for i in range(len(nparray)):
            #make both user input and value lowercase
            if value.lower() == nparray[i].lower():
                #take proper case value
                value = nparray[i]
                #make loop break
                found = True
        if found: return value
        print("Sorry, the "+column+" you entered is not identifiable by the database. Keep trying!")