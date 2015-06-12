# Create a dictionary of dictionaries to hold your data.
phonebook = {"id": 1, "fname" : "Dar", "lname": "Wright", "phone": "XXX-XXX-XXXX"}, \
            {"id": 2, "fname" : "Luigi", "lname": "Mario", "phone": "505-123-4567"}, \
            {"id": 2, "fname" : "Mario", "lname": "Mario", "phone": "555-123-4567"}


def add():
    # Function for adding entries

    pass


def change():
    # Function to change entries

    pass


def delete():
    # Function to delete entries
    while True:
        choice = str.lower(raw_input("Are you sure you want to delete an entry? Yes or No: "))
        if choice == 'yes' or choice == 'y':
            entry = search()
            print entry
            del_entry = str.lower(raw_input("This is the entry you wish to delete? Yes or No: ?"))
            if len(entry) > 1:
                if del_entry == 'yes' or choice == 'y':
                    del phonebook[entry]
            else:
                exit()
        elif choice == 'no' or choice == 'n':
            exit()
        else:
            print "Please enter a valid option.\n"

    pass


def search_fname(name):
    name = str.capitalize(name)
    found = []
    for n in phonebook:
        if name == n["fname"]:
            found.append(n)
    return found


def search_lname(name):
    name = str.capitalize(name)
    found = []
    for n in phonebook:
        if name == n["lname"]:
            found.append(n)
    return found


def search_phone(phone):
    phone = phone
    found = []
    for n in phonebook:
        if phone == n["phone"]:
            found.append(n)
    return found



def search():
    # Function to search for entries
    while True:
        choice = raw_input("Press 1 to search by first name. \nPress 2 to search by last name. "
                           "\nPress 3 to search by phone number.\nPress 4 to quit.\n>")
        if choice == '1':
            name = raw_input("Please enter the first name: ")
            entries = search_fname(name)
            if not entries:
                print "No match found."
            else:
                for n in entries:
                    print n["fname"], n["lname"], n["phone"]
            return entries

        elif choice == '2':
            name = raw_input("Please enter the last name: ")
            entries = search_lname(name)
            if not entries:
                print "No match found."
            else:
                for n in entries:
                    print n["fname"], n["lname"], n["phone"]
            return entries
            exit()
        elif choice == '3':
            phone = raw_input("Please enter the phone number in this format XXX-XXX-XXXX: ")
            entries = search_phone(phone)
            if not entries:
                print "No match found."
            else:
                for n in entries:
                    print n["fname"], n["lname"], n["phone"]
            return entries
            exit()
        elif choice == '4':
            exit()
        else:
            print "Please enter a valid option.\n"

def phonebook():
    while True:
        choice = raw_input("Press 1 to search.\nPress 2 to add.\n3 to update.\n4 to delete.\n5 to quit.\n>>")
        if choice == '1':
            search()
        elif choice == '2':
            add()
        elif choice == '3':
            change()
        elif choice == '4':
            delete()
        elif choice == '5':
            exit()
        else:
            print "Not a valid choice. Please try again.\n\n"

phonebook()

