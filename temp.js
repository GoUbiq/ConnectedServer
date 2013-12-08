var io = require('socket.io-client');

var socket = io.connect('ws://192.168.0.100:8000');

/**

socket.of('/register').emit( 'register', { 'user': 'sumit', 'device' : 'laptop' } );

socket.of('/register').on('new_device', function (data) {
    console.log('HIII');
    console.log(data);
  });

socket.of('/register').emit('registered_devices', 'all') 

socket.of('/register').on('respond_registered_devices', function (data) {
    console.log(data);
 });


//socket.of('/register').emit('apocalypse', 'all') 

socket.of('/register').emit('remove_device', { 'user': 'sumit', 'device' : 'laptop' }) 

**/
socket.of('/connect').emit( 'connect', { 'user': 'sumit', 'device' : 'laptop' } );

socket.of('/connect').on('new_connection', function (data) {
    console.log(data);
 });

socket.of('/connect').emit( 'send_message', { 'user': 'sumit', 'destination' : 'send_all', 'message' : 'play it cock sucker'} );

socket.of('/connect').on('transfer', function (data) {
    console.log(data);
 });