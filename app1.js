var io = require('socket.io-client');

var socket = io.connect('ws://localhost:8000');

socket.of('/app').emit( 'app_start', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video' }});

var time = 0;
setInterval(function() { 
	time = time + 1
	console.log(time);
	socket.of('/app').emit( 'app_action', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video', 'request' : 'video_time', 'time' : time.toString() }});
}, 1000);



