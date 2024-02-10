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
        self.resource_server.route('/get_data')(self.request_listener)

    def run(self, **kwargs):
        self.resource_server.run(**kwargs)

    def home_screen(self):
        return render_template('home_page.html')
    
    def request_processor(self, path):
        pass

    def request_listener(self, unique_id):
        data = DB_Helper.fetch_record(unique_id)
        print(data)
        return '<p>Displaying the data</p>'

        


if __name__ == '__main__':
    my_server = ResourceServer(__name__)
    my_server.run(host='0.0.0.0' ,debug=True)
