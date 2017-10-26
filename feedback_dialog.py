#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog, QLabel, QTextEdit, QComboBox, QLineEdit, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QFileDialog, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from base import Header


class FeedbackDialog(QDialog):
    def __init__(self, parent=None):
        super(FeedbackDialog, self).__init__()
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('反馈')
        self.resize(600, 450)

        self.header = Header('反馈', self)
        self.header.setFixedHeight(40)
        self.header.closeButton.clicked.connect(self.close)

        self.feedbackImg = QLabel()
        self.feedbackImg.setObjectName('feedbackImg')
        self.pixmap = QPixmap('resource/volume.png')
        self.feedbackImg.setPixmap(self.pixmap)
        self.feedbackImg.setFixedSize(24, 24)

        self.feedbackLabel = QLabel('您有什么问题或建议想要对我们说？')
        self.feedbackLabel.setObjectName('feedbackLabel')

        self.feedbackLayout = QHBoxLayout()
        self.feedbackLayout.addWidget(self.feedbackImg)
        self.feedbackLayout.addWidget(self.feedbackLabel)

        self.feedbackTextedit = QTextEdit()
        self.feedbackTextedit.setPlaceholderText(
                "请详细描述您遇到的问题，例如\n"
                "1. 升级\下载异常，请提供 A:软件名称 B:您所在地\n"
                "2. 网络异常，请检查电脑网络连接是否正常，并尝试刷新\n"
                "3. 卸载异常， 请提供软件名称\n"
                "4. 推荐软件，请提供软件名称及推荐理由\n"
                "5. 产品建议，无论是功能体验问题，还是脑洞大开的idea，欢迎向我们提出建议"
                )

        self.contactLabel = QLabel('联系方式')
        self.contactCombox = QComboBox()
        self.contactCombox.addItem('QQ')
        self.contactCombox.addItem('邮箱')
        self.contactCombox.addItem('github')
        self.contactCombox.addItem('微博')

        self.contactLineedit = QLineEdit()

        self.contactLayout = QHBoxLayout()
        self.contactLayout.addWidget(self.contactLabel)
        self.contactLayout.addWidget(self.contactCombox)
        self.contactLayout.addWidget(self.contactLineedit)

        self.describeLabel = QLabel('请留下您的联系方式，以便我们快速定位问题的原因并及时给您反馈')

        self.submitButton = QPushButton('提交')
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.header)
        self.mainLayout.addLayout(self.feedbackLayout)
        self.mainLayout.addWidget(self.feedbackTextedit)
        self.mainLayout.addLayout(self.contactLayout)
        self.mainLayout.addWidget(self.describeLabel)
        self.mainLayout.addWidget(self.submitButton)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = FeedbackDialog()
    widget.show()
    app.exec_()
