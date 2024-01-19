from flask import Flask
from flask import send_file

class ResourceServer:
    def __init__(self, name) -> None:
        self.resource_server = Flask(name)
        self.setup_routes()

    def setup_routes(self):
        self.resource_server.route('/')(self.hello_world)

    def run(self, **kwargs):
        self.resource_server.run(**kwargs)

    def hello_world(self):
        return '<h4>Hello World!</h4>'
    


if __name__ == '__main__':
    my_server = ResourceServer(__name__)
    my_server.run(debug=True)
