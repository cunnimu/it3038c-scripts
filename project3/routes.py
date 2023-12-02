from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config.from_object(__name__)

# The index page:
@app.route('/')
def hello():
    return render_template("index.html")

# The results page:
@app.route('/results',methods=['POST'])
def results():
    if request.method == 'POST':
        # Get the search term from the form on the index page
        query = request.form['query']

        # Call the api and search for the query
        r = requests.get(f"https://api.artic.edu/api/v1/artworks/search?q={query}&fields=id,title,image_id,artist_title")
        results = r.json()

    # Pass the data to the results page
    return render_template("results.html", results = results['data'], query = query)