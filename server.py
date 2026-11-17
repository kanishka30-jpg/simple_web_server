import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as server:
    print("Webserver running at port", PORT)
    server.serve_forever()
