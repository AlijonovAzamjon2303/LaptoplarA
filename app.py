from webob import Request, Response
from parse import parse

class FrameWorkApp:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ, start_response)

    def handle_request(self, request):
        res = Response()

        for path, handler in self.routes.items():
            if path == request.path:
                handler(request, res)
            else:
                parsed = parse(path, request.path)
                if parsed is not None:
                    handler(request, res, parsed.named)

        return res

    def route(self, path):
        if path in self.routes:
            raise KeyError("Qisqasi URL da xatolik bor")
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper