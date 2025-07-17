# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_mainwindow.ui'
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 10, 80, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 10, 591, 24))
        self.label_vocab = QLabel(self.centralwidget)
        self.label_vocab.setObjectName(u"label_vocab")
        self.label_vocab.setGeometry(QRect(10, 10, 71, 21))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(100, 100, 591, 41))
        self.label_grammar = QLabel(self.centralwidget)
        self.label_grammar.setObjectName(u"label_grammar")
        self.label_grammar.setGeometry(QRect(10, 100, 71, 21))
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(100, 170, 591, 151))
        self.label_meaning = QLabel(self.centralwidget)
        self.label_meaning.setObjectName(u"label_meaning")
        self.label_meaning.setGeometry(QRect(10, 170, 71, 21))
        self.label_examples = QLabel(self.centralwidget)
        self.label_examples.setObjectName(u"label_examples")
        self.label_examples.setGeometry(QRect(10, 340, 71, 21))
        self.plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(100, 340, 591, 191))
        self.slider_example = QSlider(self.centralwidget)
        self.slider_example.setObjectName(u"slider_example")
        self.slider_example.setGeometry(QRect(230, 50, 461, 20))
        self.slider_example.setOrientation(Qt.Orientation.Horizontal)
        self.label_example_count = QLabel(self.centralwidget)
        self.label_example_count.setObjectName(u"label_example_count")
        self.label_example_count.setGeometry(QRect(10, 50, 71, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 50, 101, 24))
        self.lineEdit_2.setReadOnly(True)
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.label_vocab.setText(QCoreApplication.translate("MainWindow", u"Vokabular", None))
        self.label_grammar.setText(QCoreApplication.translate("MainWindow", u"Grammatik", None))
        self.label_meaning.setText(QCoreApplication.translate("MainWindow", u"Bedeutung", None))
        self.label_examples.setText(QCoreApplication.translate("MainWindow", u"Beispiele", None))
        self.label_example_count.setText(QCoreApplication.translate("MainWindow", u"Beispiele", None))
    # retranslateUi

