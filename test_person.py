from Tools.person import Person
# from DIRECTORY.FILE  import CLASS NAME
# do not need the file extension
# pycharm needs a __init__.py file in the directory you want to import things from
from Tools.primeFinder import checkIfPrime

dar = Person()
dar.set_default()
print dar.name, dar.age, dar.job
print '\033[0;34m', dar.name, '\033[0;36m', dar.age, '\033[0;31m', dar.job, '\033[0m'
print "\033[0;34m {0} \033[0;36m {1} \033[0;31m {2} \033[0m".format(dar.name, dar.age, dar.job)
# "We have {0} hectares planted to {1}.".format(49, "okra")
print dar.name, dar.age, dar.job
print "Is %s's age a prime number?" % dar.name, checkIfPrime(dar.age)

