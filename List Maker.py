from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List")
        self.setFixedSize(500,500)

        Central_Widget = QWidget(self)
        self.setCentralWidget(Central_Widget)

        #Layout 1
        Layout = QVBoxLayout()
        Central_Widget.setLayout(Layout)
        Layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        Layout.setContentsMargins(40,40,40,100)

        #Label 1
        self.Label_1 = QLabel("Title",self)
        self.Label_1.setAlignment(Qt.AlignHCenter)
        self.Font_1 = self.Label_1.font()
        self.Font_1.setPointSize(20)
        self.Label_1.setFont(self.Font_1)
        Layout.addWidget(self.Label_1)

        #Line Edit 1
        Line_Edit = QLineEdit(self)
        Layout.addWidget(Line_Edit)

        #Button 1
        self.Button_1 = QPushButton("Push",self)
        self.Button_1.clicked.connect(lambda: self.Button_1_Clicked(Line_Edit.text()))
        Layout.addWidget(self.Button_1)

        #List 1
        self.list = QListWidget(self)
        self.list.itemClicked.connect(self.List_Remove)
        Layout.addWidget(self.list)

    def Button_1_Clicked(self,text):
        self.list.addItem(text)

    def List_Remove(self,item):
        self.list.takeItem(self.list.row(item))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()