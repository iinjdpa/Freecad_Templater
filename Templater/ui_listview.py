# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(407, 240)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout.addWidget(self.listView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_create = QPushButton(Dialog)
        self.pushButton_create.setObjectName(u"pushButton_create")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_create.sizePolicy().hasHeightForWidth())
        self.pushButton_create.setSizePolicy(sizePolicy)
        self.pushButton_create.setMinimumSize(QSize(93, 28))
        self.pushButton_create.setMaximumSize(QSize(93, 28))

        self.verticalLayout.addWidget(self.pushButton_create)

        self.pushButton_edit = QPushButton(Dialog)
        self.pushButton_edit.setObjectName(u"pushButton_edit")
        sizePolicy.setHeightForWidth(self.pushButton_edit.sizePolicy().hasHeightForWidth())
        self.pushButton_edit.setSizePolicy(sizePolicy)
        self.pushButton_edit.setMinimumSize(QSize(93, 28))
        self.pushButton_edit.setMaximumSize(QSize(93, 28))

        self.verticalLayout.addWidget(self.pushButton_edit)

        self.pushButton_delete = QPushButton(Dialog)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setMinimumSize(QSize(93, 28))
        self.pushButton_delete.setMaximumSize(QSize(93, 28))

        self.verticalLayout.addWidget(self.pushButton_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        sizePolicy.setHeightForWidth(self.pushButton_ok.sizePolicy().hasHeightForWidth())
        self.pushButton_ok.setSizePolicy(sizePolicy)
        self.pushButton_ok.setMinimumSize(QSize(93, 28))
        self.pushButton_ok.setMaximumSize(QSize(93, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_ok)

        self.pushButton_cancelar = QPushButton(Dialog)
        self.pushButton_cancelar.setObjectName(u"pushButton_cancelar")
        sizePolicy.setHeightForWidth(self.pushButton_cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_cancelar.setSizePolicy(sizePolicy)
        self.pushButton_cancelar.setMinimumSize(QSize(93, 28))
        self.pushButton_cancelar.setMaximumSize(QSize(93, 28))

        self.horizontalLayout_2.addWidget(self.pushButton_cancelar)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        QWidget.setTabOrder(self.pushButton_cancelar, self.pushButton_ok)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Template creator", None))
        self.pushButton_create.setText(QCoreApplication.translate("Dialog", u"Create", None))
        self.pushButton_edit.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"Load", None))
        self.pushButton_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

