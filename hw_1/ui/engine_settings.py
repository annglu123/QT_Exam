# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'engine_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(510, 250)
        Form.setMinimumSize(QSize(510, 250))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSlider = QSlider(self.groupBox)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout.addWidget(self.verticalSlider, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSlider_2 = QSlider(self.groupBox)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_2.addWidget(self.verticalSlider_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSlider_3 = QSlider(self.groupBox)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSlider_4 = QSlider(self.groupBox)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_4.addWidget(self.verticalSlider_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSlider_6 = QSlider(self.groupBox)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_6.addWidget(self.verticalSlider_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
    # retranslateUi

