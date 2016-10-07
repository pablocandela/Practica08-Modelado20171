import sys
from PyQt4 import QtGui,QtCore, uic

class Ventana(QtGui.QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        uic.loadUi('servidor.ui', self)
        header_horizontal = self.tableWidget.horizontalHeader()
        header_horizontal.setResizeMode(QtGui.QHeaderView.Stretch)
        header_vertical = self.tableWidget.verticalHeader()
        header_vertical.setResizeMode(QtGui.QHeaderView.Stretch)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
