from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen

from cache import Cache


ORIGIN = "https://dummyjson.com"

cache = Cache()


class ProxyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        cache_key = self.path

        cached_response = cache.get(cache_key)

        if cached_response is not None:
            print("Cache HIT:", cache_key)

            self.send_response(200)
            self.send_header("Content-Type", cached_response["content_type"])
            self.send_header("X-Cache", "HIT")
            self.end_headers()

            self.wfile.write(cached_response["body"])
            return

        print("Cache MISS:", cache_key)

        origin_url = ORIGIN + self.path

        print("Forwarding request to:", origin_url)

        request = Request(
            origin_url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        with urlopen(request) as response:
            body = response.read()
            content_type = response.headers.get(
                "Content-Type",
                "text/plain"
            )

        cache.set(
            cache_key,
            {
                "body": body,
                "content_type": content_type
            }
        )

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("X-Cache", "MISS")
        self.end_headers()

        self.wfile.write(body)


server = HTTPServer(("localhost", 3000), ProxyHandler)

print("Caching proxy running on http://localhost:3000")

server.serve_forever()