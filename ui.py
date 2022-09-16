from objects import movie_database

def displayMenu():
    print("COMMAND MENU")
    print("cat   - View movies by category")
    print("year  - View movies by year")
    print("add   - Add a movie")
    print("del   - Delete a movie")
    print("exit  - Exit program")
    print()

def displayCategories():
    print("CATEGORIES")
    print("1. Animation")
    print("2. Comedy")
    print("3. History")
    print()

def main():

    # USE YOUR OWN FILE PATH TO THE DATABASE
    file_path = 'C:/Users/Admin/Documents/Development/python_scripts/week_13/movies.db'

    database = movie_database(file_path)

    print("The Movie List program")
    displayMenu()
    displayCategories()

    while (True):
        command = input("Command: ").strip()

        if (command == "cat"):
            database.view_by_category()
        elif (command == "year"):
            database.view_by_year()
        elif (command == "add"):
            database.insert_movie()
        elif (command == "del"):
            database.delete_movie()
        elif (command == "exit"):
            break

        print()

if __name__ == "__main__":
    main()
