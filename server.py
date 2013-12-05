import sys
from pymongo import MongoClient
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

mongoClient = MongoClient()
connected_db = mongoClient['connected_db']

devices = connected_db.devices
connected = connected_db.connected


class ConnectedServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(request):
        print 'Got Request' + request.path
        if request.path  == "/connectPhone":
           request.send_response(200)
           request.send_header("Content-type", "text/html")
           request.end_headers()
           request.wfile.write("<html><head><title>You requested to connectPhone.</title></head>")
           request.wfile.write("<p>You accessed path: %s</p>" % request.path)
           request.wfile.write("</body></html>")

        elif request.path == "/connectTV":
            i = 0
            while i < 1000:
                print request.date_time_string()
            print "connectTV"
            post = {'user': 'sumit', 'device':'TV', 'request': 'connectTV'};
            connected.insert(post)

        elif request.path == "/connectLaptop":
            print "connectLaptop"
            post = {'user': 'sumit', 'device':'Laptop', 'request': 'connectLaptop'};
            connected.insert(post)

        elif request.path == "/connectPhone":
            print "connectLaptop"
            post = {'user': 'sumit', 'device':'Phone', 'request': 'connectPhone'};
            connected.insert(post)

        elif request.path == "/connectTablet":
            print "connectLaptop"
            post = {'user': 'sumit', 'device':'Tablet', 'request': 'connectTablet'};
            connected.insert(post)


        elif request.path == "/registerTV":
            print "registerTV"
            post = {'user': 'sumit', 'device':'TV', 'request': 'registerTV'};

        elif request.path == "/getConnectedDevices":
            print "connectedDevices"
            query = {'user': 'sumit'}
            connected_devices = connected.find(query)
            for d in connected_devices:
                print d['device']

        elif request.path == "/getDevices":
            print "getDevices"

        elif request.path == "/disconnectTV":
            connected.remove({'device' : 'TV'})

        elif request.path == "/disconnectLaptop":
            connected.remove({'device' : 'Laptop'})

        elif request.path == "/disconnectTab":
            connected.remove({'device' : 'Tab'})

        elif request.path == "/disconnectPhone":
            connected.remove({'device' : 'Phone'})

        else:
            print "Unknown Path"

    def do_POST(request):
        print request.path


def run():
    print "Run called"
    HandlerClass = ConnectedServerHandler
    ServerClass  = BaseHTTPServer.HTTPServer
    Protocol     = "HTTP/1.0"

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('127.0.0.1', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()

if __name__ == '__main__':
    print " Main Called"
    run()
