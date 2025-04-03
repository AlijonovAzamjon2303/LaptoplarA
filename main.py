from app import FrameWorkApp

app = FrameWorkApp()

@app.route("/home")
def home(request, response):
    response.text = "Home pagedan alangali salom!"

@app.route("/about")
def about(request, response):
    response.text = "About pagedan alangali salom!"

"""
{
    "/home":home,
    "/about":about   
}
"""