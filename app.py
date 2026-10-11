from flask import Flask, render_template, request

from miniproject import movies, recommend_movies

app = Flask(__name__)
genres = sorted({movie["genre"] for movie in movies})


@app.route("/", methods=["GET", "POST"])
def index():
    selected_genre = ""
    recommendations = []
    searched = False

    if request.method == "POST":
        selected_genre = request.form.get("genre", "").strip().lower()
        searched = True
        if selected_genre in genres:
            recommendations = recommend_movies(selected_genre)

    return render_template(
        "index.html",
        genres=genres,
        selected_genre=selected_genre,
        recommendations=recommendations,
        searched=searched,
    )


if __name__ == "__main__":
    app.run(debug=True)
