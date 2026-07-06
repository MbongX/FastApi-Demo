from fastapi import FastAPI, Request
#from fastapi.responses import HTMLResponse
#for template -> jinja2 
from fastapi.templating import Jinja2Templates
#access/mounting the static files
from fastapi.staticfiles import StaticFiles

app = FastAPI()
#mounting in the static files
app.mount("/static", StaticFiles(directory="static"), name="static")

#since we are now using template we need to create a template directory (standard convention across FastAPI and Flask)
# we also need to tell fast api on where are we storing our templates -> via a templates obj
templates = Jinja2Templates(directory="templates")



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
#@app.get("/", response_class=HTMLResponse, include_in_schema=False) # the include in schema param tells the fastsapi whether to include an endpoint within the docs or not | this is ideal when we don't want to include endpoints that return html content
#@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
#def home(): 
    #returning an HTML String
 #   return f"<h1>{posts[0]['title']}</h1>"

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request): #we need to add a request paramater as an arguments as this is require by Jinja2
    # we will be return a template via the following 'template.TemplateResponse(request, home.html)'
    # we can also pass in a context dictionary into our templates | variable to render/use within the template in this case we will be using out List Dictionary
    return templates.TemplateResponse(
        request, 
        "home.html", 
        {"posts": posts, "title": "Home"},
        ) # within the parentgesis we pass in the request and the name of the html template


# we'll create a snippet that will hold dummy data for now
@app.get("/api/posts")
def get_posts():
    return posts
    #in this case FastAPI will automatically convert that list of dictionary into a JSON array

#what if we want to reeturn an html page as a response 
#first we need to import the HTML response from fastAPI. -> from fastapi.responses import HTMLResponse
