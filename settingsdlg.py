import sys
import os
import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox


class Settings(QDialog):
	def __init__(self):
		super(Settings, self).__init__()
		uic.loadUi("./res/settings.ui",self)
		self.params = self.load_params()
		self.desettings.clicked.connect(self.open_desttings_mthd)
		self.sttconfig.clicked.connect(self.open_sttconfig_mthd)
		self.livaconfig.clicked.connect(self.liva_edit_config_mthd)
		self.ok.clicked.connect(self.ok_mthd)
		self.cancel.clicked.connect(self.cancel_mthd)
		self.show()
	
	def load_params(self):
		with open(os.path.expanduser("~/.config/liva/liva-config.json"), 'r') as jsf:
			self.params = json.load(jsf)
	
	def open_desttings_mthd(self):
		dechoice = self.decombo.currentIndex()
		if dechoice == 0: # budgie
			cmd = 'budgie-desktop-settings'
		elif dechoice == 1: # cinnamon
			cmd = 'cinnamon-settings'
		elif dechoice == 2: # gnome
			cmd = 'gnome-control-center'
		elif dechoice == 3: # Lx-Qt
			cmd = 'lxqt-config'
		elif dechoice == 4: # mate
			cmd = 'mate-control-center'
		elif dechoice == 5: # pantheon
			cmd = 'switchboard'
		elif dechoice == 6: # plasma
			cmd = 'systemsettings5'
		elif dechoice == 7: # unity
			cmd = 'unity-control-center'
		elif dechoice == 8: # Xfce
			cmd = 'xfce4-settings-manager'
		else:
			cmd = 'unknown'
		self.exec_cmd_settings(cmd)
	
	def liva_edit_config_mthd(self):
		# term = self.params['Liva_options']['terminal_emulator']
		term = 'xterm'
		# cmd =  self.params['Liva_options']['text_editor'] + ' ' +  self.params['Liva_options']['config_file']
		cmd = 'vim ' + str(os.path.expanduser('~/.config/liva/liva-config.json'))
		self.exec_cmd_settings(term + ' -hold -e ' + cmd)
	
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

