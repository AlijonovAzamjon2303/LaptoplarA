from webob import Request, Response

class FrameWorkApp:
    def __call__(self, environ, start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ, start_response)

    def handle_request(self, request):
        user_agent = request.environ.get("HTTP_USER_AGENT", "Topilmadi")
        res = Response()
        res.text = f"Men handlerdan qaytyapman, sen {user_agent}"

        return res