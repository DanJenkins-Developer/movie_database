from db import create, read, delete, insert

class movie_database:

    def __init__(self, path):
        self.__connection = create(path)
    
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def value(self, connection):
            self.__connection = connection

    def view_by_category(self):

        query = '''select category.name, movies.name from category, movies where category.CategoryID = movies.CategoryID ORDER BY category.CategoryID'''

        results = read(self.connection, query)

        # Print results
        print("Category \tMovie")
        for movie in results:
            print("{} \t{}".format(movie[0], movie[1]))

    def view_by_year(self):

        query = '''select year, name FROM movies ORDER BY year'''

        results = read(self.connection, query)

        # Print results
        print("Year \tMovie")
        for movie in results:
            print("{} \t{}".format(movie[0], movie[1]))

    def insert_movie(self):

        name = input("Name: ").strip()
        year = input("Year: ").strip()
        minutes = input("Minutes: ").strip()
        categoryID = input("Category ID: ").strip()

        query = "INSERT INTO movies (name, year, minutes, CategoryID) VALUES ('{}',{},{},{})".format(name, year, minutes, categoryID)

        insert(self.connection, query)

        print("{} was added to the database".format(name))
    
    def delete_movie(self):

        id = input("Enter the movie to delete: ").strip()
        query = "DELETE FROM movies WHERE name = '{}'".format(id)
        delete(self.connection, query)

        print("Deleted.")