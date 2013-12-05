var io = require('socket.io-client');

var socket = io.in('connect').connect('http://localhost:8000');

socket.emit('vent', 'buzz');




