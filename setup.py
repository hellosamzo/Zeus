from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(200, 200, 300, 300)
		self.setWindowTitle("Zeus")
		self.initUI()
	
	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Test Label")
		self.label.move(50,50)

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Click Me")
		self.b1.clicked.connect(self.b1_clicked)

	def b1_clicked(self):
		self.label.setText("pressed")
		self.update()

	def update(self):
		self.label.setStyleSheet("border: 1px solid black;")
		self.label.adjustSize()

def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()