from hackathon import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import opencam
class App(QWidget):
			def __init__(self):
							super().__init__()
							self.title='HerbyKnows!'
							self.left=10
							self.top=10
							self.width=640
							self.height=480
							self.initUI()

			def initUI(self):
							self.setWindowTitle(self.title)
							self.setGeometry(self.left,self.top,self.width,self.height)
							button=QPushButton('Get information',self)
							button.clicked.connect(self.click)
							button2=QPushButton('Use Camera',self)
							button2.clicked.connect(self.capture)
							#button.setToolTip('YAA YEET')
							button.move(100,200)
							# button1.move(100,100)
							button2.move(100,300)
							self.show()

			def openFileNameDialog(self):
							fileName, _ = QFileDialog.getOpenFileName(self,"Select Image", "","All Files (*);;Python Files (*.py)")
							if fileName:
								return (fileName) 

			def capture(self):
							userip=opencam.capture()
							


			def click(self):
							userip=self.openFileNameDialog()
							flower_name=get_name(userip)
							print(flower_name)
							list1=content(flower_name)
							for i in list1:
								print(i)


if __name__=='__main__':
				app=QApplication(sys.argv)
				ex=App()
				sys.exit(app.exec_())
				# userip=ex.openFileNameDialog()
				# flower_name=get_name(userip)
				# print(flower_name)