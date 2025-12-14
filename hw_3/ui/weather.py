# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLatitude = QLabel(Form)
        self.labelLatitude.setObjectName(u"labelLatitude")

        self.horizontalLayout.addWidget(self.labelLatitude)

        self.doubleSpinBoxLatitude = QDoubleSpinBox(Form)
        self.doubleSpinBoxLatitude.setObjectName(u"doubleSpinBoxLatitude")
        self.doubleSpinBoxLatitude.setMinimum(-90.000000000000000)
        self.doubleSpinBoxLatitude.setMaximum(90.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBoxLatitude)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelLongitude = QLabel(Form)
        self.labelLongitude.setObjectName(u"labelLongitude")

        self.horizontalLayout_2.addWidget(self.labelLongitude)

        self.doubleSpinBoxLongitude = QDoubleSpinBox(Form)
        self.doubleSpinBoxLongitude.setObjectName(u"doubleSpinBoxLongitude")
        self.doubleSpinBoxLongitude.setMinimum(-180.000000000000000)
        self.doubleSpinBoxLongitude.setMaximum(180.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBoxLongitude)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelDelay = QLabel(Form)
        self.labelDelay.setObjectName(u"labelDelay")

        self.horizontalLayout_3.addWidget(self.labelDelay)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(3)

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelLatitude.setText(QCoreApplication.translate("Form", u"\u0428\u0438\u0440\u043e\u0442\u0430:", None))
        self.labelLongitude.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430:", None))
        self.labelDelay.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))
    # retranslateUi

