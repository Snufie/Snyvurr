from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):

    def do_GET(self, email, password):
        self.send_response(200)
        return