# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import SIGNAL, QObject

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o ui_form.py
from ui_form import Ui_MainWindow

import Parser

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QObject.connect(self.ui.vocab_button_process, SIGNAL ('clicked()'),
            lambda mw=self: MainWindow.processWord(mw))

        # QObject.connect(self.ui.slider_example, SIGNAL ('valueChanged(value)'), self.processExamples)
        self.ui.examples_slider.valueChanged.connect(self.processExamples)


    def processWord(self):
        self.clearAll()

        word = self.ui.vocab_lineEdit.text()
        parser.process(word)

        self.ui.grammar_plainTextEdit.appendPlainText(parser.getGrammar())

        self.ui.meaning_plainTextEdit.appendPlainText(parser.getDefinitions())

        self.ui.examples_plainTextEdit.appendPlainText(parser.getExamples(2))

        print('Processed')

    def processExamples(self, value):
        self.ui.examples_plainTextEdit.clear()
        self.ui.examples_plainTextEdit.appendPlainText(parser.getExamples(value))
        print('Processed examples')


    def clearAll(self):
        self.ui.grammar_plainTextEdit.clear()
        self.ui.meaning_plainTextEdit.clear()
        self.ui.examples_plainTextEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    parser = Parser.Parser();
    sys.exit(app.exec())
