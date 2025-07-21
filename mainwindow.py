# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import SIGNAL, QObject

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

import Parser

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QObject.connect(self.ui.button_process, SIGNAL ('clicked()'),
            lambda mw=self: MainWindow.processWord(mw))

        # QObject.connect(self.ui.slider_example, SIGNAL ('valueChanged(value)'), self.processExamples)
        self.ui.slider_example.valueChanged.connect(self.processExamples)


    def processWord(self):
        self.clearAll()

        word = self.ui.lineEdit_vocabulary.text()
        parser.load(word)

        self.ui.plainTextEdit_grammar.appendPlainText(parser.getGrammar())

        self.ui.plainTextEdit_meaning.appendPlainText(parser.getDefinition())

        self.ui.plainTextEdit_examples.appendPlainText(parser.getExamples(3))

        print('Processed')

    def processExamples(self, value):
        self.ui.plainTextEdit_examples.clear()
        self.ui.plainTextEdit_examples.appendPlainText(parser.getExamples(value))
        print('Processed examples')


    def clearAll(self):
        self.ui.plainTextEdit_grammar.clear()
        self.ui.plainTextEdit_meaning.clear()
        self.ui.plainTextEdit_examples.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    parser = Parser.Parser();
    sys.exit(app.exec())
