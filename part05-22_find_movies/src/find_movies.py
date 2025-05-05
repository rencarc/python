def find_movies(database: list, search_term: str):

    search_term_lower = search_term.lower()
    

    matching = [
        movie for movie in database if search_term_lower in movie["name"].lower()
    ]
    
    return matching