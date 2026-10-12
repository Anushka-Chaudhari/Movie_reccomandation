from dataclasses import dataclass


@dataclass(frozen=True)
class Song:
    title: str
    artist: str
    genre: str
    moods: tuple[str, ...]
    activities: tuple[str, ...]


SONGS = [
    Song("Blinding Lights", "The Weeknd", "pop", ("energetic", "happy"), ("workout", "travel")),
    Song("Levitating", "Dua Lipa", "pop", ("happy", "energetic"), ("party", "workout")),
    Song("Shape of You", "Ed Sheeran", "pop", ("happy", "relaxed"), ("travel", "study")),
    Song("Believer", "Imagine Dragons", "rock", ("energetic", "motivated"), ("workout", "travel")),
    Song("Thunder", "Imagine Dragons", "rock", ("energetic", "happy"), ("workout", "party")),
    Song("Perfect", "Ed Sheeran", "romance", ("romantic", "relaxed"), ("relax", "travel")),
    Song("All of Me", "John Legend", "romance", ("romantic", "sad"), ("relax", "study")),
    Song("Someone Like You", "Adele", "pop", ("sad", "relaxed"), ("relax", "study")),
    Song("Lose Yourself", "Eminem", "hip-hop", ("motivated", "energetic"), ("workout", "study")),
    Song("Sunflower", "Post Malone & Swae Lee", "hip-hop", ("happy", "relaxed"), ("travel", "relax")),
    Song("Weightless", "Marconi Union", "instrumental", ("relaxed",), ("study", "relax")),
    Song("River Flows in You", "Yiruma", "instrumental", ("relaxed", "sad"), ("study", "relax")),
    Song("Can't Stop the Feeling!", "Justin Timberlake", "pop", ("happy", "energetic"), ("party", "workout")),
    Song("Counting Stars", "OneRepublic", "pop", ("motivated", "happy"), ("travel", "workout")),
]


def recommend_songs(mood: str, activity: str, genre: str) -> list[tuple[Song, int]]:
    """Rank songs using simple points for matching mood, activity, and genre."""
    ranked = []
    for song in SONGS:
        score = 0
        if mood in song.moods:
            score += 2
        if activity in song.activities:
            score += 2
        if genre != "any" and genre == song.genre:
            score += 1
        if score:
            ranked.append((song, score))
    return sorted(ranked, key=lambda item: (-item[1], item[0].title))


def choose(prompt: str, options: tuple[str, ...]) -> str:
    """Ask until the user enters one of the displayed choices."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print("Please choose one of:", ", ".join(options))


def main() -> None:
    moods = ("happy", "sad", "relaxed", "energetic", "romantic", "motivated")
    activities = ("study", "workout", "travel", "party", "relax")
    genres = ("any", "pop", "rock", "romance", "hip-hop", "instrumental")

    print("\n=== Rule-Based Song Recommendation System ===")
    print("Tell me how you feel and what you are doing. I'll suggest songs!\n")
    mood = choose(f"Choose a mood ({', '.join(moods)}): ", moods)
    activity = choose(f"Choose an activity ({', '.join(activities)}): ", activities)
    genre = choose(f"Choose a genre ({', '.join(genres)}): ", genres)

    results = recommend_songs(mood, activity, genre)
    print("\nRecommended songs:")
    for song, score in results[:5]:
        print(f"- {song.title} — {song.artist} (match score: {score})")
    if not results:
        print("No matches found. Try a different mood, activity, or genre.")


if __name__ == "__main__":
    main()
