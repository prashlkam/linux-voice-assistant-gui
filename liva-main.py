import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox
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
	
	
	def copy_clpboard(self):
		self.outputtext.selectAll()
		self.outputtext.copy()
	
	def help_func(self):
		# replace ls with man page for liva - TBD
		os.popen("konsole -e man ls")
	
	def settings_func(self):
		QMessageBox.about(self, "Alert", "Not yet implemented...")
	
	def quit_app(self):
		self.close()
	
	def exec_cmd(self):
		# talk("Executing command " + cmdtorun)
		cmdtorun = self.outputtext.toPlainText()
		QMessageBox.about(self, "Alert", "Executing: " + cmdtorun)
		os.popen(cmdtorun)
	
	def liva_run():
		pass
		
	def take_command():
		pass
		

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
