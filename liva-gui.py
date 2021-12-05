#!/usr/bin/env python3

import sys
import os
import livavoice as liva
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox, QLabel
from PyQt5.Qt import QClipboard

class ProgressPopup(QDialog):
	"""Loading screen animation."""
	def __init__(self):
		super(ProgressPopup, self).__init__()
		gif_path = './res/img/progress.gif'
		self.dlg = QDialog()
		self.dlg.setWindowTitle("Recording...")
		self.dlg.setWindowModality(False)
		self.dlg.setFixedSize(260, 260)
		self.dlg.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
		self.label_animation = QLabel(self.dlg)
		self.movie = QMovie(gif_path)
		self.label_animation.setMovie(self.movie)
	
	def start_animation(self):
		self.movie.start()
		self.dlg.show()
	
	def stop_animation(self):
		self.movie.stop()
		self.dlg.done(0)

class LinuxVoiceAssistant(QDialog):
	def __init__(self):
		super(LinuxVoiceAssistant, self).__init__()
		uic.loadUi("./res/maindlg.ui",self) 
		self.copy.clicked.connect(self.copy_clpboard)
		self.mic.clicked.connect(self.take_command)
		self.ask.clicked.connect(self.liva_run)
		self.help.clicked.connect(self.help_func)
		self.settings.clicked.connect(self.settings_func)
		self.quit.clicked.connect(self.quit_app)
		self.show()
		self.liva_object = liva.LivaVoice()
		
	
	
	def copy_clpboard(self):
		self.outputtext.selectAll()
		self.outputtext.copy()
	
	def help_func(self):
		# replace ls with man page for liva - TBD
		os.popen("xterm -e man ls")
	
	def settings_func(self):
		QMessageBox.about(self, "Alert", "Not yet implemented...")
	
	def quit_app(self):
		self.close()
	
	def exec_cmd(self):
		# executes final part of utterance
		cmdtorun = self.outputtext.toPlainText()
		os.popen(cmdtorun)
		QMessageBox.about(self, "Alert", "Executing: " + cmdtorun)
	
	def liva_run(self):
		# code for Ask / Run button
		displaytext = ''
		cmd = self.outputtext.toPlainText()
		if 'Command' in cmd and 'Result' in cmd:
			self.ask.setText("Ask/Run")
			self.outputtext.setPlainText('')
			self.liva_object = liva.LivaVoice()
		else:
			disp_txt = []
			disp_txt = self.liva_object.liva_run(cmd)
			displaytext = 'Command:- \n----------------- \n' + disp_txt[0] + '\nResult:- \n------------- \n' + disp_txt[1]
			self.ask.setText("Reset")
			self.outputtext.setPlainText(''.join(displaytext))
	
	def take_command(self):
		# code for mic button
		# self.RecordPopup = ProgressPopup()
		# self.RecordPopup.start_animation()
		self.liva_object = liva.LivaVoice()
		cmd = self.liva_object.take_command()
		self.outputtext.setPlainText(cmd)
		# self.RecordPopup.stop_animation()
		# self.RecordPopup.close()

# main
app = QApplication(sys.argv)
welcome = LinuxVoiceAssistant()
widget = QtWidgets.QDialog(welcome)
widget.setModal(True)
# widget.addWidget(welcome)
# widget.setFixedHeight(800)
# widget.setFixedWidth(1200)
# widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting...")
