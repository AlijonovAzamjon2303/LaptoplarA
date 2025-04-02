class FrameWorkApp:
    def __call__(self, environ, start_response):
        status = "200 OK"
        headers = [("Content-type", "text/html")]

        start_response(status, headers)

        return [b"Salom Salimjon, gamelar qanday ?"]