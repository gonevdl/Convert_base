# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, \
    QComboBox, QVBoxLayout, QHBoxLayout, QLabel, QFormLayout, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
import emoji


class Convert(QWidget):
    def __init__(self):
        super(Convert, self).__init__()

        self.setUi()

    def setUi(self):

        self.setFont(QFont('kaiti'))
        self.setWindowTitle("进制计算器" + emoji.emojize(':kissing_closed_eyes:', use_aliases=True))
        self.setFixedSize(1100, 150)
        self.setWindowIcon(QIcon("./src/Developer Folder.ico"))
        self.setFont(QFont("楷体"))

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit1.setAlignment(Qt.AlignRight)
        self.lineEdit2.setAlignment(Qt.AlignRight)
        self.lineEdit1.setFixedSize(720, 40)
        self.lineEdit2.setFixedSize(720, 40)
        # self.lineEdit2.setReadOnly(True)
        print(self.lineEdit1.size())

        self.lineEdit1.setFocusPolicy(Qt.StrongFocus)
        # self.lineEdit1.keyPressEvent(QKeyEvent)

        self.label1 = QLabel("输入" + emoji.emojize(':sleeping:', use_aliases=True))
        self.label2 = QLabel("输出" + emoji.emojize(':grimacing:', use_aliases=True))

        self.btn1 = QComboBox()
        self.btn2 = QComboBox()
        self.btn1.addItems(['2进制', '8进制', '10进制', '16进制', '其他进制'])
        # self.btn1.addItems(
        #     ['2进制' + emoji.emojize(':stuck_out_tongue_winking_eye:', use_aliases=True),
        #      '8进制' + emoji.emojize(':stuck_out_tongue_closed_eyes:', use_aliases=True),
        #      '10进制' + emoji.emojize(':wink:', use_aliases=True),
        #      '16进制' + emoji.emojize(':satisfied:', use_aliases=True),
        #      '其他进制' + emoji.emojize(':unamused:', use_aliases=True)])
        self.btn2.addItems(['2进制', '8进制', '10进制', '16进制', '其他进制'])
        # self.btn2.addItems(
        #     ['2进制' + emoji.emojize(':stuck_out_tongue_winking_eye:', use_aliases=True),
        #      '8进制' + emoji.emojize(':stuck_out_tongue_closed_eyes:', use_aliases=True),
        #      '10进制' + emoji.emojize(':wink:', use_aliases=True),
        #      '16进制' + emoji.emojize(':satisfied:', use_aliases=True),
        #      '其他进制' + emoji.emojize(':unamused:', use_aliases=True)])
        self.btn1.setFixedHeight(40)
        self.btn2.setFixedHeight(40)
        self.btn1.setEditable(True)
        self.btn2.setEditable(True)

        print(self.btn2.size())

        formlayout = QFormLayout()
        formlayout.addRow(self.label1, self.lineEdit1)
        formlayout.addRow(self.label2, self.lineEdit2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        hbox = QHBoxLayout()
        hbox.addLayout(formlayout)
        hbox.addLayout(vbox)
        hbox.setAlignment(Qt.AlignBottom)

        self.setLayout(hbox)

        self.btn1.currentIndexChanged.connect(lambda: self.change(self.btn1))
        self.btn2.currentIndexChanged.connect(lambda: self.change(self.btn2))

    def change(self, btn):
        print(btn.currentText())
        if btn.currentText() == '其他进制':
            num, ok = QInputDialog.getInt(self, "输入", "请输入一个整数" + emoji.emojize(':unamused:', use_aliases=True))
            if ok:
                btn.setCurrentText(str(num) + '进制')
                # self.lineEdit2.setText("结果")
                print(btn.currentText())
                print(num)
            else:
                btn.setCurrentText("2进制")

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Enter) or (event.key() == Qt.Key_Return):
            # self.label2.setText("结果")
            result = self.cal(self.lineEdit1.text())
            self.lineEdit2.setText(result)

    def cal(self, text):
        try:
            src = self.btn1.currentText()
            des = self.btn2.currentText()

            def bit(s: str):
                num = ''
                for ch in s:
                    if '0' <= ch <= '9':
                        num += ch
                    else:
                        return int(num)

            src_num = bit(src)
            des_num = bit(des)

            def con(n, x):
                # n为待转换的十进制数，x为机制，取值为2-16
                a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
                b = []
                while True:
                    s = n // x  # 商
                    y = n % x  # 余数
                    b = b + [y]
                    if s == 0:
                        break
                    n = s
                b.reverse()
                result = ''
                for i in b:
                    result += str(a[i])
                return result

            temp_10 = int(self.lineEdit1.text(), src_num)
            result = str(con(int(temp_10), des_num))
            return result
        except Exception as err:
            QMessageBox.setFont(self, QFont('楷体'))
            QMessageBox.warning(self, "错误", '输入的表达式错误' + emoji.emojize(':scream:', use_aliases=True) +
                                '，请重新输入！', QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cvrt = Convert()
    cvrt.show()
    sys.exit(app.exec_())
