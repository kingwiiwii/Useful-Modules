''' Function to convert the time to human readable'''
''' add import timeConverter to top of script using this module '''
''' usage example - print "RunTime -", time_readable(RunTime) '''

import time

def time_readable(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    if (secs) < 1:
        return "Less than a second"
    else:
        return '%02d:%02d:%02d' % (hours, mins, secs)


