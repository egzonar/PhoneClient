import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Message(QWidget):
	def __init__(self, parent = None, number='123'):
		super(Message, self).__init__(parent)

		layout = QFormLayout()
		self.btn = QPushButton("Phone number")

		self.le = QLineEdit()
		self.le.setText(number)
		layout.addRow(self.btn,self.le)
		self.btn1 = QPushButton("Type message")
		self.btn1.clicked.connect(self.gettext)

		self.le1 = QLineEdit()
		layout.addRow(self.btn1,self.le1)

		self.setLayout(layout)
		self.setWindowTitle("Phone client information")

	def show_success_notification(self):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText("Message sent!")
		#msg.setInformativeText("This is additional information")
		msg.setWindowTitle("Message Information")
		#msg.setDetailedText("The details are as follows:")
		msg.show()
		sys.exit(app.exec_())
		
	def gettext(self):
		text, ok = QInputDialog.getText(self, 'Message input box', 'Enter your message')

		if ok:
			self.le1.setText(str(text))
			self.show_success_notification()
			

	def getint(self):
		num,ok = QInputDialog.getInt(self,"integer input dualog", "enter a number")
		self.le2.setText(str(number))
	def window():
	   app = QApplication(sys.argv)
	   w = QWidget()
	   b = QPushButton(w)
	   b.setText("Message sent!")
	   b.move(50,50)
	   b.clicked.connect(showdialog)
	   w.setWindowTitle("Message Information")
	   w.show()
	   sys.exit(app.exec_())


def main(): 
	app = QApplication(sys.argv)
	ex = Message(number=sys.argv[1])
	ex.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
   print "Number of arguments: ", len(sys.argv)
   print "The first argument is: " , sys.argv[0]
   if len(sys.argv) < 2:
	print "No second argument, you should write a phone number!!!"
	sys.exit(1)
   print "The second argument is: " , sys.argv[1]
 
   main()
	
	
	
