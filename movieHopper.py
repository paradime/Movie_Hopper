"""
Movie Hopper Application for finding the most efficient order to watch movies at a theater
when hopping
Author: Bryon Wilkins
"""
from copy import deepcopy

class Movie(object):
    """
    title       - string (title of movie)
    times       - list of ints (times that the movies will be playing)
    duration    - int (duration of movie)
    """
    __slots__=('title', 'times', 'duration')

    """
    @params
    title - string (title of movie)
    times - list of ints (times movie will be playing)
    duration - int (duration of movie)
    """
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

class MovieMap:
    """
    startNode   - MovieNode (the node the map starts at)
    visited     - list of movies (a list of already visited movies)
    waitTime    - ints (the total time that you are waiting and not watching a movie)
    """
    __slots__=('startNode', 'visited', 'waitTime')

    def __init__(self, startNode):
        self.startNode = startNode
        self.waitTime = 0
        self.visited = []
        self.visited.append(startNode.movie)

    """
    Fills the current map with nodes
    """
    def fillMap(self):
        tempVis = deepcopy(self.visited)
        curNode = self.startNode
        while(curNode is not None):
            curNode.next = curNode.nextNode(self.visited)
            curNode = curNode.next
            tempVis = deepcopy(self.visited)

class MovieNode:
    """
    next - next movie in list
    movie - movie (corresponding movie)
    startTime - int (start time of this movie)
    movies - list of all movies
    """
    __slots__=('next', 'movie', 'startTime', 'movies')

    def __init__(self, movie, startTime, movies):
        self.movie = movie
        self.startTime = startTime
        self.movies = movies
        self.next = None

    def __str__(self):
        result = "\n"
        result += self.movie.title + " at \t" + intToTime(self.startTime) + ". "
        if(self.next is not None):
            result += "Followed by " + str(self.next)
        return result

    """
    visited - list of visited movies
    returns the next Earliest movie that isn't in visited
    """
    def nextNode(self, visited):
        for movie in self.movies:
            if(visited.count(movie) == 0):
                earliestStart = movie.getEarliestStart(self.movie.getEndTime(self.startTime))
                visited.append(movie)
                nextNode = MovieNode(movie, earliestStart, self.movies)
                return nextNode
        return None

"""
@para
time - string (Military time represent "hr mn")
@return
returns a numeric representation of minutes after midnight this time is 
"""
def timeToInt(time):
    element = time.split()
    result = int(element[0]) * 60
    result += int(element[1])
    return result

"""
@param
time - int (int representation of minutes past midnight)
@return
string - military time representation (hr mn)
"""
def intToTime(time):
    result = str(int(time/60))
    if(time%60 < 10):
        result += " 0" + str(time%60)
    else:
        result += " " + str(time%60)
    return result

    
def main():
    inp = ""
    #1 - end of movie input
    #2 - end of time inpu
    print("1 for end of movie input, 2 for end of time input")
    movies = []
    inp = input("Earliest you can be at the Movies? (Military time \"hr mn\")")
    startTime = timeToInt(inp)
    while(inp != "1"):
        inp = input("Enter title: ")
        if (inp != "1"):
            title = inp
            inp = input("Enter duration (minutes): ")
            dur = int(inp)
            times = []
            while(inp !="2"):
                inp = input("Enter military time (hr min): ")
                if(inp != "2"):
                    time = timeToInt(inp)
                    times.append(time)
            newMovie = Movie(title, times, dur)
            print("\n" + str(newMovie))
            movies.append(newMovie)
    startNode = MovieNode(movies[0], movies[0].getEarliestStart(startTime), movies)
    movieMap = MovieMap(startNode)
    movieMap.fillMap()
    print("\nEarliest movie you can make: " + str(movieMap.startNode))

main()
            
        
