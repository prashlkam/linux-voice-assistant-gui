import speech_recognition as sr
import pyaudio
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
		# self.engine.setProperty('voice',self.vices[2].id)
		
	
	def talk(self, text):
		self.engine.say(text)
		self.engine.runAndWait()
	
	
	def take_command(self):
		self.command = ''
		try:
			with sr.Microphone() as source:
				print('listening...')
				voice = self.listener.listen(source)
				self.command = self.listener.recognize_google(voice)
				self.command = self.command.lower()
				if 'liva' in self.command:
					self.command = self.command.replace('liva ', '')
					print(self.command)
		except Exception as e:
			print("Exception: " + str(e))
			# pass
		# self.outputtext.setText(command)
		return self.command
	
	def liva_run(self, cmd):
		self.command = cmd
		if self.command == '':
			self.command = self.take_command()
		self.resulttoshow = ''
		# print(command)
		if 'run' in self.command:
			self.command = self.command.replace('run ', '')
			# exec_cmd(cmdtorun)
		elif 'launch' in self.command:
			self.command = self.command.replace('launch ', '')
			# exec_cmd(cmdtorun)
		elif 'play' in self.command:
			self.command = self.command.replace('play ', '')
			self.talk('playing ' + self.command)
			pywhatkit.playonyt(self.command)
		elif 'who is' in self.command:
			self.command = self.command.replace('who is ', '')
			info = wikipedia.summary(self.command, 3)
			# print(info)
			# self.outputtext.setText(info)
			self.resulttoshow = info
			self.talk(info)
		elif 'what is' in self.command:
			self.command = self.command.replace('what is ', '')
			info = wikipedia.summary(self.command, 3)
			# print(info)
			# self.outputtext.setText(info)
			self.resulttoshow = info
			self.talk(info)
		elif 'where is' in self.command:
			self.command = self.command.replace('where is ', '')
			info = wikipedia.summary(self.command, 3)
			# print(info)
			# self.outputtext.setText(info)
			self.resulttoshow = info
			self.talk(info)
		elif 'how to' in self.command:
			self.command = self.command.replace('how to ', '')
			# QMessageBox.about(self, "Alert", 'searching how to ' + qstn)
			self.talk('searching how to ' + self.command)
			pywhatkit.search(self.command)
		elif 'get information' in self.command:
			self.command = self.command.replace('get information ', '')
			# QMessageBox.about(self, "Alert", 'Getting information: ' + qstn)
			self.talk('getting information ' + self.command)
			pywhatkit.search(self.command)
		elif 'search information' in self.command:
			self.command = self.command.replace('search information ', '')
			# QMessageBox.about(self, "Alert", 'Searching information: ' + qstn)
			self.talk('searching information ' + self.command)
			pywhatkit.search(self.command)
		elif 'get info' in self.command:
			self.command = self.command.replace('get info ', '')
			# QMessageBox.about(self, "Alert", 'Getting info: ' + qstn)
			self.talk('getting info ' + self.command)
			pywhatkit.info(self.command)
		elif 'search info' in self.command:
			self.command = self.command.replace('search info ', '')
			# QMessageBox.about(self, "Alert", 'Searching info: ' + qstn)
			self.talk('searching info ' + self.command)
			pywhatkit.info(self.command)
		elif 'time' in self.command:
			time = datetime.datetime.now().strftime('%I:%M %p')
			# QMessageBox.about(self, "Alert", 'Current time: ' + time)
			self.resulttoshow = 'Current time: ' + time
			self.talk('Current time is ' + time)
		elif 'date' in self.command:
			date = datetime.datetime.now().strftime('%d %B %Y')
			# QMessageBox.about(self, "Alert", 'Current date: ' + date)
			self.resulttoshow = 'Current date: ' + date
			self.talk('Current date is ' + date)
		elif 'joke' in self.command:
			joke = pyjokes.get-joke()
			# self.outputtext.setText(joke)
			self.resulttoshow = joke
			self.talk(joke)
		elif 'liva are you single' in self.command:
			self.resulttoshow = 'I am in a relationship with Tux...'
			self.talk('I am in a relationship with Tux...')
		else:
			# QMessageBox.about(self, "Alert", 'I didn\'t get you. Please say the command again...')
			self.resulttoshow = ''
			self.talk('I didn\'t get you. Please say the command again...')
		
		print('Command:\n--------\n' + self.command)
		if self.resulttoshow == '':
			self.resulttoshow = 'No Results to Show Here...'
		print('Result:\n--------\n' + self.resulttoshow)
		return self.command, self.resulttoshow
		

# main
lv = LivaVoice()
lv.liva_run('')
