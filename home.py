#!/usr/bin/python
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from registration import AddToContact
import call
from message import Message

def show_registration(nr):
   ex = AddToContact(number=sys.argv[1])
   ex.show()
   sys.exit(app.exec_())

def show_call():
   ex = call.window()
   ex.show()
   sys.exit(app.exec_())

def show_message():
   ex = Message(number=sys.argv[1])
   ex.show()
   sys.exit(app.exec_())

def window():

   phone_number = sys.argv[1]

   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Phone Number : "+ phone_number)
   w.setGeometry(300,300,500,200)
   b.move(50,20)
  
  # a=QDialog()
   b1=QPushButton(w)
   b1.setText("Add to Contact")
   b1.move(50,100)
   b1.clicked.connect(lambda: show_registration(phone_number))
   
#subprocess.call(['python',Desktop/CoderGals/PhoneClient,self.registration.py])
#b1.clicked.connect(Desktop/CoderGals/PhoneClient,self.registration.py)
   

   b2=QPushButton(w)
   b2.setText("Call")
   b2.move(200,100)
   b2.clicked.connect(show_call)

   b3=QPushButton(w)
   b3.setText("Send Message")
   b3.move(320,100)
   b3.clicked.connect(show_message)

   
 
   w.setWindowTitle("Phone Client")
   w.show()
   sys.exit(app.exec_())
    



	
if __name__ == '__main__':
   print "Number of arguments: ", len(sys.argv)
   print "The first argument is: " , sys.argv[0]
   if len(sys.argv) < 2:
	print "No second argument, you should write a phone number!!!"
	sys.exit(1)
   print "The second argument is: " , sys.argv[1]
   window()
   main()


	
