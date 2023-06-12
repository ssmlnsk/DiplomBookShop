from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(665, 600)
        Dialog.setStyleSheet("background-color: rgb(255, 240, 224);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(12, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 70))
        self.label.setMaximumSize(QtCore.QSize(300, 70))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../лого.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setMaximumSize(QtCore.QSize(80, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/logo_mini.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.edit_surname = QtWidgets.QLineEdit(Dialog)
        self.edit_surname.setStyleSheet("background-color: rgb(255, 255, 255); \n"
"border-top: 1px solid #3e3e3e;\n"
"border-left: 1px solid #3e3e3e;\n"
"border-right: 1px solid #3e3e3e;\n"
"border-bottom: 1px solid #3e3e3e;")
        self.edit_surname.setObjectName("edit_surname")
        self.horizontalLayout_4.addWidget(self.edit_surname)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_20.addWidget(self.label_3)
        self.edit_name = QtWidgets.QLineEdit(Dialog)
        self.edit_name.setStyleSheet("background-color: rgb(255, 255, 255); \n"
"border-top: 1px solid #3e3e3e;\n"
"border-left: 1px solid #3e3e3e;\n"
"border-right: 1px solid #3e3e3e;\n"
"border-bottom: 1px solid #3e3e3e;")
        self.edit_name.setObjectName("edit_name")
        self.horizontalLayout_20.addWidget(self.edit_name)
        self.horizontalLayout_20.setStretch(1, 100)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_19.addWidget(self.label_18)
        self.edit_lastname = QtWidgets.QLineEdit(Dialog)
        self.edit_lastname.setStyleSheet("background-color: rgb(255, 255, 255); \n"
"border-top: 1px solid #3e3e3e;\n"
"border-left: 1px solid #3e3e3e;\n"
"border-right: 1px solid #3e3e3e;\n"
"border-bottom: 1px solid #3e3e3e;")
        self.edit_lastname.setObjectName("edit_lastname")
        self.horizontalLayout_19.addWidget(self.edit_lastname)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.date_birth = QtWidgets.QDateEdit(Dialog)
        self.date_birth.setStyleSheet("background-color: rgb(255, 255, 255); ")
        self.date_birth.setObjectName("date_birth")
        self.horizontalLayout_5.addWidget(self.date_birth)
        self.horizontalLayout_5.setStretch(1, 100)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.edit_email = QtWidgets.QLineEdit(Dialog)
        self.edit_email.setStyleSheet("background-color: rgb(255, 255, 255); \n"
"border-top: 1px solid #3e3e3e;\n"
"border-left: 1px solid #3e3e3e;\n"
"border-right: 1px solid #3e3e3e;\n"
"border-bottom: 1px solid #3e3e3e;")
        self.edit_email.setObjectName("edit_email")
        self.horizontalLayout.addWidget(self.edit_email)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_add_client = QtWidgets.QPushButton(Dialog)
        self.btn_add_client.setStyleSheet("background-color: rgb(143, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.btn_add_client.setObjectName("btn_add_client")
        self.horizontalLayout_3.addWidget(self.btn_add_client)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Добавить нового клиента"))
        self.label_5.setText(_translate("Dialog", "Введите фамилию:"))
        self.label_3.setText(_translate("Dialog", "Введите имя:"))
        self.label_18.setText(_translate("Dialog", "Введите отчество:"))
        self.label_7.setText(_translate("Dialog", "Введите дату рождения:"))
        self.label_4.setText(_translate("Dialog", "Введите e-mail:"))
        self.btn_add_client.setText(_translate("Dialog", "Добавить нового клиента"))
