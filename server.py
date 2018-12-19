import http.server
import socketserver
from http import HTTPStatus
from datetime import datetime

HTTP_PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world\n')
        self.wfile.write(str(datetime.now()).encode())

httpd = socketserver.TCPServer(('', HTTP_PORT), Handler)
print("server started on ", HTTP_PORT)
httpd.serve_forever()

