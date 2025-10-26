# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import SIGNAL, QObject

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic mainwindow.ui -o ui_form.py
from ui_form import Ui_MainWindow

import Parser
import BuildTime as bt

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        menubar = self.menuBar()
        menu = menubar.addMenu('Help')
        about_action = menu.addAction("About")
        about_action.setStatusTip("Show build information about the program.")
        about_action.triggered.connect(self.showAbout)

        self.initSignals()
        self.initGui()

        return

    def initSignals(self):
        self.ui.vocab_lineEdit.editingFinished.connect(self.processWord)

        QObject.connect(self.ui.vocab_button_copy, SIGNAL ('clicked()'), lambda mw=self: MainWindow.copyWord(mw))

        QObject.connect(self.ui.grammar_button_copy, SIGNAL ('clicked()'), lambda mw=self: MainWindow.copyGrammer(mw))

        QObject.connect(self.ui.meaning_button_copy, SIGNAL ('clicked()'), lambda mw=self: MainWindow.copyMeanings(mw))

        QObject.connect(self.ui.examples_button_copy, SIGNAL ('clicked()'), lambda mw=self: MainWindow.copyExamples(mw))

        QObject.connect(self.ui.thesaurus_button_copy, SIGNAL ('clicked()'), lambda mw=self: MainWindow.copyThesaurus(mw))

        QObject.connect(self.ui.tag_button_copy, SIGNAL ('clicked()'), lambda mw=self: MainWindow.copyTags(mw))

        self.ui.examples_slider.valueChanged.connect(self.processExamples)
        return

    def initGui(self):
        minimum_width_left = 70
        self.ui.vocab_label.setMinimumWidth(minimum_width_left)
        self.ui.grammar_label.setMinimumWidth(minimum_width_left)
        self.ui.meaning_label.setMinimumWidth(minimum_width_left)
        self.ui.examples_label.setMinimumWidth(minimum_width_left)
        self.ui.thesaurus_label.setMinimumWidth(minimum_width_left)
        self.ui.tag_label.setMinimumWidth(minimum_width_left)

        minimum_width_right = 100
        self.ui.vocab_button_copy.setMinimumWidth(minimum_width_right)
        self.ui.grammar_button_copy.setMinimumWidth(minimum_width_right)
        self.ui.meaning_button_copy.setMinimumWidth(minimum_width_right)
        self.ui.examples_button_copy.setMinimumWidth(minimum_width_right)
        self.ui.thesaurus_button_copy.setMinimumWidth(minimum_width_right)
        self.ui.tag_button_copy.setMinimumWidth(minimum_width_right)

        self.ui.splitter.setStretchFactor(0,1)
        self.ui.splitter.setStretchFactor(1,5)
        self.ui.splitter.setStretchFactor(2,5)
        self.ui.splitter.setStretchFactor(3,5)
        return

    def processWord(self):
        self.clearAll()

        word = self.ui.vocab_lineEdit.text()
        parser.process(word)
        example_count = 2

        if (self.ui.examples_slider.value() == example_count):
            self.processExamples(example_count)
        else:
            self.ui.examples_slider.setValue(example_count)

        self.ui.grammar_plainTextEdit.appendPlainText(parser.getGrammar())

        self.ui.meaning_plainTextEdit.appendPlainText(parser.getDefinitions())

        self.ui.tag_lineEdit.setText(parser.getTags())

        self.ui.thesaurus_plainTextEdit.appendPlainText(parser.getThesaurus())

        return

    def processExamples(self, value):
        self.ui.examples_plainTextEdit.clear()
        self.ui.examples_plainTextEdit.appendPlainText(parser.getExamples(value))
        self.ui.examples_label_count.setText(str(value))

        return

    def clearAll(self):
        self.ui.grammar_plainTextEdit.clear()
        self.ui.meaning_plainTextEdit.clear()
        self.ui.examples_plainTextEdit.clear()
        self.ui.thesaurus_plainTextEdit.clear()
        return

    def copyWord(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.vocab_lineEdit.text())
        return

    def copyGrammer(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.grammar_plainTextEdit.toPlainText())
        return

    def copyMeanings(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.meaning_plainTextEdit.toPlainText())
        return

    def copyExamples(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.examples_plainTextEdit.toPlainText())
        return

    def copyThesaurus(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.thesaurus_plainTextEdit.toPlainText())
        return

    def copyTags(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.tag_lineEdit.text())
        return

    def showAbout(self):
        build_time = bt.BuildTime()
        about_box = QMessageBox()
        about_box.setWindowTitle('About')
        display_text = 'Version 1.2.3\n'
        display_text += 'Built on: '+build_time.get()
        about_box.setText(display_text)
        about_box.exec()
        return

    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    parser = Parser.Parser();
    sys.exit(app.exec())
