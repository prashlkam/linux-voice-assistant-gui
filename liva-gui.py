#!/usr/bin/env python3

import sys
import os
import livavoice as liva
import settingsdlg as liva_settings
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox, QLabel
from PyQt5.Qt import QClipboard

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
		self.settings_dialog = liva_settings.Settings()
		self.settings_dialog.show()
	
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
