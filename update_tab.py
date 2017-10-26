#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout


class UpdateTab(QWidget):
    def __init__(self, parent=None):
        super(UpdateTab, self).__init__()
        self.setObjectName('UpdateTab')
        self.parent = parent

        self.label = QLabel('UpdateTab')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = UpdateTab()
    widget.show()
    app.exec_(sys.exit())
