var io = require('socket.io-client');

var socket = io.connect('http://54.201.0.33:8000');

socket.emit('connect', 'buzz');




