__author__ = 'darwright'
out_filename = 'years_as_strings.txt'
year = 1899

with open(out_filename, 'w') as save_file:
    while year < 2016:
        save_file.write("(\'{}\'), ".format(year))
        year += 1