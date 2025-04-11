from app import FrameWorkApp
import json

app = FrameWorkApp()

def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)

    return users

@app.route("/home")
def home(request, response):
    with open("id.json", "r") as file:
        cnt = json.load(file)
    cnt += 1

    response.text = f"Home pagedan alangali salom! -> {cnt}"

    with open("id.json", "w") as file:
        json.dump(cnt, file)

@app.route("/about")
def about(request, response):
    response.text = "About pagedan alangali salom!"

@app.route("/u/{login}")
def get_info(request, response, d):
    users = load_users()
    user = users.get(d.get("login", -1), "Bunday user yo'q!")

    response.text = json.dumps(user)

@app.route("/admin/{login}")
def get_admin(request, response, d):
    response.text = f"Admin page {d.get("login", -1)}"

"""
{
    "/home":home,
    "/about":about   
}
"""