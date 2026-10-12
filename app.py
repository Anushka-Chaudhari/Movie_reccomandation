from flask import Flask, render_template, request

from song_recommendation import recommend_songs

app = Flask(__name__)
MOODS = ("happy", "sad", "relaxed", "energetic", "romantic", "motivated")
ACTIVITIES = ("study", "workout", "travel", "party", "relax")
GENRES = ("any", "pop", "rock", "romance", "hip-hop", "instrumental")


@app.route("/", methods=["GET", "POST"])
def index():
    selections = {"mood": "", "activity": "", "genre": "any"}
    recommendations = []
    searched = False

    if request.method == "POST":
        selections = {
            "mood": request.form.get("mood", "").strip().lower(),
            "activity": request.form.get("activity", "").strip().lower(),
            "genre": request.form.get("genre", "any").strip().lower(),
        }
        if selections["mood"] in MOODS and selections["activity"] in ACTIVITIES and selections["genre"] in GENRES:
            recommendations = recommend_songs(**selections)[:5]
            searched = True

    return render_template(
        "index.html",
        moods=MOODS,
        activities=ACTIVITIES,
        genres=GENRES,
        selections=selections,
        recommendations=recommendations,
        searched=searched,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
