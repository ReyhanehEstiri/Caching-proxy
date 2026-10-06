from http.server import BaseHTTPRequestHandler, HTTPServer


class ProxyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("Request received:", self.path)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello from caching proxy!")


server = HTTPServer(("localhost", 3000), ProxyHandler)

print("Caching proxy running on http://localhost:3000")

server.serve_forever()