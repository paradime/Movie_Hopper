"""
Movie Hopper Application for finding the most efficient order to watch movies at a theater
when hopping
Author: Bryon Wilkins
"""
from copy import deepcopy
from movie import Movie

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
        result += self.movie.title +" at " + intToTime(self.startTime) + ". "
        if(self.next is not None):
            result += str(self.next)
        return result

    """
    Prints a table for nodes in ascending order
    """
    def printTable(self):
        titleList = []
        timeList = []
        self.fillTitleList(titleList)
        self.fillTimeList(timeList)
        nameJust = intLongestString(titleList)
        print("#:".rjust(2), "Title:".rjust(nameJust), "Time:".rjust(5))
        for i in range(len(titleList)):
            print(str(i + 1).rjust(2), titleList[i].rjust(nameJust), timeList[i].rjust(5))

    """
    Helper function to fill titleList
    @param
    titleList - a list of titles to be filled
    """
    def fillTitleList(self, titleList):
        titleList.append(self.movie.title)
        if(self.next is not None):
            self.next.fillTitleList(titleList)

    """
    Helper function to fill timeList
    @param
    timeList - a list of times to be filled
    """
    def fillTimeList(self, timeList):
        timeList.append(intToTime(self.startTime))
        if(self.next is not None):
            self.next.fillTimeList(timeList)

    """
    @params
    visited - list of visited movies
    @return 
    a new MovieNode that is next in movies and has a time after current movies endTime
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
    if(int(time/60) < 10):
        result = "0" + str(int(time/60))
    else:
        result = str(int(time/60))
    if(time%60 < 10):
        result += " 0" + str(time%60)
    else:
        result += " " + str(time%60)
    return result

"""
@param
stringList - list of strings
@return
int - the length of the longest string in stringList
"""
def intLongestString(stringList):
    length = 0
    for string in stringList:
        if len(string) > length:
            length = len(string)
    return length
    
"""
Main function for MovieHopper
Asks for input
Converts input into a list of paths the user could make
Prints the possible paths that can be taken
"""
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
            movies.append(newMovie)
    startNode = MovieNode(movies[0], movies[0].getEarliestStart(startTime), movies)
    movieMap = MovieMap(startNode)
    movieMap.fillMap()
    print("\nMovie order you can make:")
    movieMap.startNode.printTable()

main()