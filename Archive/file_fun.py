# with open('/Users/darwright/Python/test.txt', 'wr') as my_file:
#     my_file.write("Class is so fun, even when the weather is hot.\n")
#
# with open('/Users/darwright/Python/name-age.txt', 'a') as f:
#     f.write("Test test testing")

my_file = '/Users/darwright/Python/name-age.txt'
choice = int(raw_input('Do you want to get (1) or write a name (2)?'))

if choice == 2:
    name = raw_input("Name: ")
    age = raw_input("Age: ")

    with open(my_file, 'a') as name_age_file:
        name_age_file.write('{},{}\n'.format(name, age))

elif choice == 1:
    name_requested = raw_input("What name you looking for:")
    with open(my_file) as name_age_file:
        for line in name_age_file
            name, age = line.split(',')
            if name_requested == name:
                print 'The age of {} is {}'.format(name, age)