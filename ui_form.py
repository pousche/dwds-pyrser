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
        MainWindow.resize(800, 800)
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

        self.vocab_button_copy = QPushButton(self.centralwidget)
        self.vocab_button_copy.setObjectName(u"vocab_button_copy")

        self.vocab_layout.addWidget(self.vocab_button_copy)


        self.verticalLayout.addLayout(self.vocab_layout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout_grammar = QGridLayout(self.layoutWidget)
        self.gridLayout_grammar.setObjectName(u"gridLayout_grammar")
        self.gridLayout_grammar.setContentsMargins(0, 0, 0, 0)
        self.grammar_button_copy = QPushButton(self.layoutWidget)
        self.grammar_button_copy.setObjectName(u"grammar_button_copy")

        self.gridLayout_grammar.addWidget(self.grammar_button_copy, 0, 2, 1, 1)

        self.grammar_label = QLabel(self.layoutWidget)
        self.grammar_label.setObjectName(u"grammar_label")

        self.gridLayout_grammar.addWidget(self.grammar_label, 0, 0, 1, 1)

        self.grammar_spacer_label = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_grammar.addItem(self.grammar_spacer_label, 1, 0, 1, 1)

        self.grammar_spacer_copy = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_grammar.addItem(self.grammar_spacer_copy, 1, 2, 1, 1)

        self.grammar_plainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.grammar_plainTextEdit.setObjectName(u"grammar_plainTextEdit")

        self.gridLayout_grammar.addWidget(self.grammar_plainTextEdit, 0, 1, 2, 1)

        self.gridLayout_grammar.setColumnStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.gridLayout_meaning = QGridLayout(self.layoutWidget1)
        self.gridLayout_meaning.setObjectName(u"gridLayout_meaning")
        self.gridLayout_meaning.setContentsMargins(0, 0, 0, 0)
        self.meaning_label = QLabel(self.layoutWidget1)
        self.meaning_label.setObjectName(u"meaning_label")

        self.gridLayout_meaning.addWidget(self.meaning_label, 0, 0, 1, 1)

        self.meaning_button_copy = QPushButton(self.layoutWidget1)
        self.meaning_button_copy.setObjectName(u"meaning_button_copy")

        self.gridLayout_meaning.addWidget(self.meaning_button_copy, 0, 2, 1, 1)

        self.meaning_spacer_label = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_meaning.addItem(self.meaning_spacer_label, 1, 0, 1, 1)

        self.meaning_spacer_copy = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_meaning.addItem(self.meaning_spacer_copy, 1, 2, 1, 1)

        self.meaning_plainTextEdit = QPlainTextEdit(self.layoutWidget1)
        self.meaning_plainTextEdit.setObjectName(u"meaning_plainTextEdit")

        self.gridLayout_meaning.addWidget(self.meaning_plainTextEdit, 0, 1, 2, 1)

        self.gridLayout_meaning.setColumnStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.gridLayout_examples = QGridLayout(self.layoutWidget2)
        self.gridLayout_examples.setObjectName(u"gridLayout_examples")
        self.gridLayout_examples.setContentsMargins(0, 0, 0, 0)
        self.examples_label = QLabel(self.layoutWidget2)
        self.examples_label.setObjectName(u"examples_label")

        self.gridLayout_examples.addWidget(self.examples_label, 0, 0, 1, 1)

        self.examples_slider = QSlider(self.layoutWidget2)
        self.examples_slider.setObjectName(u"examples_slider")
        self.examples_slider.setMinimum(1)
        self.examples_slider.setMaximum(5)
        self.examples_slider.setValue(2)
        self.examples_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_examples.addWidget(self.examples_slider, 1, 2, 1, 1)

        self.examples_plainTextEdit = QPlainTextEdit(self.layoutWidget2)
        self.examples_plainTextEdit.setObjectName(u"examples_plainTextEdit")

        self.gridLayout_examples.addWidget(self.examples_plainTextEdit, 0, 1, 5, 1)

        self.examples_button_copy = QPushButton(self.layoutWidget2)
        self.examples_button_copy.setObjectName(u"examples_button_copy")

        self.gridLayout_examples.addWidget(self.examples_button_copy, 0, 2, 1, 1)

        self.examples_spacer_copy = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_examples.addItem(self.examples_spacer_copy, 4, 2, 1, 1)

        self.examples_spacer_label = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_examples.addItem(self.examples_spacer_label, 1, 0, 4, 1)

        self.examples_label_count = QLabel(self.layoutWidget2)
        self.examples_label_count.setObjectName(u"examples_label_count")

        self.gridLayout_examples.addWidget(self.examples_label_count, 2, 2, 1, 1)

        self.gridLayout_examples.setColumnStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget2)
        self.layoutWidget3 = QWidget(self.splitter)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.gridLayout_thesaurus = QGridLayout(self.layoutWidget3)
        self.gridLayout_thesaurus.setObjectName(u"gridLayout_thesaurus")
        self.gridLayout_thesaurus.setContentsMargins(0, 0, 0, 0)
        self.thesaurus_label = QLabel(self.layoutWidget3)
        self.thesaurus_label.setObjectName(u"thesaurus_label")

        self.gridLayout_thesaurus.addWidget(self.thesaurus_label, 0, 0, 1, 1)

        self.thesaurus_button_copy = QPushButton(self.layoutWidget3)
        self.thesaurus_button_copy.setObjectName(u"thesaurus_button_copy")

        self.gridLayout_thesaurus.addWidget(self.thesaurus_button_copy, 0, 2, 1, 1)

        self.thesaurus_spacer_copy = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_thesaurus.addItem(self.thesaurus_spacer_copy, 1, 2, 1, 1)

        self.thesaurus_spacer_label = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_thesaurus.addItem(self.thesaurus_spacer_label, 1, 0, 1, 1)

        self.thesaurus_plainTextEdit = QPlainTextEdit(self.layoutWidget3)
        self.thesaurus_plainTextEdit.setObjectName(u"thesaurus_plainTextEdit")

        self.gridLayout_thesaurus.addWidget(self.thesaurus_plainTextEdit, 0, 1, 3, 1)

        self.splitter.addWidget(self.layoutWidget3)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout_tag = QHBoxLayout()
        self.horizontalLayout_tag.setObjectName(u"horizontalLayout_tag")
        self.tag_label = QLabel(self.centralwidget)
        self.tag_label.setObjectName(u"tag_label")

        self.horizontalLayout_tag.addWidget(self.tag_label)

        self.tag_lineEdit = QLineEdit(self.centralwidget)
        self.tag_lineEdit.setObjectName(u"tag_lineEdit")

        self.horizontalLayout_tag.addWidget(self.tag_lineEdit)

        self.tag_button_copy = QPushButton(self.centralwidget)
        self.tag_button_copy.setObjectName(u"tag_button_copy")

        self.horizontalLayout_tag.addWidget(self.tag_button_copy)


        self.verticalLayout.addLayout(self.horizontalLayout_tag)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DWDS Parser", None))
        self.vocab_label.setText(QCoreApplication.translate("MainWindow", u"Vokabular", None))
        self.vocab_lineEdit.setText(QCoreApplication.translate("MainWindow", u"Buch", None))
        self.vocab_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.grammar_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.grammar_label.setText(QCoreApplication.translate("MainWindow", u"Grammatik", None))
        self.grammar_plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"-", None))
        self.meaning_label.setText(QCoreApplication.translate("MainWindow", u"Bedeutung", None))
        self.meaning_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.meaning_plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"-", None))
        self.examples_label.setText(QCoreApplication.translate("MainWindow", u"Beispiele", None))
        self.examples_plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"-", None))
        self.examples_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.examples_label_count.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.thesaurus_label.setText(QCoreApplication.translate("MainWindow", u"Verwandte", None))
        self.thesaurus_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.thesaurus_plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tag_label.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
        self.tag_lineEdit.setText("")
        self.tag_button_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
    # retranslateUi

