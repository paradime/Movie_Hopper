"""
Movie Class used by Movie Hopper application
Author: Bryon Wilkins
"""
class Movie(object):
    """
    title       - string (title of movie)
    times       - list of ints (times that the movies will be playing)
    duration    - int (duration of movie)
    """
    __slots__=('title', 'times', 'duration')

    def __init__(self, title, times, duration):
        self.title = title
        self.times = times
        self.duration = duration

    def __str__(self):
        result = "Title: "
        result += self.title + " Times: "
        for time in self.times:
            result += intToTime(time) + ", "
        result += "Duration: " + str(self.duration)
        return result

    """
    Clean function for getting the end time of a movie
    @param
    startTime - int(the chosen start time for a movie)
    @return
    returns the time it expects the movie to be over
    """
    def getEndTime(self, startTime):
        return startTime + self.duration

    """
    @param
    self - movie object
    start - int (earliest that you can be to the movie)
    @return
    Returns an int which is the earliest movie time larger than start
    -1 - no more times
    """
    def getEarliestStart(self, start):
        earliest = 1440 #The maximum number of minutes in one day
        for time in self.times:
            #Compare each time to start and the earliest
            #return the number 
            if(start < time and earliest > time):
                earliest = time
        if(earliest == 1440):
            earliest = -1
        return earliest