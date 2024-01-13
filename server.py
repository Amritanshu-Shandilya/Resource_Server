from http.server import SimpleHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
port = 9999

class ResourceServer (SimpleHTTPRequestHandler):
    
    def do_GET(self) -> None:
        print('path: ' + self.path)
        return super().do_GET()



if __name__ == '__main__':
    
    server = HTTPServer((hostName, port), ResourceServer)
    print ("Server strated at http://%s:%s"%(hostName, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server_closed')