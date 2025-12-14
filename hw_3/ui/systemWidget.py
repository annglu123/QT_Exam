# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'systemWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber, QLabel,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelDelay = QLabel(Form)
        self.labelDelay.setObjectName(u"labelDelay")

        self.gridLayout.addWidget(self.labelDelay, 0, 0, 1, 1)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)

        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)

        self.labelCPU = QLabel(Form)
        self.labelCPU.setObjectName(u"labelCPU")

        self.gridLayout.addWidget(self.labelCPU, 1, 0, 1, 1)

        self.lcdNumberCPU = QLCDNumber(Form)
        self.lcdNumberCPU.setObjectName(u"lcdNumberCPU")

        self.gridLayout.addWidget(self.lcdNumberCPU, 1, 1, 1, 1)

        self.labelRAM = QLabel(Form)
        self.labelRAM.setObjectName(u"labelRAM")

        self.gridLayout.addWidget(self.labelRAM, 2, 0, 1, 1)

        self.lcdNumberRAM = QLCDNumber(Form)
        self.lcdNumberRAM.setObjectName(u"lcdNumberRAM")

        self.gridLayout.addWidget(self.lcdNumberRAM, 2, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelDelay.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.labelCPU.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.labelRAM.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM", None))
    # retranslateUi

