var io = require('socket.io-client');

var socket = io.connect('ws://192.168.0.102:8000');

/**

socket.of('/register').emit( 'register', { 'user': 'sumit', 'device' : 'laptop' } );

socket.of('/register').on('new_device', function (data) {
    console.log(data);
  });

socket.of('/register').emit('registered_devices', 'all') 

socket.of('/register').on('respond_registered_devices', function (data) {
    console.log(data);
 });


socket.of('/register').emit('apocalypse', 'all') 

socket.of('/register').emit('remove_device', { 'user': 'sumit', 'device' : 'laptop' }) 


socket.of('/connect').emit( 'connect', { 'user': 'sumit', 'device' : 'laptop' } );

socket.of('/connect').on('new_connection', function (data) {
    console.log("Connect: New connection" + data);
 });



socket.of('/connect').emit( 'send_message', { 'user': 'sumit', 'destination' : 'send_all', 'message' : 'play it cock sucker'} );

socket.of('/connect').on('transfer', function (data) {
    console.log(data);
 });

socket.of('/connect').emit('connected_devices', 'all') 

socket.of('/connect').on('respond_connected_devices', function (data) {
    console.log(data);
 });
 
 */

socket.of('/app').on('new_connection', function (data) {
    console.log("App: New connection " + data);
 });


socket.of('/app').emit( 'app_start', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video' }});

socket.of('/app').emit( 'app_action', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video', 'request' : 'pause' }});

socket.of('/app').emit( 'app_action', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video', 'request' : 'play' }});

socket.of('/app').emit( 'app_action', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video', 'request' : 'play_url', 'url' : 'http://www.youtube.com/watch?v=J-gYJBsln-w' }});

socket.of('/app').emit ( 'app_stop', {'params' : { 'app_id' : '12345', 'app_name' : 'Ubiq Video' }});