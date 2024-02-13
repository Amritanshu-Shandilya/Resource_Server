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
        self.resource_server.route('/get_data/<user_id>/<unique_id>/<time_stamp>')(self.request_listener)
        self.resource_server.route('/get_name/<unique_id>')(self.get_name)

    def run(self, **kwargs):
        self.resource_server.run(**kwargs)

    def home_screen(self):
        '''This functions is used to render a homescreen on the server.'''
        return render_template('home_page.html')
    
    def block_user(Self):
        '''This function is used to render an access denied screen on the server'''
        return render_template('access_denied.html')
    
    def request_processor(self):
        '''This function takes the record data and uses it to get the contents of the file data and send it as a response to the client'''
        id, name, lv1, lv2, lv3 = self.extracted_data
        # creating the path
        path = 'E:/'+lv1+'/'+lv2+'/'+lv3+'/'+name+'.txt'

        with open(path, 'r') as file:
            file_content = file.read()
        
        return file_content
    
    def authenticate(slef, user_id):
        '''This function ensures that the user accessing the id is a registered user and returns True if it is.'''
        pass

    def request_listener(self, user_id, unique_id, time_stamp):
        '''This function listens the requests and processes it to get the record of the accessed file and sends it to be processed. 
            It also adds request to history and authenticates the client'''
        self.extracted_data = self.db_helper.fetch_record(unique_id=unique_id)[0]

        if self.db_helper.add_to_history(user_id, unique_id, time_stamp):
            return self.request_processor()
    

    def get_name(self, unique_id):
        '''This fucntion fetches the name of the file using the unique id'''
        name = self.db_helper.fetch_name(unique_id=unique_id)
        return name

        


if __name__ == '__main__':
    my_server = ResourceServer(__name__)
    my_server.run(host='0.0.0.0' ,debug=True)
