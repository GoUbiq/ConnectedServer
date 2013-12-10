from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from pymongo import MongoClient
from namespaces import ConnectNamespace, DefaultNamespace, RegisterNamespace, AppNamespace

mongoClient = MongoClient()
connected_db = mongoClient['connected_db']

devices = connected_db.devices
connected = connected_db.connected

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

nsmap = {'/connect': ConnectNamespace, '' : DefaultNamespace, '/register' : RegisterNamespace, '/app' : AppNamespace}

def run():
    print 'Starting Server'
    server = SocketIOServer(('0.0.0.0', 8000), SessionClient(),
        resource="socket.io", policy_server=True,
        policy_listener=('0.0.0.0', 10843))
    server.serve_forever()


if __name__ == '__main__':
    print " Main Called"
    run()

