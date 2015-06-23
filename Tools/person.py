class Person(object):
    def __init__(self):
        """
        balsjlakjdkjsda
        :return:
        """
        self.name = ''
        self.age = 0
        self.job = ''

    def set_name(self):
        self.name = raw_input("Name: ")

    def set_age(self):
        self.age = int(raw_input("Age: "))

    def set_job(self):
        self.job = raw_input("Job: ")

    def set_default(self):
        self.name = 'Dar'
        self.age = 33
        self.job = 'QA Tech of DOOOOM!'

