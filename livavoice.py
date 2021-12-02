import speech_recognition as sr
from gnewsclient import gnewsclient
import python_weather
import subprocess 
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
		self.load_params()
		self.listener = sr.Recognizer()
		self.engine = pyttsx3.init()
		self.voices = self.engine.getProperty('voices')
		self.engine.setProperty('voice',self.params['Pyttsx3_options']['language'] + '+f3')
		self.chunk = int(self.params['Pyaudio_options']['chunk'])
		if 'paInt16' in self.params['Pyaudio_options']['sample_format']:
			self.sample_format = pyaudio.paInt16 
		self.channels = int(self.params['Pyaudio_options']['channels'])
		self.fs = int(self.params['Pyaudio_options']['fs'])
		self.seconds = int(self.params['Pyaudio_options']['seconds'])
		self.audiofilename = os.path.expanduser(self.params['Pyaudio_options']['audio_file'])
		self.pyaud = pyaudio.PyAudio()
		
	def load_params(self):
		with open(os.path.expanduser('~/.config/liva/liva-config.json'), 'r') as jsf:
			self.params = json.load(jsf)
	
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
		wf = wave.open(self.audiofilename, 'wb')
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
			self.recaudio(self.audiofilename)
			# with sr.Microphone(device_index=4) as source:
			with sr.AudioFile(self.audiofilename) as source:
				# print('listening...')
				voice = self.listener.listen(source)
				self.command = self.listener.recognize_google(voice)
				self.command = self.command.lower()
		except Exception as e:
			print("Exception: " + str(e))
		return self.command
	
	def exec_cmd(self, command):
		# executes final part of utterance
		os.popen(command)
		self.talk('Executing ' + command)
	
	def exec_cmd_term(self, command):
		# executes final part of utterance
		term = self.params['Liva_options']['terminal_emulator']
		os.popen(term + ' -hold -e ' + command)
		self.talk('Executing in terminal ' + command)
		
	# def weather_func(self, params):
	async def weather_func(self):
		# declare the client. format defaults to metric system (celcius, km/h, etc.)
		client = python_weather.Client(format=python_weather.IMPERIAL)
		# fetch a weather forecast from a city
		city = self.params['Weather_options']['location']
		weather = await client.find(city)
		# returns the current day's forecast temperature (int)
		# print(weather.current.temperature)
		# get the weather forecast for a few days
		s = '' 
		s = 'Location: ' + weather.location_name + '\n'
		s += 'Date/Time: ' + str(weather.current.date) + '\n'
		if 'Celcius' in self.params['Weather_options']['temprature_unit']:
			s += 'Temprature: ' + str(round((weather.current.temperature - 32) * 5 / 9, 2)) + ' °C\n'
		else:
			s += 'Temprature: ' + str(weather.current.temperature) + ' °F\n'
		s += 'Humidity: ' + str(weather.current.humidity) + ' %\n'
		if 'KMPH' in self.params['Weather_options']['windspeed_unit']:
			s += 'Wind Speed: ' + str(round(weather.current.wind_speed * 0.621, 2)) + " KMPH\n"
		else:
			s += 'Wind Speed: ' + str(weather.current.wind_speed) + " MPH\n"
		s += 'Forecast: ' + weather.current.sky_text + '\n'        
		# close the wrapper once done
		await client.close()
		return s
		
	# def news_func(self, params):
	def news_func(self):
		# load params
		newsopts = self.params['News_options']
		# declare a NewsClient object
		client = gnewsclient.NewsClient(language=newsopts['language'], location=newsopts['location'], topic=newsopts['topic'], max_results=int(newsopts['max_count']))
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
			self.command = self.command.replace('run in terminal ', ' ')
			self.exec_cmd_term(self.command)
		if 'run' in self.command:
			self.command = self.command.replace('run ', '')
			self.exec_cmd(self.command)
		elif 'launch in terminal' in self.command:
			self.command = self.command.replace('launch in terminal ', ' ')
			self.exec_cmd_term(self.command)
		elif 'launch' in self.command:
			self.command = self.command.replace('launch ', '')
			self.exec_cmd(self.command)
		elif 'open in terminal' in self.command:
			self.command = self.command.replace('open in terminal ', ' ')
			self.exec_cmd_term(self.command)
		elif 'open' in self.command:
			self.command = self.command.replace('open ', '')
			self.exec_cmd(self.command)
		elif 'start in terminal' in self.command:
			self.command = self.command.replace('start in terminal ', ' ')
			self.exec_cmd_term(self.command)
		elif 'start' in self.command:
			self.command = self.command.replace('start ', '')
			self.exec_cmd(self.command)
		elif 'man page ' in self.command:
			self.command = self.command.replace('man page ', ' man ')
			self.exec_cmd_term(self.command)
		elif 'info page' in self.command:
			self.command = self.command.replace('info page ', ' info ')
			self.exec_cmd_term(self.command)
		elif 'play' in self.command:
			self.command = self.command.replace('play ', '')
			pywhatkit.playonyt(self.command)
			self.talk('playing ' + self.command)
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
		# return values
		print('Command:\n--------\n' + self.command)
		if self.resulttoshow == '':
			self.resulttoshow = 'No Results to Show Here...'
		print('Result:\n--------\n' + self.resulttoshow)
		return self.command, self.resulttoshow
		

# main
# lv = LivaVoice()
# lv.liva_run('')
