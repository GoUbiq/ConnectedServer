from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin

mongoClient = MongoClient()
connected_db = mongoClient['connected_db']

devices = connected_db.devices
connected = connected_db.connected

class DefaultNamespace(BaseNamespace, BroadcastMixin):

    '''
   def initialize(self):
        print 'DefaultNamespace: initialize'

    '''

    def on_connect(self, data):
        print 'DefaultNamespace: on_connect'

    def on_register(self, packet):
        print 'DefaultNamespace: on_register'

    def on_transfer(self, packet):
        print 'DefaultNamespace: on_transfer'


    def recv_message(self, data):
        print 'DefaultNamespace: recv_message'

    def recv_error(self, packet):
        print 'error'

    def  



class ConnectNamespace(BaseNamespace, BroadcastMixin):
    def recv_connect(self):
        print 'ConnectNamespace: recv_connect'

    def initialize(self):
        print 'ConnectNamespace: initialize'

    def on_connect():
        print 'ConnectNamespace: on_connect'

    def on_vent(self, packet):
        print 'on_vent'

class SessionClient(object):

    def  __init__(self):
        self.buffer = []
    
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].strip('/') or 'index.html'
        print path
        
        if path.startswith("socket.io"):
            socketio_manage(environ, nsmap)
        else:
            return not_found(start_response)


def not_found(start_response):
    start_response('404 Not Found', [])
    return ['<h1>Not Found</h1>']

nsmap = {'/connect': ConnectNamespace, '' : DefaultNamespace}

def run():
    print 'Starting Server'
    server = SocketIOServer(('127.0.0.1', 8000), SessionClient(),
        resource="socket.io", policy_server=True,
        policy_listener=('0.0.0.0', 10843))
    server.serve_forever()


if __name__ == '__main__':
    print " Main Called"
    run()

