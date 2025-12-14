# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_shop.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 346)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(Form)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout.addWidget(self.listWidget)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(170, 0, 0)")

        self.verticalLayout.addWidget(self.label_3)

        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setToolTipDuration(-1)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043d\u0438\u0433\u0443", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u0413\u0430\u0440\u0440\u0438 \u041f\u043e\u0442\u0442\u0435\u0440 \u0438 \u0443\u0437\u043d\u0438\u043a \u0410\u0437\u043a\u0430\u0431\u0430\u043d\u0430 \u0414\u0436\u043e\u0430\u043d \u0420\u043e\u0443\u043b\u0438\u043d\u0433", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0435\u0437\u043d\u044b\u0439 \u043a\u043e\u0440\u043e\u043b\u044c. \u041c\u043e\u0440\u0438\u0441 \u0414\u0440\u044e\u043e\u043d", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"\u0425\u043e\u0431\u0431\u0438\u0442. \u0414\u0436\u043e\u043d \u0420.\u0420. \u0422\u043e\u043b\u043a\u0438\u043d", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e QR", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u043c\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u043b\u0430\u0442\u0438\u0442\u044c", None))
    # retranslateUi

