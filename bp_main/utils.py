import sqlite3


def search_by_title(query):
    """
    search by request
    :param query: query is str
    :return: movie list
    """
    with sqlite3.connect('./netflix.db') as connection:
        cur = connection.cursor()

        sqlite_query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title LIKE "%{query}%"
        ORDER BY release_year DESC
        LIMIT 1
        """

    cur.execute(sqlite_query)
    raw_data = cur.fetchall()
    # print(raw_data)
    return {
        "title": raw_data[0][0],
        "country": raw_data[0][1],
        "release_year": raw_data[0][2],
        "genre": raw_data[0][3],
        "description": raw_data[0][4]
    }


# print(search_by_title("Roxy"))


def search_by_release_year(first_year, second_year):
    """
    Search by release years
    :param first_year: int
    :param second_year: int
    :return: movie list
    """
    with sqlite3.connect('./netflix.db') as connection:
        cur = connection.cursor()

        sqlite_query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {first_year} AND {second_year}
        LIMIT 100
        """

    cur.execute(sqlite_query)
    raw_data = cur.fetchall()

    result = []
    for element in raw_data:
        movie = {
            "title": element[0],
            "release_year": element[1]
        }
        result.append(movie)
    return result


def search_by_rating(rating):
    """
    search by rating
    :param rating: str
    :return: movie list by rating request
    """
    with sqlite3.connect('./netflix.db') as connection:
        cur = connection.cursor()

        sqlite_query = f"""
        SELECT title, rating, description
        FROM netflix        
        """

    if rating == 'children':
        sqlite_query += "WHERE rating='G'" \
                        "LIMIT 10"
    elif rating == 'family':
        sqlite_query += "WHERE rating='G' or rating='PG' or rating='PG-13'" \
                        "LIMIT 10"

    elif rating == 'adult':
        sqlite_query += "WHERE rating='R' or rating='NC-17'" \
                        "LIMIT 10"

    cur.execute(sqlite_query)
    raw_data = cur.fetchall()

    result = []
    for element in raw_data:
        movie = {
            "title": element[0],
            "rating": element[1],
            "description": element[2]
        }
        result.append(movie)
    return result


def search_by_genre(genre):
    """
    search by genre
    :param genre: str
    :return: movie list by genre request
    """
    with sqlite3.connect("./netflix.db") as connection:
        cur = connection.cursor()

        sqlite_query = f"""
                        SELECT title, description
                        FROM netflix
                        WHERE listed_in LIKE "%{genre.lower()}%" 
                        ORDER BY release_year DESC
                        LIMIT 10 
        """

    cur.execute(sqlite_query)
    raw_data = cur.fetchall()

    result = []

    for i in raw_data:
        movie = {
            "title": i[0],
            "description": i[1]
        }
        result.append(movie)
    return result


def get_pair_actor(first_actor, second_actor):
    with sqlite3.connect("../netflix.db") as connection:
        cur = connection.cursor()

        sqlite3_query = f"""
                          SELECT `cast`
                          FROM netflix 
                          WHERE `cast` LIKE "%{first_actor}%"
                          AND `cast` LIKE "%{second_actor}%" 
        """

    cur.execute(sqlite3_query)
    data = cur.fetchall()

    actors = []
    unique_actors = set()

    for movie in data:
        # print(movie)
        for element in movie:
            # print(element)
            # print(type(element))
            for name in element.split(','):
                actors.append(name)

    for element in actors:
        if actors.count(element) > 2:
            unique_actors.add(element)

    return list(unique_actors)


# print(get_pair_actor("Rose McIver", "Ben Lamb"))

def search_by_type(type_film, genre, year):
    with sqlite3.connect("../netflix.db") as connection:
        cur = connection.cursor()

        sqlite3_query = f"""
                          SELECT title, description, type, listed_in, release_year
                          FROM netflix 
                          WHERE netflix.type LIKE "%{type_film}%"
                          AND netflix.listed_in LIKE "%{genre}%" 
                          AND release_year={year}
        """

    cur.execute(sqlite3_query)
    data = cur.fetchall()

    movies = []
    for element in data:
        movie = {
            "title": element[0],
            "description": element[1]
        }
        movies.append(movie)
    return movies
