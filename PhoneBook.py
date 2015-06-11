# Create a dictionary of dictionaries to hold your data.
phonebook = {"id": 1, "fname" : "Dar", "lname": "Wright", "phone": "XXX-XXX-XXXX"}, \
            {"id": 2, "fname" : "Luigi", "lname": "Mario", "phone": "505-123-4567"}


def add():
    # Function for adding entries

    pass


def change():
    # Function to change entries

    pass


def delete():
    # Function to delete entries
    pass

def search_fname(name):
    name = str.capitalize(name)
    for n in phonebook:
        if name == n["fname"]:
            return n["id"]
        else:
            print "No match found."
            return 0

def search_lname(name):
    name = str.capitalize(name)
    for n in phonebook:
        if name == n["lname"]:
            return n["id"]
        else:
            print "No match found."
            return 0

def search_phone(phone):
    for n in phonebook:
        if phone == n["phone"]:
            return n["id"]
        else:
            print "No match found."
            return 0



def search():
    # Function to search for entries
    while True:
        choice = raw_input("Press 1 to search by first name. \nPress 2 to search by last name. "
                           "\nPress 3 to search by phone number.\nPress 4 to quit.\n>")
        if choice == '1':
            name = raw_input("Please enter the first name: ")
            id = search_fname(name)
                if
        elif choice == '2':

        elif choice == '3':

        else:
            exit()


while True:
    choice = raw_input("press 1 to search, 2 to add, 3 to update, 4 to delete.")
    if choice == '1':
        search()
    elif choice == '2':
        add()
    elif choice == '3':
        change()
    elif choice == '4':
        delete()
    else
        print "Not a valid choice. Please try again."
    # The rest of the menu code here
