from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

#temp location of the list for enpoint interaction | this will be returned on the post endpoint
posts: list[dict] = [
    {
      "id" : 1,
      "author" : "Corey Schafer",
      "title" : "Fast Api is awesome",
      "content" : "This framework is really easy to use and super fast",
      "date_posted": "April 20, 2026",
    },
    {
      "id" : 2,
      "author" : "Jane Doe",
      "title" : "Python is great for web development",
      "content" : "Python is a great language for web development, and FastAPI makes it even better",
      "date_posted": "April 21, 2026"
    },
]
# to convert from JSON to HTML Response we need to add the HTML response class
@app.get("/", response_class=HTMLResponse, include_in_schema=False) # the include in schema param tells the fastsapi whether to include an endpoint within the docs or not | this is ideal when we don't want to include endpoints that return html content
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    #returning an HTML String
    return f"<h1>{posts[0]['title']}</h1>"


# we'll create a snippet that will hold dummy data for now
@app.get("/api/posts")
def get_posts():
    return posts
    #in this case FastAPI will automatically convert that list of dictionary into a JSON array

#what if we want to reeturn an html page as a response 
#first we need to import the HTML response from fastAPI. -> from fastapi.responses import HTMLResponse
