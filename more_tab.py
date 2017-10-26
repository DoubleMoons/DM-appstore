#! /usr/bin/ python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout


class MoreTab(QWidget):
    def __init__(self, parent=None):
        super(MoreTab, self).__init__()
        self.setObjectName('UninstallTab')
        self.parent = parent

        self.label = QLabel("MoreTab")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MoreTab()
    widget.show()
    app.exec_(sys.exit())
