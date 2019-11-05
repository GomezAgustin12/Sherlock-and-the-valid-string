import Sherlock
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Sherlock and the valid string")
        MainWindow.resize(575, 400)
        font = QtGui.QFont()
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(100, 20, 371, 61))
        font.setPointSize(30)
        self.Titulo.setFont(font)


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 160, 291, 61))
        font.setPointSize(20)
        self.lineEdit.setFont(font)

        self.validacion = QtWidgets.QLabel(self.centralwidget)
        self.validacion.setGeometry(QtCore.QRect(130, 240, 291, 61))
        font.setPointSize(24)
        self.validacion.setFont(font)

        self.enter = QtWidgets.QLabel(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(160, 110, 241, 31))
        self.enter.setFont(font)

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

    def send(self):
        solucion = Sherlock.solucion(self.lineEdit.text())
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
