import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt



def window():
   app = QApplication(sys.argv)
   w = QWidget()
   layout = QGridLayout(w)
   b = QLabel(w)
   b.setText("In attesa dell'inizio della votazione...")
   w.setGeometry(0,0,1280,720)
   layout.addWidget(b, 0, 0, Qt.AlignCenter)
   w.setWindowTitle("Voting")
   app.setFont(QtGui.QFont("Oxygen",30,QtGui.QFont.Bold))
   app.setStyleSheet("""
      QWidget {
         color: #FFFFFF;
         background-color: #1e3fe8; 
      }
   """)
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()