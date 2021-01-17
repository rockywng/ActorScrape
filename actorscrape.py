import imdb
ia = imdb.IMDb()

# Obtain name of actor from user
name = input("Enter the name of the actor you'd like to look up:")

# Search for persons data
search = ia.search_person(name)

# Find actor id
id = search[0].personID

# Use id to get persons full set of information
full_person = ia.get_person(id, info=["filmography"])

# Get dictionary of actor's filmography
movies = full_person["filmography"].get('actor')

# Create movie_list list
movie_list = []

# Add movie titles from dictionary to list
for x in movies:
    movie_list.append(x['title'])

# Isolate first element of list
first = movie_list.pop(0)

# Isolate last element of list
last = movie_list.pop(-1)

# Join middle elements of list with commas
middle = ', '.join(movie_list)\

# Build final statement
statement = name + " has appeared in "
statement += first + ", " + middle
statement += " and " + last + "."
statement = statement.replace("(", "")
statement = statement.replace(")", "")

# Produce final statement
print(statement)
    
