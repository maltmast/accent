import http.server
import socketserver
import os
import webbrowser as wb


PORT = 8000
DIRECTORY = os.getcwd()

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        try:
            wb.open_new_tab(f"http://localhost:{PORT}")
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()