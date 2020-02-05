from http.server import BaseHTTPRequestHandler
from routes import routes, data
from singleton import data_store
import pyautogui

class Server(BaseHTTPRequestHandler):

    def __init__(self, *args):
        super(Server, self).__init__(*args)  
    
    def do_HEAD(self):
        return
    
    def do_POST(self):
        return
    
    def do_GET(self):
        self.respond()
    
    def handle_http(self, status, content_type):
        u = data_store.Instance()
        # print(u.x)
        # print(u.y)
        # print(self.path[:6])
        if self.path in routes:
            print(routes[self.path])
            route_content = routes[self.path]['template']
            filepath = "{}".format(route_content)
            try:
                content_type = "text/html"
                response_content = open("{}".format(route_content))
                response_content = response_content.read()
            except:
                content_type = "text/plain"
                response_content = "404 Not Found"
        else:
            try:
                if self.path.startswith('/pose/'):
                    u.x = self.path[6:9]
                    u.y = self.path[9:12]
                    response_content = "test"
                elif self.path.startswith('/mouse/'):
                    response_content = u.x+' '+u.y
            except:
                content_type = "text/plain"
                response_content = "404 Not Found"

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(response_content, "UTF-8")
    
    def respond(self):
        content = self.handle_http(200, 'text/html')
        self.wfile.write(content)