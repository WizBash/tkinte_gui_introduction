# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splashscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.setEnabled(True)
        SplashScreen.resize(699, 400)
        SplashScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint) # removing title bar
        SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.timer = QtCore.QTimer()
        


        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shadhowframe = QtWidgets.QFrame(self.centralwidget)
        self.shadhowframe.setStyleSheet("QFrame{\n"
"    background-color: rgb(85, 0, 127);\n"
"    color: rgb(255, 99, 252);\n"
"    border-radius:50px;\n"
"}")

                #==========================remove title bar================================
        #self.SplashScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadhowframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shadhowframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shadhowframe.setObjectName("shadhowframe")
        self.label = QtWidgets.QLabel(self.shadhowframe)
        self.label.setGeometry(QtCore.QRect(50, 50, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yi Baiti")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.shadhowframe)
        self.label_2.setGeometry(QtCore.QRect(370, 90, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.shadhowframe)
        self.progressBar.setGeometry(QtCore.QRect(20, 230, 641, 31))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(127, 58, 126);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style:none;\n"
"    border-radius:15px;\n"
"    text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.506, stop:0 rgba(116, 7, 156, 255), stop:0.482955 rgba(220, 78, 226, 255), stop:1 rgba(255, 170, 255, 255));\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 9)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.shadhowframe)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 661, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.shadhowframe)
        self.label_4.setGeometry(QtCore.QRect(50, 350, 251, 20))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.shadhowframe)
        self.label_5.setGeometry(QtCore.QRect(370, 350, 271, 20))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.shadhowframe)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label.setText(_translate("SplashScreen", "HiSCHOOL"))
        self.label_2.setText(_translate("SplashScreen", "Management System"))
        self.label_3.setText(_translate("SplashScreen", "Loading..."))
        self.label_4.setText(_translate("SplashScreen", "<strong>Developer </strong>: Wabwire Brian   "))
        self.label_5.setText(_translate("SplashScreen", "wizbash01@gmail.com    +256784335700"))

        #==========================remove title bar================================
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.timer.timeout.connect(self.progressBar)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
