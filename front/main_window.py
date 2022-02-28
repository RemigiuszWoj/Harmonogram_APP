# import tkinter

# root = tkinter.Tk()

# message = tkinter.Label(root, text="Hello, World!", highlightbackground='white')
# message.pack()

# root.mainloop()


# #!/usr/bin/env python3

# import tkinter as tk
# from tkinter.font import Font

# class Pad(tk.Frame):

#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)

#         self.toolbar = tk.Frame(self, bg="#eee")
#         self.toolbar.pack(side="top", fill="x")

#         self.bold_btn = tk.Button(self.toolbar, text="Bold", command=self.make_bold)
#         self.bold_btn.pack(side="left")

#         self.clear_btn = tk.Button(self.toolbar, text="Clear", command=self.clear)
#         self.clear_btn.pack(side="left")

#         # Creates a bold font
#         self.bold_font = Font(family="Helvetica", size=14, weight="bold")

#         self.text = tk.Text(self)
#         self.text.insert("end", "Select part of text and then click 'Bold'...")
#         self.text.focus()
#         self.text.pack(fill="both", expand=True)

#         # configuring a tag called BOLD
#         self.text.tag_configure("BOLD", font=self.bold_font)

#     def make_bold(self):
#         # tk.TclError exception is raised if not text is selected
#         try:
#             self.text.tag_add("BOLD", "sel.first", "sel.last")        
#         except tk.TclError:
#             pass

#     def clear(self):
#         self.text.tag_remove("BOLD",  "1.0", 'end')


# def demo():
#     root = tk.Tk()
#     Pad(root).pack(expand=1, fill="both")
#     root.mainloop()


# if __name__ == "__main__":
#     demo()

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 401, 231))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 250, 321, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 240, 91, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))

# coding: utf-8
import sys
from PyQt5.QtWidgets import *
# from test import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec_())