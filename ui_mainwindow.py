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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_process = QPushButton(self.centralwidget)
        self.button_process.setObjectName(u"button_process")
        self.button_process.setGeometry(QRect(700, 10, 80, 24))
        self.lineEdit_vocabulary = QLineEdit(self.centralwidget)
        self.lineEdit_vocabulary.setObjectName(u"lineEdit_vocabulary")
        self.lineEdit_vocabulary.setGeometry(QRect(100, 10, 591, 24))
        self.label_vocab = QLabel(self.centralwidget)
        self.label_vocab.setObjectName(u"label_vocab")
        self.label_vocab.setGeometry(QRect(10, 10, 71, 21))
        self.label_grammar = QLabel(self.centralwidget)
        self.label_grammar.setObjectName(u"label_grammar")
        self.label_grammar.setGeometry(QRect(10, 100, 71, 21))
        self.label_meaning = QLabel(self.centralwidget)
        self.label_meaning.setObjectName(u"label_meaning")
        self.label_meaning.setGeometry(QRect(10, 170, 71, 21))
        self.label_examples = QLabel(self.centralwidget)
        self.label_examples.setObjectName(u"label_examples")
        self.label_examples.setGeometry(QRect(10, 320, 71, 21))
        self.slider_example = QSlider(self.centralwidget)
        self.slider_example.setObjectName(u"slider_example")
        self.slider_example.setGeometry(QRect(100, 320, 201, 20))
        self.slider_example.setMinimum(2)
        self.slider_example.setMaximum(5)
        self.slider_example.setOrientation(Qt.Orientation.Horizontal)
        self.plainTextEdit_grammar = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_grammar.setObjectName(u"plainTextEdit_grammar")
        self.plainTextEdit_grammar.setGeometry(QRect(100, 90, 591, 51))
        self.plainTextEdit_meaning = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_meaning.setObjectName(u"plainTextEdit_meaning")
        self.plainTextEdit_meaning.setGeometry(QRect(100, 160, 591, 141))
        self.plainTextEdit_examples = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_examples.setObjectName(u"plainTextEdit_examples")
        self.plainTextEdit_examples.setGeometry(QRect(100, 360, 591, 161))
        self.button_copy_grammar = QPushButton(self.centralwidget)
        self.button_copy_grammar.setObjectName(u"button_copy_grammar")
        self.button_copy_grammar.setGeometry(QRect(700, 90, 80, 24))
        self.button_copy_meaning = QPushButton(self.centralwidget)
        self.button_copy_meaning.setObjectName(u"button_copy_meaning")
        self.button_copy_meaning.setGeometry(QRect(700, 160, 80, 24))
        self.button_copy_example = QPushButton(self.centralwidget)
        self.button_copy_example.setObjectName(u"button_copy_example")
        self.button_copy_example.setGeometry(QRect(700, 360, 80, 24))
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
        self.button_process.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.lineEdit_vocabulary.setText(QCoreApplication.translate("MainWindow", u"Buch", None))
        self.label_vocab.setText(QCoreApplication.translate("MainWindow", u"Vokabular", None))
        self.label_grammar.setText(QCoreApplication.translate("MainWindow", u"Grammatik", None))
        self.label_meaning.setText(QCoreApplication.translate("MainWindow", u"Bedeutung", None))
        self.label_examples.setText(QCoreApplication.translate("MainWindow", u"Beispiele", None))
        self.button_copy_grammar.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.button_copy_meaning.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.button_copy_example.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
    # retranslateUi

