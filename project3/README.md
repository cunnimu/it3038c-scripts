# Project 3
## Art Finder

This is a simple flask app that searches for artwork using the [Art Institute of Chicago's API](https://api.artic.edu/docs/#introduction)
## Background

My goal with this was to build on some of the lessons in the course. I hadn't yet done a project with python, so I wanted to build something with that. I looked over the course materials. I decided to make a flask app that calls a third party API. I liked the Art Institute of Chicago's API and thought it looked like fun. Everyone should spend more time appreciating great art, right?
## Setup

To run this app, download the project code to your machine. 
Note: I am giving commands for Linux. If you are using Powershell, it will be similar but might not be the same. ie: use `python` in place of `python3`.

Create & start a virtual environment:
```
python3 -m venv venv 
. venv/bin/activate 
```

In your environment, use:
```
pip install -r requirements.txt
```
to ensure you have downloaded flask and the extensions necessary to run this project (Flask, requests)

To start:
```
python3 main.py
```

## Project Structure


This is the structure in flask. The `main.py` file starts the program. The `routes.py` file contains the different routes  The templates folder holds the code for the different pages. 

The search term is entered into the form on the index page:
```
<input type="text" class="form-control" id="query" name="query" placeholder="for example: space">
```

This is then used on  `routes.py`:
```
# The results page:
@app.route('/results',methods=['POST'])
def results():
    if request.method == 'POST':
        # Get the search term from the form on the index page
        query = request.form['query']
```
The route specifies the `results` page and the `POST` method. The `query` is the search term from the form. Next, this is used in the API call.
### Search Results

You can search for any term you like to see this in action. Try: space, cats, robots, ohio...you will get artwork from various mediums. Because it searches the metadata, some will be more relevant to your interests than others. But that is okay: art is subjective and you can appreciate it regardless.

The API call looks like this:
```
r = requests.get(f"https://api.artic.edu/api/v1/artworks/search?q={query}&fields=id,title,image_id,artist_title")
results = r.json()
```
See [the documentation](https://api.artic.edu/docs/#quick-start) for more information on how to call the API. The `query` is the search term.


## Additional Resources

For more information on the tools used, please see:
 - [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
 - [Art Institute of Chicago API Documentation](https://api.artic.edu/docs)
 - [Art Institute of Chicago Public API Talk](https://www.youtube.com/watch?v=1YAFJdXZiC8) - video on Chi Hack Night youtube; gives background on the API
