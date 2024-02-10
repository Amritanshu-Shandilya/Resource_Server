from flask import Flask
from flask import send_file

from database_helper import DB_Helper

class ResourceServer:
    def __init__(self, name) -> None:
        self.resource_server = Flask(name)
        self.setup_routes()

    def setup_routes(self):
        pass

    def request_processor(self):
        pass
    
    def request_listener(self):
        pass


    


if __name__ == '__main__':
    my_server = ResourceServer(__name__)
    my_server.run(debug=True)
