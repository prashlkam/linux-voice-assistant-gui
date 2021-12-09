import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox


class Settings(QDialog):
	def __init__(self):
		super(Settings, self).__init__()
		uic.loadUi("./res/settings.ui",self)
		self.desettings.clicked.connect(self.open_desttings_mthd)
		self.sttconfig.clicked.connect(self.open_sttconfig_mthd)
		self.ok.clicked.connect(self.ok_mthd)
		self.cancel.clicked.connect(self.cancel_mthd)
		self.show()
	
	def open_desttings_mthd(self):
		dechoice = self.decombo.currentIndex()
		if dechoice == 0: # budgie
			cmd = 'budgie-desktop-settings'
		elif dechoice == 1: # cinnamon
			cmd = 'cinnamon-settings'
		elif dechoice == 2: # gnome
			cmd = 'gnome-control-center'
		elif dechoice == 3: # mate
			cmd = 'mate-control-center'
		elif dechoice == 4: # pantheon
			cmd = 'switchboard'
		elif dechoice == 5: # plasma
			cmd = 'systemsettings5'
		elif dechoice == 6: # unity
			cmd = 'unity-control-center'
		else:
			cmd = 'unknown'
		self.exec_cmd_settings(cmd)
	
	def open_sttconfig_mthd(self):
		QMessageBox.about(self, "Alert", "Not yet implemented...")
	
	def exec_cmd_settings(self, cmd):
		if not 'unknown' in cmd and not cmd == '':
			os.popen(cmd)
		else:
			QMessageBox.about(self, "Alert", "Couldn't find the Control Center for your Desktop...")
	
	def ok_mthd(self):
		self.close()
	
	def cancel_mthd(self):
		self.close()
	

# # main
# app = QApplication(sys.argv)
# settingsdlg = Settings()
# widget = QtWidgets.QDialog(settingsdlg)
# widget.setModal(True)
# # widget.addWidget(settingsdlg)
# # widget.show()
# try:
    # sys.exit(app.exec_())
# except:
    # print("Exiting...")

