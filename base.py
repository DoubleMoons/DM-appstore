#! /usr/bin/ python3
# -*- coding: utf-8 -*-

# base.py主要设置一些需要重复使用并且在多个文件中均被使用到的控件

from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout, QScrollArea
from PyQt5.QtCore import pyqtSignal


# 是子窗口的标题栏
class Header(QFrame):
    myStyle = """
    QFrame {background: #2D2D2D;}

    QLabel {
        margin-left: 8px;
        color: white;
        font-weight: bold;
        font-size: 15px;
    }

    QPushButton {
        border: none;
        font: bold;
        font-size: 13px;
        color: #7C7C7C;
        margin-right: 8px;
    }

    QPushButton:hover{
        color: #DCDDE4;
    }
    """

    def __init__(self, title: str, parent=None):
        super(Header, self).__init__()
        self.parent = None
        self.setStyleSheet(self.myStyle)

        self.title = QLabel(title)
        self.closeButton = QPushButton('×')
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.addWidget(self.title)
        self.mainLayout.addStretch(1)
        self.mainLayout.addWidget(self.closeButton)


# 滚动区域，并设置scroll滑到底部的信号
class ScrollArea(QScrollArea):
    scrollDown = pyqtSignal()

    def __init__(self, parent=None):
        super(ScrollArea, self).__init__()
        self.parent = parent
        self.frame = QFrame()
        self.frame.setObjectName('frame')
        self.verticalScrollBar().valueChanged.connect(self.sliderPostionEvent)
        self.setWidgetResizable(True)
        self.setWidget(self.frame)

    def sliderPostionEvent(self):
        if self.verticalScrollBar().value() == self.verticalScrollBar().maximum():
            self.scrollDown.emit()

