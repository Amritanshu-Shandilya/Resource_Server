from flask import Flask
from flask import render_template
from flask import request

from database_helper import DB_Helper

class ResourceServer:
    def __init__(self, name) -> None:

        self.db_helper = DB_Helper()

        self.extracted_data = None

        self.resource_server = Flask(name)
        self.setup_routes()

    def setup_routes(self):
        self.resource_server.route('/')(self.home_screen)
        self.resource_server.route('/get_data/<unique_id>')(self.request_listener)

    def run(self, **kwargs):
        self.resource_server.run(**kwargs)

    def home_screen(self):
        return render_template('home_page.html')
    
    def request_processor(self):
        id, name, lv1, lv2, lv3 = self.extracted_data
        # creating the path
        path = '/'+lv1+'/'+lv2+'/'+lv3+'/'+name+'.txt'

        with open(path, 'r') as file:
            file_content = file.read()
        
        return file_content

    def request_listener(self, unique_id):
        self.extracted_data = self.db_helper.fetch_record(unique_id=unique_id)[0]
        
        self.request_processor()

        


if __name__ == '__main__':
    my_server = ResourceServer(__name__)
    my_server.run(host='0.0.0.0' ,debug=True)
