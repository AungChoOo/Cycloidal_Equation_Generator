import sys
import time
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout,QLabel,QLineEdit
# from PyQt5.QtWidgets import (QApplication,QWidget,QSlider,QLabel,
# 							QGroupBox,QVBoxLayout,QGridLayout)
R = 0
E = 0
Rr = 0
N = 0

class Example():
	def __init__(self):
		self.widget = QWidget()
		self.widget.setWindowTitle("Cycloidal Disk")
		self.widget.setGeometry(0,0,600,200)
		self.widget.show()
		self.initUI()

	def initUI(self):
		
		self.ring = QLineEdit()
		self.ring.setPlaceholderText("Enter Ring Radius")
		self.eccentricity = QLineEdit()
		self.eccentricity.setPlaceholderText("Enter Eccentricity")
		self.pin = QLineEdit()
		self.pin.setPlaceholderText("Enter Pin Radius")
		self.number = QLineEdit()
		self.number.setPlaceholderText("Enter Number of pins")

		self.linex = QLineEdit()
		self.linex.setReadOnly(True)
		self.linex.setPlaceholderText("X")
		self.liney = QLineEdit()
		self.liney.setReadOnly(True)
		self.liney.setPlaceholderText("Y")

		self.button = QPushButton('Enter')
		self.button.setStyleSheet("QPushButton {background-color : white;}"
		                     "QPushButton::hover{background-color : orange;}"
		                     "QPushButton::pressed{background-color : red;}") 
		self.button.clicked.connect(self.calculated)

		self.reset = QPushButton('Reset')
		self.reset.setStyleSheet("QPushButton {background-color : white;}"
		                     "QPushButton::hover{background-color : orange;}"
		                     "QPushButton::pressed{background-color : red;}") 
		self.reset.clicked.connect(self.reseted)

		layout = QGridLayout()
		layout.addWidget(self.ring,0,0)
		layout.addWidget(self.eccentricity,1,0)
		layout.addWidget(self.pin,2,0)
		layout.addWidget(self.number,3,0)
		layout.addWidget(self.button,4,0)
		layout.addWidget(self.reset,5,0)
		layout.addWidget(self.linex,6,0)
		layout.addWidget(self.liney,7,0)
		self.widget.setLayout(layout)

	def calculated(self):
		R = int(self.ring.text())
		E = int(self.eccentricity.text())
		Rr = int(self.pin.text())
		N = int(self.number.text())

		R_EN = R/(E*N)
		NmE = N-E
		_N = 1-N

		X = "({}*cos(t))- ( {}*cos( t+arctan( sin({}*t)/({} - cos({}*t)) ))) - ({}*cos({}*t)) ".format(R,Rr,_N,R_EN,_N,E,N)
		Y = "({}*sin(t))- ( {}*sin( t+arctan( sin({}*t)/({} - cos({}*t)) ))) - ({}*sin({}*t)) ".format(R,Rr,_N,R_EN,_N,E,N)

		self.linex.setText(X)
		self.liney.setText(Y)

	def reseted(self):
		self.ring.clear()
		self.eccentricity.clear()
		self.pin.clear()
		self.number.clear()
		self.linex.clear()
		self.liney.clear()


def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()