from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(427, 346)
        Form.setMinimumSize(QtCore.QSize(427, 0))
        Form.setMaximumSize(QtCore.QSize(427, 346))
        Form.setStyleSheet("background-color: rgb(255, 240, 224);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(12, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(290, 70))
        font = QtGui.QFont()
        font.setFamily("Rostov")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setPixmap(QtGui.QPixmap("../лого.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setMaximumSize(QtCore.QSize(80, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/logo_mini.PNG"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setOpenExternalLinks(False)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(43)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(430, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(56, 24))
        self.label_2.setMaximumSize(QtCore.QSize(0, 24))
        self.label_2.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.edit_login = QtWidgets.QLineEdit(Form)
        self.edit_login.setStyleSheet("background-color: rgb(255, 255, 255); \n"
"border-top: 1px solid #3e3e3e;\n"
"border-left: 1px solid #3e3e3e;\n"
"border-right: 1px solid #3e3e3e;\n"
"border-bottom: 1px solid #3e3e3e;")
        self.edit_login.setObjectName("edit_login")
        self.horizontalLayout.addWidget(self.edit_login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.edit_password = QtWidgets.QLineEdit(Form)
        self.edit_password.setStyleSheet("background-color: rgb(255, 255, 255); \n"
"border-top: 1px solid #3e3e3e;\n"
"border-left: 1px solid #3e3e3e;\n"
"border-right: 1px solid #3e3e3e;\n"
"border-bottom: 1px solid #3e3e3e;")
        self.edit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.horizontalLayout_2.addWidget(self.edit_password)
        self.btn_hide_password = QtWidgets.QPushButton(Form)
        self.btn_hide_password.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_hide_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_hide_password.setStyleSheet("background-color: rgb(143, 0, 2);\n"
"font: 9pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.btn_hide_password.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/eye2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hide_password.setIcon(icon)
        self.btn_hide_password.setAutoRepeat(False)
        self.btn_hide_password.setObjectName("btn_hide_password")
        self.horizontalLayout_2.addWidget(self.btn_hide_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.edit_captcha = QtWidgets.QLineEdit(Form)
        self.edit_captcha.setStyleSheet("background-color: rgb(255, 255, 255); \n"
"border-top: 1px solid #3e3e3e;\n"
"border-left: 1px solid #3e3e3e;\n"
"border-right: 1px solid #3e3e3e;\n"
"border-bottom: 1px solid #3e3e3e;")
        self.edit_captcha.setObjectName("edit_captcha")
        self.horizontalLayout_4.addWidget(self.edit_captcha)
        self.btn_new_captcha = QtWidgets.QPushButton(Form)
        self.btn_new_captcha.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_new_captcha.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_new_captcha.setStyleSheet("background-color: rgb(143, 0, 2);\n"
"font: 9pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.btn_new_captcha.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new_captcha.setIcon(icon1)
        self.btn_new_captcha.setObjectName("btn_new_captcha")
        self.horizontalLayout_4.addWidget(self.btn_new_captcha)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.captcha = QtWidgets.QLabel(Form)
        self.captcha.setMinimumSize(QtCore.QSize(407, 67))
        self.captcha.setMaximumSize(QtCore.QSize(407, 67))
        self.captcha.setFrameShape(QtWidgets.QFrame.Box)
        self.captcha.setScaledContents(True)
        self.captcha.setAlignment(QtCore.Qt.AlignCenter)
        self.captcha.setObjectName("captcha")
        self.verticalLayout.addWidget(self.captcha)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.btn_enter = QtWidgets.QPushButton(Form)
        self.btn_enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enter.setStyleSheet("background-color: rgb(143, 0, 2);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.btn_enter.setObjectName("btn_enter")
        self.verticalLayout.addWidget(self.btn_enter)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(7, 10)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Авторизация"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.label_2.setText(_translate("Form", " Логин: "))
        self.label_3.setText(_translate("Form", " Пароль: "))
        self.label_4.setText(_translate("Form", " Введите капчу: "))
        self.captcha.setText(_translate("Form", "капча"))
        self.btn_enter.setText(_translate("Form", "Войти"))
