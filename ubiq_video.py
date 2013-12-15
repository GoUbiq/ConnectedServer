import time
import os


class UbiqVideo():

	def __init__(self):
		print 'UbiqVideo: __init__'
		self.current_time = "00:00" 
		self.current_video = "http://ubiq.com/cant_play"
		self.room = None
		self.current_video = 'None'
		self.playing = False

		#When Application is initilized, it needs user info

	def action(self, params):
		#print 'UbiqVideo: on_request'

		request = params['request']
		if request == None:
			print 'Illegal request'
		#else:
			#print 'Request for action: ' + request

		if request == 'play_url':
			self.__play_url(params)

		elif request == 'play':
			self.__play(params)
		elif request == 'pause':
			self.__pause(params)
		elif request == 'video_time':
			self.__time(params)
		else:
			print 'Unknown request'


	def __time(self, data):
		#print 'UbiqVideo: __time'
		#print data

		self.current_time = data['time']
		self.devices.emit_to_room('sumit' , 'video_data', self.current_time)

		print self.current_time


	def __play_url(self, data):
		print 'UbiqVideo: __play_url'
		print data

		play_url = data['url']

		message = play_url + " is playing"
		self.devices.emit_to_room('sumit' , 'video_data', message)
		"""
		
		play_target = data ['target']

		if target == 'all'
			self.devices.play_all(play_url)
		elif 
			self.devices.play(play_target, play_url)
		cmd = 'osascript ~/Services/weblink/openweblink.scpt openlink \"' + play_url + '\"'
		os.system(cmd)
		self.playing = True

		"""

		#Let all the other rooms knows. Status of image.


	def start(self, request, devices):
		#Initialize app variables
		print 'UbiqVideo: start request received'
		print request
		self.devices = devices 

		#Initialize 

		message = 'New device has joined'
		self.devices.join('sumit')
		self.devices.emit_to_room('sumit' , 'new_connection', message)

	def stop(self, request):
		#Initialize app variables
		print 'UbiqVideo: stop request received'
		print request

	def __play(self, request):
		print 'UbiqVideo: play'


	def __pause(self, request):
		print 'UbiqVideo: pause'

	def get_current_info():
		print 'UbiqVideo: get_current_info'

