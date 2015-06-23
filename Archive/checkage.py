def checkage(age):
    """
    usage: checkage(age)
    If age is less than 18 will return a False response
    If age is greater than or equal too, will return a True response
    """
    if age < 18:
        return False
    elif age >= 18:
        return True

age = checkage(2)
print age