"""
Movie Hopper Application for finding the most efficient order to watch movies at a theater
when hopping
Author: Bryon Wilkins
"""
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

class MovieNode:
    """
    neighbors   - list of nodes
    movie       - movie (corresponding movie)
    """
    __slots__=('neighbors', 'movie')

"""
@param
movies - list of movies
movie - movie object (your start node for this map)
startTime - int (the earliest time you can make it to the movies)
@return
MovieMap object with start state as movie parameter.
    startTime should determine what time of movie should be used
    Should be a map where each node is directed towards
        the EARLIEST start time of a movie that isn't 
        already visited
    Node neighbors should be extracted from movies
"""
def mkMovieMap(movies, movie, startTime):
    #Currently Unimplemented
    newMap = MovieMap
    newMap.visited = [movie]
    startNode = mkMovieNode(movies, movie, startTime, newMap)

"""
@param
movies - list of movies (all movies)
movie - movie object (our node's data)
startTime - int (the earliest time we can make it to this movie)
myMap - MovieMap object (does not need to be complete)
@return
MovieNode object where movie is same as parameter
    Neighbors should be based on this algorithm:
        startTime + movie.duration 
"""
def mkMovieNode(movies, movie, startTime, myMap):
    #Currently Unimplemented
    newNode = MovieNode
    newNode.movie = movie
    for mov in movies:
        if myMap.visited.count(mov) == 0:
            myMap.visited.append(mov)

"""
@parameter
movieMap - fully constructed MovieMap
@return
a list of enums? (Movie, startTime)
"""
#def dijkstra(movieMap):
    #currently unimplemented

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
    print("\nEarliest movie you can make: " + intToTime(movies[0].getEarliestStart(startTime)))

main()
            
        
