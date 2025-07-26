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

        QObject.connect(self.ui.grammar_button_copy, SIGNAL ('clicked()'),
            lambda mw=self: MainWindow.copyGrammer(mw))

        QObject.connect(self.ui.meaning_button_copy, SIGNAL ('clicked()'),
            lambda mw=self: MainWindow.copyMeanings(mw))

        QObject.connect(self.ui.examples_button_copy, SIGNAL ('clicked()'),
            lambda mw=self: MainWindow.copyExamples(mw))

        # QObject.connect(self.ui.slider_example, SIGNAL ('valueChanged(value)'), self.processExamples)
        self.ui.examples_slider.valueChanged.connect(self.processExamples)

        minimum_width_left = 70
        self.ui.vocab_label.setMinimumWidth(minimum_width_left)
        self.ui.grammar_label.setMinimumWidth(minimum_width_left)
        self.ui.meaning_label.setMinimumWidth(minimum_width_left)
        self.ui.examples_label.setMinimumWidth(minimum_width_left)

        minimum_width_right = 100
        self.ui.vocab_button_process.setMinimumWidth(minimum_width_right)
        self.ui.grammar_button_copy.setMinimumWidth(minimum_width_right)
        self.ui.meaning_button_copy.setMinimumWidth(minimum_width_right)
        self.ui.examples_button_copy.setMinimumWidth(minimum_width_right)

        self.ui.splitter.setStretchFactor(0,1)
        self.ui.splitter.setStretchFactor(1,5)
        self.ui.splitter.setStretchFactor(2,5)


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

    def copyGrammer(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.grammar_plainTextEdit.toPlainText())

    def copyMeanings(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.meaning_plainTextEdit.toPlainText())

    def copyExamples(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.examples_plainTextEdit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    parser = Parser.Parser();
    sys.exit(app.exec())
