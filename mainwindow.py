# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import SIGNAL, QObject

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

import Parser

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QObject.connect(self.ui.pushButton, SIGNAL ('clicked()'),
            lambda mw=self: testFunc(mw))

def testFunc(main_window):
    parser.load('seufzen')
    main_window.ui.plainTextEdit_grammar.clear()
    main_window.ui.plainTextEdit_grammar.appendPlainText(parser.getGrammar())


    print('Processed')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    parser = Parser.Parser();
    sys.exit(app.exec())
