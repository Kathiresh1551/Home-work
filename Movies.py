myMoviesList = ["friends", "starnger things", "money heist", "witcher", "peaky blinders", "dark"]
friendMoviesList = []
errorMessage = 0
commonMovies = []

friendMovies = int(input("enter no of movies: "))
for friendMovies in range (0, friendMovies):
    moviesList = input("Enter movies: ")
    friendMoviesList.append(moviesList)
for myIndex in range (len(myMoviesList)):
    for friendIndex in range (len(friendMoviesList)):
        if (myMoviesList[myIndex] == friendMoviesList[friendIndex]):
            commonMovies.append(friendMoviesList[friendIndex])
for index in range (len(commonMovies)):        
    print(index+1, commonMovies[index])
if (len(commonMovies) == 0):
    print("nothing matches")






# for myMovies in range (len(myMoviesList)):
#     for friendMovies in range (len(friendMovieList)):
#         if (friendMovieList[friendMovies] == myMoviesList[myMovies]):
#             print(friendMovies)