#!/usr/bin/python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AddToContact(QWidget):
   def __init__(self, parent = None, number=None):
      super(AddToContact, self).__init__(parent)
		
      layout = QFormLayout()
      self.btn = QPushButton("Phone Number")
      self.btn.clicked.connect(self.getphone)#Me marre numrin direkt!!!!
		
      self.le = QLineEdit()
      self.le.setText(number)
      layout.addRow(self.btn,self.le)
      self.btn1 = QPushButton("Name")
      self.btn1.clicked.connect(self.gettext)
		
      self.le1 = QLineEdit()
      layout.addRow(self.btn1,self.le1)
      self.btn2 = QPushButton("Surname")
      self.btn2.clicked.connect(self.gettext)
		
      self.le2 = QLineEdit()
      layout.addRow(self.btn2,self.le2)
      self.setLayout(layout)
      self.setWindowTitle("Add Contact")
		

			
   def gettext(self):
      text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
		
      if ok:
         self.le1.setText(str(number))
			
   def getphone(self):
      num,ok = QInputDialog.getText(self,"integer input dualog", "enter a number")
      self.le2.setText(str(number))
  
def main(): 
   ex = AddToContact(number=sys.argv[1])
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
