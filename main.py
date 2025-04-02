from wsgiref.simple_server import make_server

from app import FrameWorkApp

app = FrameWorkApp()

server = make_server("localhost", 8000, app)
server.serve_forever()