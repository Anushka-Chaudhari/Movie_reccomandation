movies = [
    {"title": "The Dark Knight", "genre": "action"},
    {"title": "Mad Max: Fury Road", "genre": "action"},
    {"title": "Inception", "genre": "sci-fi"},
    {"title": "Interstellar", "genre": "sci-fi"},
    {"title": "The Hangover", "genre": "comedy"},
    {"title": "Home Alone", "genre": "comedy"},
    {"title": "The Notebook", "genre": "romance"},
    {"title": "Pride and Prejudice", "genre": "romance"},
    {"title": "The Conjuring", "genre": "horror"},
    {"title": "A Quiet Place", "genre": "horror"},
]


def recommend_movies(preferred_genre: str) -> list[str]:
    """Return movie titles matching the user's preferred genre."""
    genre = preferred_genre.strip().lower()
    return [
        movie["title"]
        for movie in movies
        if movie["genre"] == genre
    ]


def main() -> None:
    available_genres = sorted({movie["genre"] for movie in movies})
    print("Welcome to the Movie Recommendation System!")
    print("Available genres:", ", ".join(available_genres))

    preferred_genre = input("What genre would you like to watch? ")
    recommendations = recommend_movies(preferred_genre)

    if recommendations:
        print("\nRecommended movies:")
        for title in recommendations:
            print(f"- {title}")
    else:
        print("Sorry, there are no movies for that genre.")
        print("Please choose one of the genres listed above.")


if __name__ == "__main__":
    main()