import sqlite3


def search_by_title(query):
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
    with sqlite3.connect('./netflix.db') as connection:
        cur = connection.cursor()

        sqlite_query = f"""
        SELECT title, rating, description
        FROM netflix        
        LIMIT 100
        """

    cur.execute(sqlite_query)
    raw_data = cur.fetchall()

    result = []
    for movie in raw_data:
        if rating == 'children':
            sqlite_query += "WHERE rating='G'"
        elif rating == 'family':
            sqlite_query += "WHERE rating='G' or rating='PG' or rating='PG-13"
        elif rating == 'adult':
            sqlite_query += "WHERE rating='R' or rating='NC-17'"
