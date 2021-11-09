import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox


class Settings(QDialog):
	def __init__(self):
		super(Settings, self).__init__()
		uic.loadUi("./res/settings.ui",self)
		self.ok.clicked.connect(self.ok_mthd)
		self.ok.clicked.connect(self.cancel_mthd)
		self.show()
		
	def ok_mthd(self):
		pass
	
	def cancel_mthd(self):
		pass
	

# main
app = QApplication(sys.argv)
settingsdlg = Settings()
widget = QtWidgets.QDialog(settingsdlg)
widget.setModal(True)
# widget.addWidget(settingsdlg)
# widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting...")

