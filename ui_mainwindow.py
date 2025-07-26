# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vocab_layout = QHBoxLayout()
        self.vocab_layout.setObjectName(u"vocab_layout")
        self.vocab_label = QLabel(self.centralwidget)
        self.vocab_label.setObjectName(u"vocab_label")

        self.vocab_layout.addWidget(self.vocab_label)

        self.vocab_lineEdit = QLineEdit(self.centralwidget)
        self.vocab_lineEdit.setObjectName(u"vocab_lineEdit")

        self.vocab_layout.addWidget(self.vocab_lineEdit)

        self.vocab_button_process = QPushButton(self.centralwidget)
        self.vocab_button_process.setObjectName(u"vocab_button_process")

        self.vocab_layout.addWidget(self.vocab_button_process)


        self.verticalLayout.addLayout(self.vocab_layout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.gridLayout_grammar = QGridLayout(self.widget)
        self.gridLayout_grammar.setObjectName(u"gridLayout_grammar")
        self.gridLayout_grammar.setContentsMargins(0, 0, 0, 0)
        self.grammar_button_copy = QPushButton(self.widget)
        self.grammar_button_copy.setObjectName(u"grammar_button_copy")

        self.gridLayout_grammar.addWidget(self.grammar_button_copy, 0, 2, 1, 1)

        self.grammar_label = QLabel(self.widget)
        self.grammar_label.setObjectName(u"grammar_label")

        self.gridLayout_grammar.addWidget(self.grammar_label, 0, 0, 1, 1)

        self.grammar_spacer_label = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_grammar.addItem(self.grammar_spacer_label, 1, 0, 1, 1)

        self.grammar_spacer_copy = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_grammar.addItem(self.grammar_spacer_copy, 1, 2, 1, 1)

        self.grammar_plainTextEdit = QPlainTextEdit(self.widget)
        self.grammar_plainTextEdit.setObjectName(u"grammar_plainTextEdit")

        self.gridLayout_grammar.addWidget(self.grammar_plainTextEdit, 0, 1, 2, 1)

        self.gridLayout_grammar.setColumnStretch(1, 1)
        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.gridLayout_meaning = QGridLayout(self.widget1)
        self.gridLayout_meaning.setObjectName(u"gridLayout_meaning")
        self.gridLayout_meaning.setContentsMargins(0, 0, 0, 0)
        self.meaning_label = QLabel(self.widget1)
        self.meaning_label.setObjectName(u"meaning_label")

        self.gridLayout_meaning.addWidget(self.meaning_label, 0, 0, 1, 1)

        self.meaning_button_copy = QPushButton(self.widget1)
        self.meaning_button_copy.setObjectName(u"meaning_button_copy")

        self.gridLayout_meaning.addWidget(self.meaning_button_copy, 0, 2, 1, 1)

        self.meaning_spacer_label = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_meaning.addItem(self.meaning_spacer_label, 1, 0, 1, 1)

        self.meaning_spacer_copy = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_meaning.addItem(self.meaning_spacer_copy, 1, 2, 1, 1)

        self.meaning_plainTextEdit = QPlainTextEdit(self.widget1)
        self.meaning_plainTextEdit.setObjectName(u"meaning_plainTextEdit")

        self.gridLayout_meaning.addWidget(self.meaning_plainTextEdit, 0, 1, 2, 1)

        self.gridLayout_meaning.setColumnStretch(1, 1)
        self.splitter.addWidget(self.widget1)
        self.widget2 = QWidget(self.splitter)
        self.widget2.setObjectName(u"widget2")
        self.gridLayout_examples = QGridLayout(self.widget2)
        self.gridLayout_examples.setObjectName(u"gridLayout_examples")
        self.gridLayout_examples.setContentsMargins(0, 0, 0, 0)
        self.examples_slider = QSlider(self.widget2)
        self.examples_slider.setObjectName(u"examples_slider")
        self.examples_slider.setMinimum(1)
        self.examples_slider.setMaximum(5)
        self.examples_slider.setValue(2)
        self.examples_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_examples.addWidget(self.examples_slider, 1, 2, 1, 1)

        self.examples_button_copy = QPushButton(self.widget2)
        self.examples_button_copy.setObjectName(u"examples_button_copy")

        self.gridLayout_examples.addWidget(self.examples_button_copy, 0, 2, 1, 1)

        self.examples_label = QLabel(self.widget2)
        self.examples_label.setObjectName(u"examples_label")

        self.gridLayout_examples.addWidget(self.examples_label, 0, 0, 1, 1)

        self.examples_spacer_copy = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_examples.addItem(self.examples_spacer_copy, 2, 2, 1, 1)

        self.examples_spacer_label = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_examples.addItem(self.examples_spacer_label, 1, 0, 2, 1)

        self.examples_plainTextEdit = QPlainTextEdit(self.widget2)
        self.examples_plainTextEdit.setObjectName(u"examples_plainTextEdit")

        self.gridLayout_examples.addWidget(self.examples_plainTextEdit, 0, 1, 3, 1)

        self.gridLayout_examples.setColumnStretch(1, 1)
        self.splitter.addWidget(self.widget2)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.vocab_label.setText(QCoreApplication.translate("MainWindow", u"Vokabular", None))
        self.vocab_lineEdit.setText(QCoreApplication.translate("MainWindow", u"Buch", None))
        self.vocab_button_process.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.grammar_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.grammar_label.setText(QCoreApplication.translate("MainWindow", u"Grammatik", None))
        self.meaning_label.setText(QCoreApplication.translate("MainWindow", u"Bedeutung", None))
        self.meaning_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.examples_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.examples_label.setText(QCoreApplication.translate("MainWindow", u"Beispiele", None))
    # retranslateUi

