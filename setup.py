from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def b1_clicked():
	print("clicked")

def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(200, 200, 300, 300)
	win.setWindowTitle("Zeus")

	label = QtWidgets.QLabel(win)
	label.setText("Test Label")
	label.move(50,50)

	b1 = QtWidgets.QPushButton(win)
	b1.setText("Click Me")
	b1.clicked.connect(b1_clicked)

	win.show()
	sys.exit(app.exec_())

window()