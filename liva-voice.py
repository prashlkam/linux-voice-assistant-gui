import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import wikipedia
import pyjokes
import os
import sys

class LivaVoice():
	def __init__():
		listener = sr.Recognizer()
		engine = pyttsx3.init()
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[1].id)
		
	def talk(text):
		engine.say(text)
		engine.runAndWait()
	
	
	def take_command(self):
		try:
			with sr.Microphone() as source:
				# print('listening...')
				voice = listener.listen(source)
				command = listener.recognize_google(voice)
				command = command.lower()
				if 'liva' in command:
					command = command.replace('liva', '')
					# print(command)
		except:
			pass
		self.outputtext.setText(command)
		return command
	
	def liva_run(self):
		command = take_command()
		# print(command)
		if 'run' in command:
			cmdtorun = command.replace('run', '')
			exec_cmd(cmdtorun)
		elif 'launch' in command:
			cmdtorun = command.replace('launch', '')
			exec_cmd(cmdtorun)
		elif 'play' in command:
			song = command.replace('play ', '')
			talk('playing ' + song)
			pywhatkit.playonyt(song)
		elif 'who is' in command:
			person = command.replace('who is', '')
			info = wikipedia.summary(person, 3)
			# print(info)
			self.outputtext.setText(info)
			talk(info)
		elif 'what is' in command:
			thing = command.replace('what is', '')
			info = wikipedia.summary(thing, 3)
			# print(info)
			self.outputtext.setText(info)
			talk(info)
		elif 'where is' in command:
			place = command.replace('where is', '')
			info = wikipedia.summary(place, 3)
			# print(info)
			self.outputtext.setText(info)
			talk(info)
		elif 'how to' in command:
			qstn = command.replace('how to', '')
			QMessageBox.about(self, "Alert", 'searching how to ' + qstn)
			talk('searching how to ' + qstn)
			pywhatkit.search(qstn)
		elif 'get information' in command:
			qstn = command.replace('get information', '')
			QMessageBox.about(self, "Alert", 'Getting information: ' + qstn)
			talk('getting information ' + qstn)
			pywhatkit.search(qstn)
		elif 'search information' in command:
			qstn = command.replace('search information', '')
			QMessageBox.about(self, "Alert", 'Searching information: ' + qstn)
			talk('searching information ' + qstn)
			pywhatkit.search(qstn)
		elif 'get info' in command:
			qstn = command.replace('get info', '')
			QMessageBox.about(self, "Alert", 'Getting info: ' + qstn)
			talk('getting info ' + qstn)
			pywhatkit.info(qstn)
		elif 'search info' in command:
			qstn = command.replace('search info', '')
			QMessageBox.about(self, "Alert", 'Searching info: ' + qstn)
			talk('searching info ' + qstn)
			pywhatkit.info(qstn)
		elif 'time' in command:
			time = datetime.datetime.now().strftime('%I:%M %p')
			QMessageBox.about(self, "Alert", 'Current time: ' + time)
			talk('Current time is ' + time)
		elif 'date' in command:
			date = datetime.datetime.now().strftime('%d %B %Y')
			QMessageBox.about(self, "Alert", 'Current date: ' + date)
			talk('Current date is ' + date)
		elif 'liva are you single' in command:
			talk('I am in a relationship with Tux...')
		elif 'joke' in command:
			joke = pyjokes.get-joke()
			self.outputtext.setText(joke)
			talk(joke)
		else:
			QMessageBox.about(self, "Alert", 'I didn\'t get you. Please say the command again...')
			talk('I didn\'t get you. Please say the command again...')
