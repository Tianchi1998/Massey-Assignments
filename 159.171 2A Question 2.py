#Define a function which loads file of movie titles.
def load():
    global movies_list
    file_name = input("The name of a file: ")
    if file_name == "":
        file_name = "movies.txt"
    file = open("%s" % (file_name), "r")
    movies_list = file.readlines()
    file.close()
    movies_list = [movie.strip() for movie in movies_list]

#Define a function which creates a random movie title.
def random():
    global movie1
    import random
    movie1 = random.choice(movies_list)
    print(movie1)

#Define a function which searches for certain strings.
def search():
    global movie1
    key_word1 = input("The string 1: ")
    key_word2 = input("The string 2: ")
    for i in movies_list:
        if key_word1 == "":
            movie1 = ""
            break
        elif key_word2 == "":
            if key_word1 in i:
                print(i,"\n")
                movie1 = i
        elif key_word1 in i and key_word2 in i:
            print(i,"\n")
            movie1 = i
        else:
            continue

#Define a function which searches for movie titles that start with a certain string.
def starts_with():
    global movie1
    key_word = input("The string: ")
    if key_word == "":
        print(end="")
        movie1 = ""
    else:
        for i in movies_list:
            if i.startswith(key_word):
                print(i,"\n")
                movie1 = i


favourites_list = []
#Define a function that saves the last displayed movie title to the list.
def keep():
    if movie1 == "":
        global favourites_list
        favourites_list = favourites_list
    else:
        favourites_list.append(movie1)

#Define a function that displays the favourites list.
def favourites_display():
    print(favourites_list)

#Define a function that clears the list.
def clear_favourites():
    global favourites_list
    favourites_list = []

#This function uses all the functions above to build a movie title explorer
#   which we need in this question.
def movie_title_explorer():
    print("""*** Movie Title Explorer ***
       l - load file of movie titles
       r - random movie
       s - search
       sw - starts with
       k - keep - save the last displayed movie title to your favourites
       f - favourites display
       c - clear favourites
       q - quit""")
    command=input("command(Please type l when you first use it): ")
    if command == "l":
        load()
        movie_title_explorer()
    elif command == "r":
        random()
        movie_title_explorer()
    elif command == "s":
        search()
        movie_title_explorer()
    elif command == "sw":
        starts_with()
        movie_title_explorer()
    elif command == "k":
        keep()
        movie_title_explorer()
    elif command == "f":
        favourites_display()
        movie_title_explorer()
    elif command == "c":
        clear_favourites()
        movie_title_explorer()
    elif command == "q":
        print()

#Now , we call the function.
movie_title_explorer()
