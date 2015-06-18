import time
import datetime


STARTTIME = time.time()


class StopWatch:
    def __init__(self):
        global STARTTIME
        ui()

    def starttime(self):
        global STARTTIME
        STARTTIME = time.time()
        return STARTTIME

    def stoptime(self):
        # global ENDTIME
        endtime = time.time()
        return endtime

    def time_between(self, endtime, starttime):
        # global STARTTIME, ENDTIME
        time_between = endtime - starttime
        return time_between()

    def format_time(self,new_time):
        st = datetime.datetime.fromtimestamp(new_time).strftime('%Y-%m-%d %H:%M:%S')
        return st

    def ui(self):
        global STARTTIME
        while True:
            choice = raw_input( 'Welcome to the stop watch!\n'
                                'Enter a command:\n'
                                '~~~~~~~~~~~~~~~~'
                                '1 to START!\n'
                                '2 to STOP\n'
                                '3 to quit'
                                '>> ')
            if choice == 1:
                STARTTIME = starttime()
            elif choice == 2:
                stop = stoptime()
                time_passed = time_bewtween(stop, STARTTIME)
                format_timepassed = format_time(time_passed)
                print format_timepassed, "has passed."
            else:
                print "Thank you for using my stopwatch!"
                exit()


StopWatch()
