from app import FrameWorkApp
import json

app = FrameWorkApp()

def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)

    return users

@app.route("/home")
def home(request, response):
    response.text = "Home pagedan alangali salom!"

@app.route("/about")
def about(request, response):
    response.text = "About pagedan alangali salom!"

@app.route("/u/{id}")
def get_info(request, response, id):
    users = load_users()
    user = users.get(id, "Bunday user yo'q!")

    response.text = json.dumps(user)

"""
{
    "/home":home,
    "/about":about   
}
"""