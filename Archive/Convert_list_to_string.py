def return_string(my_list):
    """
    write a function to turn a list of strings into a single word with commas.
    ['Reina', 'Ollie', 'Rachel'] becomes 'Reina, Ollie and Rachel, but
    ['Stephen', 'Dar'] become 'Stephen and Dar'
    """
    my_string = ''
    if len(my_list) == 1:
        my_string = my_list.pop()
    else:
        while len(my_list) >= 2:
            my_list.reverse()
            my_string += my_list.pop() + ', '
            my_list.reverse()
        while len(my_list) == 1:
            my_list.reverse()
            my_string += 'and ' + my_list.pop()
            my_list.reverse()
    return my_string

my_list = ['Reina', 'Ollie', 'Rachel']
my_list = return_string(my_list)
print my_list

my_list = ['Stephen', 'Dar']
my_list = return_string(my_list)
print my_list

my_list = ['Stephen']
my_list = return_string(my_list)
print my_list


