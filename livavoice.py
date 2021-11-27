import speech_recognition as sr
from gnewsclient import gnewsclient
import python_weather
import asyncio
import requests
import json
import pyaudio
import wave
import pyttsx3
import pywhatkit
import datetime
import time
import wikipedia
import pyjokes
import os
import sys


class LivaVoice():
	def __init__(self):
		self.listener = sr.Recognizer()
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('voice','english+f3')
		self.chunk = 1024  # Record in chunks of 1024 samples
		self.sample_format = pyaudio.paInt16  # 16 bits per sample
		self.channels = 2
		self.fs = 44100  # Record at 44100 samples per second
		self.seconds = 13
		self.filename = "output.wav"
		self.pyaud = pyaudio.PyAudio()  # Create an interface to PortAudio
		
	def recaudio(self, filename):
		print('Recording...')
		stream = self.pyaud.open(format=self.sample_format,
						channels=self.channels,
						rate=self.fs,
						frames_per_buffer=self.chunk,
						input=True)
		frames = []  # Initialize array to store frames
		# Store data in chunks for 3 seconds
		for i in range(0, int(self.fs / self.chunk * self.seconds)):
			data = stream.read(self.chunk)
			frames.append(data)
		# Stop and close the stream 
		stream.stop_stream()
		stream.close()
		# Terminate the PortAudio interface
		self.pyaud.terminate()
		print('Finished recording...')
		# Save the recorded data as a WAV file
		wf = wave.open(self.filename, 'wb')
		wf.setnchannels(self.channels)
		wf.setsampwidth(self.pyaud.get_sample_size(self.sample_format))
		wf.setframerate(self.fs)
		wf.writeframes(b''.join(frames))
		wf.close()
	
	def talk(self, text):
		self.engine.say(text)
		self.engine.runAndWait()
	
	
	def take_command(self):
		self.command = ''
		try:
			self.recaudio(self.filename)
			# with sr.Microphone(device_index=4) as source:
			with sr.AudioFile(self.filename) as source:
				# print('listening...')
				voice = self.listener.listen(source)
				self.command = self.listener.recognize_google(voice)
				self.command = self.command.lower()
		except Exception as e:
			print("Exception: " + str(e))
			# pass
		# self.outputtext.setText(command)
		return self.command
	
	def exec_cmd(self, command):
		# executes final part of utterance
		os.popen(command)
		self.talk('Executing ' + command)
	
	def exec_cmd_term(self, command):
		# executes final part of utterance
		os.popen('xterm -e ' + command)
		self.talk('Executing in terminal ' + command)
	
	def man_page(self, command):
		# executes final part of utterance
		os.popen('xterm -e man ' + command)
		self.talk('Showing man page for ' + command)
	
	# def weather_func(self, params):
	async def weather_func(self):
		# declare the client. format defaults to metric system (celcius, km/h, etc.)
		client = python_weather.Client(format=python_weather.IMPERIAL)
		# fetch a weather forecast from a city
		city = "Bengaluru"
		weather = await client.find(city)
		# returns the current day's forecast temperature (int)
		# print(weather.current.temperature)
		# get the weather forecast for a few days
		s = '' 
		s = 'Location: ' + city + '\n'
		s += 'Date/Time: ' + str(weather.current.date) + '\n'
		s += 'Temprature: ' + str(round((weather.current.temperature - 32) * 5 / 9, 2)) + '°C\n'
		s += 'Humidity: ' + str(weather.current.humidity) + '%\n'
		s += 'Wind Speed: ' + str(round(weather.current.wind_speed * 0.621, 2)) + "KMPH\n"
		s += 'Forecast: ' + weather.current.sky_text + '\n'        
		# close the wrapper once done
		await client.close()
		return s
		
	def load_params(self):
		pass
	
	# def news_func(self, params):
	def news_func(self):
		# load params
		# if params == []:
			# params = load_params()
		# declare a NewsClient object
		client = gnewsclient.NewsClient(language='english', location='india', topic='National', max_results=8)
		# get news feed
		n = client.get_news()
		titles = []
		for i in n:
			titles.append(i['title'] + '\n')
		s = ''
		for i in titles:
			s += i
		return s
	
	def liva_run(self, cmd):
		self.command = cmd
		if self.command == '':
			self.command = self.take_command()
		self.resulttoshow = ''
		if 'liva' in self.command:
			self.command = self.command.replace('liva ', '')
		print('Command: ',self.command)
		if 'run in terminal' in self.command:
			self.command = self.command.replace('run in terminal ', '')
			self.exec_cmd_term(self.command)
		if 'run' in self.command:
			self.command = self.command.replace('run ', '')
			self.exec_cmd(self.command)
		elif 'launch in terminal' in self.command:
			self.command = self.command.replace('launch in terminal ', '')
			self.exec_cmd_term(self.command)
		elif 'launch' in self.command:
			self.command = self.command.replace('launch ', '')
			self.exec_cmd(self.command)
		elif 'man page' in self.command:
			self.command = self.command.replace('man page ', '')
			self.man_page(self.command)
		elif 'play' in self.command:
			self.command = self.command.replace('play ', '')
			self.talk('playing ' + self.command)
			pywhatkit.playonyt(self.command)
		elif 'who is' in self.command:
			self.command = self.command.replace('who is ', '')
			info = wikipedia.summary(self.command, 3)
			self.resulttoshow = info
			self.talk(info)
		elif 'what is' in self.command:
			self.command = self.command.replace('what is ', '')
			info = wikipedia.summary(self.command, 3)
			self.resulttoshow = info
			self.talk(info)
		elif 'where is' in self.command:
			self.command = self.command.replace('where is ', '')
			info = wikipedia.summary(self.command, 3)
			self.resulttoshow = info
			self.talk(info)
		elif 'how to' in self.command:
			self.command = self.command.replace('how to ', '')
			pywhatkit.search(self.command)
			self.talk('searching how to ' + self.command)
		elif 'get information' in self.command:
			self.command = self.command.replace('get information ', '')
			pywhatkit.search(self.command)
			self.talk('getting information ' + self.command)
		elif 'search information' in self.command:
			self.command = self.command.replace('search information ', '')
			pywhatkit.search(self.command)
			self.talk('searching information ' + self.command)
		elif 'get info' in self.command:
			self.command = self.command.replace('get info ', '')
			pywhatkit.info(self.command)
			self.talk('getting info ' + self.command)
		elif 'search info' in self.command:
			self.command = self.command.replace('search info ', '')
			pywhatkit.info(self.command)
			self.talk('searching info ' + self.command)
		elif 'time' in self.command:
			time = datetime.datetime.now().strftime('%I:%M %p')
			self.resulttoshow = 'Current time: ' + time
			self.talk('Current time is ' + time)
		elif 'date' in self.command:
			date = datetime.datetime.now().strftime('%d %B %Y')
			self.resulttoshow = 'Current date: ' + date
			self.talk('Current date is ' + date)
		elif 'weather' in self.command:
			loop = asyncio.get_event_loop()
			self.weather = loop.run_until_complete(self.weather_func())
			self.resulttoshow = self.weather
			self.talk(self.weather)
		elif 'news' in self.command:
			self.news = self.news_func()
			self.resulttoshow = self.news
			self.talk(self.news)
		elif 'joke' in self.command:
			joke = pyjokes.get_joke(language="en", category="all")
			self.resulttoshow = joke
			self.talk(joke)
		elif 'liva are you single' in self.command:
			self.resulttoshow = 'I am in a relationship with Tux...'
			self.talk('I am in a relationship with Tux...')
		else:
			self.resulttoshow = ''
			self.talk('I didn\'t get you. Please say the command again...')
		print('Command:\n--------\n' + self.command)
		if self.resulttoshow == '':
			self.resulttoshow = 'No Results to Show Here...'
		print('Result:\n--------\n' + self.resulttoshow)
		return self.command, self.resulttoshow
		

# main
# lv = LivaVoice()
# lv.liva_run('')
