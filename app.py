from flask import Flask, render_template
app = Flask(__name__)


# Define the home page route
@app.route("/spotify_clone")
def hello():
    return render_template("pq.html")

if __name__ == "__main__":
    app.run(debug=True)
