import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   w.setGeometry(300,300,500,200)
   b = QPushButton(w)
   b.setText("Call")
   b.move(150,80)
   b.clicked.connect(showdialog)


   b = QPushButton(w)
   b.setText("Back")
   b.move(250,80)
   #b.clicked.connect(showdialog)


   w.setWindowTitle("Make a call!")
   w.show()
   sys.exit(app.exec_())

def showdialog():
   d = QDialog()

   b1 = QPushButton("Direct Call",d)
   b2 = QPushButton("Viber",d)
   b2.move(200,50)
   b1.move(50,50)
   d.setWindowTitle("Choose action!")
   d.setWindowModality(Qt.ApplicationModal)
   d.exec_()

if __name__ == '__main__':
   window()
