from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.responses('Hello, world!'.encode('utf-8'))
        self.send_response(200,"Hello, world!")
        return