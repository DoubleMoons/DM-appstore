#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox, QGroupBox, QFrame, QTabWidget, QWidget, QLabel, QLineEdit, QRadioButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from base import Header


class GeneralTab(QWidget):
    myStyle = """
    QGroupBox {
        border: 1px solid gray;
        border-radius: 3px;
        margin-top: 0.5em;
    }
    QGroupBox::title{
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
    }
    """

    def __init__(self, parent=None):
        super(GeneralTab, self).__init__()
        self.parent = parent
        self.setStyleSheet(self.myStyle)
        self.updateCheckerSetting()
        self.downloadCloseSetting()
        self.setLayouts()

    def updateCheckerSetting(self):
        self.updateChecker = QGroupBox('自动检查更新')

        self.openUpdateRadio = QRadioButton('打开软件时检查更新')
        self.weeklyUpdateRadio = QRadioButton('每周一次检查更新')
        self.neverUpdateRadio = QRadioButton('从不检查更新')

        self.checkerRadioLayout = QHBoxLayout()
        self.checkerRadioLayout.addWidget(self.openUpdateRadio)
        self.checkerRadioLayout.addWidget(self.weeklyUpdateRadio)
        self.checkerRadioLayout.addWidget(self.neverUpdateRadio)

        self.updateChecker.setLayout(self.checkerRadioLayout)

    def downloadCloseSetting(self):
        self.downloadClose = QGroupBox('下载中关闭软件中心')

        self.continueRadio = QRadioButton('继续下载，并最小化至托盘')
        self.stopRadio = QRadioButton('停止下载， 并退出软件中心')
        self.askRadio = QRadioButton('每次询问')

        self.downloadCloseLayout = QHBoxLayout()
        self.downloadCloseLayout.addWidget(self.continueRadio)
        self.downloadCloseLayout.addWidget(self.stopRadio)
        self.downloadCloseLayout.addWidget(self.askRadio)

        self.downloadClose.setLayout(self.downloadCloseLayout)

    def setLayouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.updateChecker)
        self.mainLayout.addWidget(self.downloadClose)

        self.setLayout(self.mainLayout)


class DownloadTab(QWidget):
    myStyle = """
    QGroupBox {
        border: 1px solid gray;
        border-radius: 3px;
        margin-top: 0.5em;
    }
    QGroupBox::title{
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
    }
    """

    def __init__(self, parent=None):
        super(DownloadTab, self).__init__()
        self.parent = parent
        self.setStyleSheet(self.myStyle)
        self.downloadFolderSetting()
        self.downloadCleanSetting()
        self.setLayouts()

    def downloadFolderSetting(self):
        self.downloadFolder = QGroupBox('下载目录')

        self.folderLabel = QLabel('下载目录')
        self.openFolder = QLabel('打开目录')
        self.labelLayout = QHBoxLayout()
        self.labelLayout.addWidget(self.folderLabel)
        self.labelLayout.addWidget(self.openFolder)

        self.showcurrentFolder = QLineEdit()
        self.showcurrentFolder.setPlaceholderText('/home/.DM-appstore/download')
        self.chooseButton = QPushButton('选择目录')
        self.restoreButton = QPushButton('恢复默认目录')
        self.changeFolderLayout = QHBoxLayout()
        self.changeFolderLayout.addWidget(self.showcurrentFolder)
        self.changeFolderLayout.addWidget(self.chooseButton)
        self.changeFolderLayout.addWidget(self.restoreButton)

        self.downloadFolderLayout = QVBoxLayout()
        self.downloadFolderLayout.addLayout(self.labelLayout)
        self.downloadFolderLayout.addLayout(self.changeFolderLayout)

        self.downloadFolder.setLayout(self.downloadFolderLayout)

    def downloadCleanSetting(self):
        self.downloadClean = QGroupBox('安装包清理')

        self.autoCleanLabel = QLabel('自动清理安装包')
        self.manualCleanLabel = QLabel('手动清理')
        self.labelLayout = QHBoxLayout()
        self.labelLayout.addWidget(self.autoCleanLabel)
        self.labelLayout.addWidget(self.manualCleanLabel)

        self.weeklyRadio = QRadioButton('下载一周后自动清理')
        self.installedRadio = QRadioButton('安装完成后自动清理')
        self.neverRadio = QRadioButton('不自动清理')
        self.radioLayout = QHBoxLayout()
        self.radioLayout.addWidget(self.weeklyRadio)
        self.radioLayout.addWidget(self.installedRadio)
        self.radioLayout.addWidget(self.neverRadio)

        self.downloadCleanLayout = QVBoxLayout()
        self.downloadCleanLayout.addLayout(self.labelLayout)
        self.downloadCleanLayout.addLayout(self.radioLayout)

        self.downloadClean.setLayout(self.downloadCleanLayout)

    def setLayouts(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.downloadFolder)
        self.mainLayout.addWidget(self.downloadClean)

        self.setLayout(self.mainLayout)


class SettingDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingDialog, self).__init__()
        self.setObjectName('SettingDialog')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon('resource/format.ico'))
        self.setWindowTitle('设置')
        self.resize(520, 400)

        self.header = Header('设置', self)
        self.header.setMaximumHeight(40)
        self.header.closeButton.clicked.connect(self.close)

        self.settingContents = QTabWidget(self)
        self.generalTab = GeneralTab()
        self.downloadTab = DownloadTab()

        self.settingContents.addTab(self.generalTab, "常规设置")
        self.settingContents.addTab(self.downloadTab, "下载设置")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.header)
        self.mainLayout.addWidget(self.settingContents)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SettingDialog()
    widget.show()
    app.exec_()
