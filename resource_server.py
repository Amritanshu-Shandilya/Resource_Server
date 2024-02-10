from flask import Flask
from flask import render_template
from flask import request

from database_helper import DB_Helper

class ResourceServer:
    def __init__(self, name) -> None:
        self.resource_server = Flask(name)
        self.setup_routes()

    def setup_routes(self):
        self.resource_server.route('/')(self.home_screen)

    def run(self, **kwargs):
        self.resource_server.run(**kwargs)

    def home_screen(self):
        return render_template('home_page.html')
    
    def request_processor(self):
        pass

    def request_listener(self):
        pass
    


if __name__ == '__main__':
    my_server = ResourceServer(__name__)
    my_server.run(debug=True)
