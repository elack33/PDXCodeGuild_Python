# Create a program that asks the user to enter their name
# and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for
# another number and printing out that many copies of the
# previous message. (Hint: order of operations exists in Python)
#
# Print out that many copies of the previous message on separate lines.

import datetime

def name_age_repeater():
    age = int(raw_input("Please enter your age: "))
    # Figure out todays date
    mydate = datetime.datetime.now()
    monthineger = mydate.month
    mint = int(monthineger)
    mymonth = datetime.date(1900, mint, 1).strftime('%B')
    mymonth = str(mymonth)
    # Ask if they were born before today in the year, to acurately calculate other years
    halfyear = raw_input("Were you born before today in the month of %s? (Enter Y or N): " % (mymonth))
    # if statements to eval if before or after today for accurate year calc
    if halfyear == 'Y':
        year = (100 - age) + mydate.year
    else:
        year = (99 - age) + mydate.year
    print "Welcome, %s! You turn 100 in the year %s." % (name, year)
    #Ask how many times you want to see the message
    numcopies = raw_input("How many times would you like to see the previous message: ")
    numcopies = int(numcopies)
    counter = 0
    #While loop for repeating message
    while counter < numcopies:
        print "Welcome, %s! You turn 100 in the year %s." % (name, year)
        counter += 1

#Call the function
name_age_repeater()
