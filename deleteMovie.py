from data import *

def delete_movie():
    print("----------DELETE MOVIE ----------")

    print("---------AVAILABLE MOVIES---------")
    for movie in movies_list:
        print("--- ", movie.title)

    delete_movie_name = input("Please enter movie name to be deleted : ")
    success_flag = False

    # iterate through the movie list to find movie is present or not
    for i in movies_list:

        if i.title == delete_movie_name:
            movies_list.remove(i)
            success_flag = True
            print("MOVIE DELETED SUCCESSFULLY!!")
            break

    if not success_flag:
        print("PLEASE ENTER CORRECT MOVIE NAME TO BE DELETED !!")

