#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog, QFrame, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox, QApplication
from PyQt5.QtCore import Qt
from base import Header


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__()
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('登录')
        self.setObjectName('LoginDialog')
        self.resize(520, 300)

        self.header = Header('登录', self)
        self.header.setMinimumHeight(40)
        self.header.closeButton.clicked.connect(self.close)

        self.usernameLine = QLineEdit()
        self.usernameLine.setObjectName('usernameLine')
        self.usernameLine.setFixedSize(200, 32)
        self.usernameLine.setPlaceholderText("请输入用户名")
        self.signupLabel = QLabel("注册帐号")
        self.signupLabel.setObjectName('signupLabel')
        self.userLayout = QHBoxLayout()
        self.userLayout.addStretch(1)
        self.userLayout.addWidget(self.usernameLine)
        self.userLayout.addSpacing(10)
        self.userLayout.addWidget(self.signupLabel)
        self.userLayout.addStretch(1)

        self.passwordLine = QLineEdit()
        self.passwordLine.setObjectName('passwordLine')
        self.passwordLine.setFixedSize(200, 32)
        self.passwordLine.setPlaceholderText("请输入密码")
        self.findpwLabel = QLabel("找回密码")
        self.findpwLabel.setObjectName('findpwLabel')
        self.passwordLayout = QHBoxLayout()
        self.passwordLayout.addStretch(1)
        self.passwordLayout.addWidget(self.passwordLine)
        self.passwordLayout.addSpacing(10)
        self.passwordLayout.addWidget(self.findpwLabel)
        self.passwordLayout.addStretch(1)

        self.remindPW = QCheckBox("记住密码")
        self.remindPW.setObjectName('remindPW')
        self.autoLogin = QCheckBox("自动登录")
        self.autoLogin.setObjectName('autoLogin')
        self.checkboxLayout = QHBoxLayout()
        self.checkboxLayout.addSpacing(127)
        self.checkboxLayout.addWidget(self.remindPW)
        self.checkboxLayout.addSpacing(58)
        self.checkboxLayout.addWidget(self.autoLogin)
        self.checkboxLayout.addStretch(1)

        self.loginButton = QPushButton("登录")
        self.loginButton.setObjectName('loginButton')
        self.loginButton.setFixedSize(200, 27)
        self.loginbtnLayout = QHBoxLayout()
        self.loginbtnLayout.addSpacing(127)
        self.loginbtnLayout.addWidget(self.loginButton)
        self.loginbtnLayout.addStretch(1)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.header)
        self.mainLayout.addStretch(1)
        self.mainLayout.addLayout(self.userLayout)
        self.mainLayout.addLayout(self.passwordLayout)
        self.mainLayout.addLayout(self.checkboxLayout)
        self.mainLayout.addLayout(self.loginbtnLayout)
        self.mainLayout.addStretch(1)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = LoginDialog()
    widget.show()
    app.exec_()  # 解决dialog一闪而过的问题
