import sys
from PyQt5 import QtWidgets
'''
	version : 1.0.14112019
'''
class Screen1(QtWidgets.QMainWindow):

	def __init__(self,name) :
	
		QtWidgets.QMainWindow.__init__(self)
		self.setWindowTitle(name)
		self.resize(300,300)
		self.b = QtWidgets.QPushButton('button 1', self)
		self.b.clicked.connect(self.close)
		self.b.move(self.rect().center()-self.b.rect().center())
		
class Screen2(QtWidgets.QMainWindow):

	def __init__(self,name) :
	
		QtWidgets.QMainWindow.__init__(self)
		self.setWindowTitle(name)
		self.resize(300,300)
		self.b = QtWidgets.QPushButton('button 2', self)
		self.b.clicked.connect(self.close)
		self.b.move(self.rect().center()-self.b.rect().center())
		
class Main(QtWidgets.QMainWindow):
	
	def __init__(self) : 
		QtWidgets.QMainWindow.__init__(self)
		self.setWindowTitle('main')
		
		self.stack = QtWidgets.QStackedLayout()
		
		self.scn1 = Screen1('Screen 1')
		self.scn1.b.clicked.connect(lambda:self.goToScreen2(self.scn1,self.scn2))
		self.scn2 = Screen2('Screen 2')
		self.scn2.b.clicked.connect(lambda:self.goToScreen1(self.scn2,self.scn1))
		
		self.stack.addWidget(self.scn1)
		self.stack.addWidget(self.scn2)
		
	def goToScreen1(self,source,dest):
		dest.move(source.x(),source.y())
		self.stack.setCurrentIndex(0)
		
	def goToScreen2(self,source,dest):
		dest.move(source.x(),source.y())
		self.stack.setCurrentIndex(1)
		
if __name__ == '__main__' : 

	app = QtWidgets.QApplication([])
	main = Main()
	sys.exit(app.exec_())