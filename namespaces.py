from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from pymongo import MongoClient
from ubiq_video import UbiqVideo

#mongoClient = MongoClient()
#connected_db = mongoClient['connected_db']

#devices = connected_db.devices
#connected = connected_db.connected

class DefaultNamespace(BaseNamespace, BroadcastMixin, RoomsMixin):

    '''
    def initialize(self):
        print 'DefaultNamespace: initialize'

    '''

    def on_connect(self, data):
        print 'DefaultNamespace: on_connect '
        print data
        if data == 'tv':
            print 'Connecting TV to session'
            post = {'user': 'sumit', 'device':'TV'};
            #connected.insert(post)
        elif data == 'laptop':
            print 'Connecting laptop to session'
            post = {'user': 'sumit', 'device':'TV'};
            #connected.insert(post)
        elif data == 'tab':
            print 'Connecting tab to session'
        elif data == 'phone':
            print 'Connecting phone'


    '''
    Transfer data from device A to device B
    '''
    def on_transfer(self, packet):
        print 'DefaultNamespace: on_transfer'
        print data 

        '''
        if data['destination'] does not exist in the database
        false destination

        else 
        transfer to destination
        return succesful message

        '''

    def recv_message(self, data):
        print 'DefaultNamespace: recv_message' + data

    def recv_error(self, packet):
        print 'error'


'''
Connect namespace
'''

class ConnectNamespace(BaseNamespace, BroadcastMixin, RoomsMixin):

    list_of_apps = []

    def recv_connect(self):
        print 'ConnectNamespace: recv_connect'

    def initialize(self):
        print 'ConnectNamespace: initialize'

    def on_connect(self, data):
                
        #CHECK IF DEVICE IS ON THE REGISTERED LIST

        print 'ConnectNamespace: on_connect' 
        print data

        user = data['user']

        if user == None:
            print 'Invalid user'
            user = 'sumit'

        device = data['device']

        if device == None:
            print 'Invalid device'
            return

        print 'Connecting ' + device
        post = {'user':  user, 'device': device}

        does_exist = connected.find(post)
        if does_exist == None:
            connected.insert(post)
        else:
            print 'Already exists'

        self.join(user)

        message = device + ' has joined'
        self.emit_to_room(user, 'new_connection', message)

        #Notify all devices in Namespace
        print 'Notifying all devices'

    def recv_disconnect(self):
        self.disconnect(silent=True)

    def on_disconnect(self, data):
        '''
        When a device decides to disconnect from the application
        '''
        
        print 'ConnectNamespace: on_disconnect' 
        print data

        user = data['user']

        if user == None:
            print 'Invalid user'
            user = 'sumit'

        device = data['device']

        if device == None:
            print 'Invalid device'
            return

        post = {'user': user, 'device': device}
        devices.remove(post)

    def on_connected_devices(self, data):
        '''
            Find all  connected devices for the user
        '''
        print 'ConnectNamespace: on_connected_devices '
        list_of_devices = []
        for device in connected.find():
            user = device['user']
            dev = device['device']
            user_info = { 'user' : user, 'device' : dev}
            list_of_devices.append(user_info)

        self.emit('respond_connected_devices', list_of_devices)


    def on_send_message(self, data):
        print 'ConnectNamespace: on_send_message'
        print data

        user = data['user']

        if user == None:
            print 'Invalid user'
            user = 'sumit'

        destination = data['destination']

        if destination == None:
            print 'Invalid destination'
            return
        elif destination == 'send_all':
            print 'Sending to all devices for the user'
        else:
            print 'I donno who the fuck you trying to send to'

        message = data['message']

        if message == None:
            print 'Invalid message'
            message = 'play this fucking shit'

        self.join(user)
        self.emit_to_room(user, 'transfer', message)

        #if app hasn't started start app
        #connect app to all 
        #Start an Application object and store it in user namespace

class AppNamespace(BaseNamespace, BroadcastMixin, RoomsMixin):
    """
        docstring for AppNamespace
    """
        
    def __app_info(data):
        app_name = data['app_name']
        app_id = data['app_id']


    def recv_connect(self):
        print 'AppNamespace: recv_connect'

    def initialize(self):
        print 'AppNamespace: initialize'
        self.list_of_apps = []
        self.ubiq_app = UbiqVideo()
        self.list_of_apps.append(self.ubiq_app)
        #list of accepted apps?

    def on_app_info(data):
        print 'AppNamespace: Application Info'

    def on_register_app(self, data):
        app_name = data['app_name']
        app_id = data['app_id']
        app_description = data['app_description']


    def on_connect_app(self, data):
        print 'AppNamespace: on_connect_app'


    def on_app_start(self, data):
        print 'AppNamespace: on_start_app'
        #check app credentials

        params = data['params']
        self.ubiq_app.start(params, self)

    def on_app_action(self, data):
        #print 'AppNamespace: on_update_app'
        #check app credentials
        #Get App id and figure out the app

        params = data['params']
        self.ubiq_app.action(params)

    def on_app_stop(self, data):
        print 'AppNamespace: on_stop_app'

        params = data['params']
        self.ubiq_app.stop(params)





class RegisterNamespace(BaseNamespace, BroadcastMixin):
    """docstring for  RegisterNamespace"""

    def recv_connect(self):
        print 'RegisterNamespace: recv_connect'

    def initialize(self):
        print 'RegisterNamespace: initialize'

    '''
    Register event for Registering device
    '''
    def on_register(self, data):

        # Add device to List of Devices
        print 'RegisterNamespace: on_register' 
        print data

        user = data['user']

        if user == None:
            print 'Invalid user'
            user = 'sumit'

        device = data['device']

        if device == None:
            print 'Invalid device'
            return

        print 'Registering' + device
        post = {'user':  user, 'device': device};
        devices.insert(post)

        #Notify all devices in Namespace
        print 'Notifying all devices'

        #WHY NOTIFY DEVICES?

        self.emit('new_device', device)


    def on_registered_devices(self, data):
        print 'RegisterNamespace: on_registered_devices'
        list_of_devices = []
        for device in devices.find():
            user = device['user']
            dev = device['device']
            user_info = { 'user' : user, 'device' : dev}
            list_of_devices.append(user_info)

        self.emit('respond_registered_devices', list_of_devices)

    def on_apocalypse(self, data):
        print 'RegisterNamespace: on_apocalypse'
        devices.drop()

    def on_remove_device(self, data):
        print 'RegisterNamespace: on_remove_device'
        user = data['user']

        if user == None:
            print 'Invalid user'
            user = 'sumit'

        device = data['device']

        if device == None:
            print 'Invalid device'
            return

        post = {'user': user, 'device': device};
        devices.remove(post)
