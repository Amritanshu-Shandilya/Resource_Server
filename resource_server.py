from flask import Flask
from flask import render_template
from flask import request,redirect, url_for

import hashlib


from database_helper import DB_Helper, Admin

class ResourceServer:
    def __init__(self, name) -> None:

        self.db_helper = DB_Helper()
        self.admin = Admin()

        self.extracted_data = None

        self.resource_server = Flask(name)
        self.setup_routes()

    def setup_routes(self):
        self.resource_server.route('/')(self.home_screen)
        self.resource_server.route('/get_data/<user_id>/<unique_id>/<time_stamp>')(self.request_listener)
        self.resource_server.route('/get_name/<unique_id>')(self.get_name)
        self.resource_server.route('/login', methods = ['GET','POST'])(self.login_module)
        self.resource_server.route('/admin')(self.admin_dashboard)
        
        

    def run(self, **kwargs):
        self.resource_server.run(**kwargs)

    def home_screen(self):
        '''This functions is used to render a homescreen on the server.'''
        return render_template('home_page.html')
    
    def block_user(Self):
        '''This function is used to render an access denied screen on the server'''
        return render_template('access_denied.html')
    
    def login_screen(self):
        '''This function is used to render a login page that will be used to log in to as the admin or manager or staff roles.'''
        return render_template('login.html')
    

    def admin_dashboard(self):
        
        name = self.admin.getname()

        return render_template('admin_dashboard.html', admin_name = name[0])


    def login_module(self):
        '''This function is used to do the verification model'''
        if request.method == 'POST':
            user_name = request.form.get('username')
            pwd = request.form.get('password')

            password = hashlib.sha256(pwd.encode()).hexdigest()

            if self.admin.login_verification(uname= user_name, pwd= password):
                return redirect(url_for('admin_dashboard'))

            else:
                return render_template('access_denied.html')
        # If the request method is not 'POST', return a default response
        return render_template("login.html")


    def get_name(self, unique_id):
        file_name = self.db_helper.fetch_name(unique_id)
        return file_name
    
    def request_processor(self):
        '''This function takes the record data and uses it to get the contents of the file data and send it as a response to the client'''
        id, name, lv1, lv2, lv3 = self.extracted_data
        # creating the path
        path = 'D:/'+lv1+'/'+lv2+'/'+lv3+'/'+name+'.txt'

        with open(path, 'r') as file:
            file_content = file.read()
        
        return file_content
    

    def authenticator(self, user_id):
        if self.db_helper.authenticate_user(user_id):
            return self.request_processor()
        
    def add_history(self, user_id, unique_id, timestamp):
        if self.db_helper.add_to_history(user_id, unique_id, timestamp):
            return True

    def request_listener(self, user_id, unique_id, time_stamp):
        '''This function listens the requests and processes it to get the record of the accessed file and sends it to be processed. 
            It also adds request to history and authenticates the client'''
        # Adds the request to the history 

        if self.add_history(user_id, unique_id, time_stamp):
            self.extracted_data = self.db_helper.fetch_record(unique_id=unique_id)[0]
            # Sends the control to the authenticator
            return self.authenticator(unique_id)

        


if __name__ == '__main__':
    my_server = ResourceServer(__name__)
    my_server.run(host='0.0.0.0' ,debug=True)
