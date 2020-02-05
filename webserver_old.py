# import http.server
# import socketserver
# import logging
# from requests import Response
# import tempfile
# from http.server import ThreadingHTTPServer

# PORT = 8000

# class posenet_handler(http.server.SimpleHTTPRequestHandler):
    
#     def do_GET(self):
#         #print(self.path)
#         if self.path.startswith('/pose'):
#             print(self.path)
#             f= open("poses.txt","w+")
#             f.write(self.path[6:])
#             f.close()
#         elif self.path.startswith('/mouse'):
#             self.send_response(200)
#             self.wfile.write(b"test")
#         else:
#             return http.server.SimpleHTTPRequestHandler.do_GET(self)

from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class Handler(BaseHTTPRequestHandler):

   def do_GET(self):
        if self.path.startswith('/pose'):
            print(self.path)
            f= open("poses.txt","w+")
            f.write(self.path[6:])
            f.close()
            return
        elif self.path.startswith('/mouse'):
            self.send_response(200)
            self.wfile.write(b"test")
            return
        else:
            return self.handle()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

