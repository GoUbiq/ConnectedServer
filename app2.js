var io = require('socket.io-client');

var socket = io.connect('ws://localhost:8000');

socket.of('/app').on('video_data', function (data) {
    console.log("App: Video data " + data);
 });

socket.of('/app').on('new_connection', function (data) {
    console.log("App: New Connection " + data);
 });


socket.of('/app').emit( 'app_start', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video' }})




