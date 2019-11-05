import Sherlock
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 413)
        font = QtGui.QFont()

        font.setWeight(50)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(40, 260, 231, 61))
        font.setPointSize(18)
        self.Titulo.setFont(font)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 280, 231, 31))
        font.setPointSize(20)
        self.lineEdit.setFont(font)

        self.validacion = QtWidgets.QLabel(self.centralwidget)
        self.validacion.setGeometry(QtCore.QRect(280, 300, 221, 61))
        font.setPointSize(18)
        self.validacion.setFont(font)

        self.enter = QtWidgets.QLabel(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(70, 300, 141, 31))
        font.setPointSize(14)
        self.enter.setFont(font)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 131, 121))
        self.label.setPixmap(QtGui.QPixmap("Holmes.png"))
        self.label.setScaledContents(True)


        self.principal_title = QtWidgets.QLabel(self.centralwidget)
        self.principal_title.setGeometry(QtCore.QRect(50, 180, 501, 51))
        font.setFamily("MS Sans Serif")
        font.setPointSize(30)
        self.principal_title.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.returnPressed.connect(self.send)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sherlock and the valid string"))
        MainWindow.setWindowIcon(QtGui.QIcon("Holmes.png"))
        self.Titulo.setText(_translate("MainWindow", "Ingrese una Cadena"))
        self.validacion.setText(_translate("MainWindow", "Validacion: "))
        self.enter.setText(_translate("MainWindow", "(Precione Enter)"))
        self.principal_title.setText(_translate("MainWindow", "Sherlock and the valid string"))

    def send(self):
        solucion = Sherlock.solucion(self.lineEdit.text())
        if solucion.verificacion():
            aux= solucion.verificacion()
            self.validacion.setText(aux)
            self.validacion.adjustSize()
        else:
            aux = solucion.soluc()
            self.validacion.setText(aux)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
