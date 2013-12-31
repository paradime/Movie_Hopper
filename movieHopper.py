
class Movie:
    __slots__=('title', 'times', 'duration')

    def __str__(self):
        result = 'Title: '
        result += self.title + ' Times: '
        for time in self.times:
            result += str(time) + ', '
        result += 'Duration: ' + str(self.duration)
        return result

def mkMovie(title, times, duration):
    newMovie = Movie
    newMovie.title = title
    newMovie.times = times
    newMovie.duration = duration
    return newMovie

def timeToInt(time):
    element = time.split()
    time = int(element[0]) * 60
    time += int(element[1])
    return time;
    
def main():
    inp = ""
    #1 - end of movie input
    #2 - end of time inpu
    print("1 for end of movie input, 2 for end of time input")
    movies = []
    while(inp != "1"):
        inp = input("Enter title: ")
        if (inp != "1"):
            title = inp
            inp = input("Enter duration (minutes): ")
            dur = int(inp)
            times = []
            while(inp !="2"):
                inp = input("Enter time (hr min): ")
                if(inp != "2"):
                    time = timeToInt(inp)
                    times.append(time)
            newMovie = mkMovie(title, times, dur)
            movies.append(newMovie)
            print(newMovie.__str__(newMovie))

main()
            
        
