# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_start.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
import os
import time
import numpy as np
from PIL import Image
from PyQt5.QtWidgets import QMessageBox

import threading
import shutil
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

class Ui_MainWindow(object):
    def easy_face1(self):
        # 调用摄像头摄像头
        cap = cv2.VideoCapture(0)
        while (True):
            # 获取摄像头拍摄到的画面
            ret, frame = cap.read()
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            img = frame
            for (x, y, w, h) in faces:
                # 画出人脸框，蓝色，画笔宽度微
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
                face_area = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(face_area)
                # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
                for (ex, ey, ew, eh) in eyes:
                    # 画出人眼框，绿色，画笔宽度为1
                    cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
            cv2.imshow('frame1', img)
            # 每5毫秒监听一次键盘动作
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyWindow('frame1')

    def easy_face2(self):
        # 调用摄像头摄像头
        cap = cv2.VideoCapture(0)
        while (True):
            # 获取摄像头拍摄到的画面
            ret, frame = cap.read()
            faces = face_cascade.detectMultiScale(frame, 1.3, 2)
            img = frame
            for (x, y, w, h) in faces:
                # 画出人脸框，蓝色，画笔宽度微
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
                face_area = img[y:y + h, x:x + w]

                ## 人眼检测
                # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
                eyes = eye_cascade.detectMultiScale(face_area, 1.3, 10)
                for (ex, ey, ew, eh) in eyes:
                    # 画出人眼框，绿色，画笔宽度为1
                    cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

                ## 微笑检测
                # 用微笑级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
                smiles = smile_cascade.detectMultiScale(face_area, scaleFactor=1.16, minNeighbors=65, minSize=(25, 25),
                                                        flags=cv2.CASCADE_SCALE_IMAGE)
                for (ex, ey, ew, eh) in smiles:
                    # 画出微笑框，红色（BGR色彩体系），画笔宽度为1
                    cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)
                    cv2.putText(img, 'Smile', (x, y - 6), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)

            # 实时展示效果画面
            cv2.imshow('frame2', img)
            # 每5毫秒监听一次键盘动作
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyWindow('frame2')

    def edit_name(self):
        self.name=self.lineEdit.text()
        self.path=os.getcwd()+'\\lian'
        if os.path.exists(self.path):  # 判断lian文件夹是否存在
            for root, dirs, files in os.walk(self.path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))  # 删除文件
                for name in dirs:
                    os.rmdir(os.path.join(root, name))  # 删除文件夹
            os.rmdir(self.path)  # 删除lian文件夹
        os.mkdir(self.path)  # 创建lian文件夹

    def catch_face(self):
        cap = cv2.VideoCapture(0)
        while (True):
            # 获取摄像头拍摄到的画面
            ret, frame = cap.read()
            os.chdir(self.path)  # 进入lian文件夹
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            img = frame
            cv2.imshow('frame3', img)#录入照片的时候弹出的窗口可能会灰屏，这是正常现象
            index = 0
            for (x, y, w, h) in faces:
                # 画出人脸框，蓝色，画笔宽度微
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
                face_area = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(face_area)
                # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
                for (ex, ey, ew, eh) in eyes:
                    # 画出人眼框，绿色，画笔宽度为1
                    cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
                    for index in range(100):
                        img_name = "12.lian.%d.jpg" % (index)
                        print(img_name)
                        image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                        cv2.imwrite(img_name, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                        time.sleep(0.5)
                        ret, frame = cap.read()
                        cv2.imwrite(img_name, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                        index += 1
                        if index==99:
                            return
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
                        # if (c % timeF == 0):这个是视频用的方式
                        # c = c + 1
                        # cv2.waitKey(1)
                        # cv2.imwrite(os.path.join(self.path+img_name), image)
                        # cv2.imwrite(os.path.join(self.path,img_name), image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
        # 最后，关闭所有窗口
        cap.release()
        cv2.destroyWindow('frame3')

    def getImagesAndLabels(self,path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            # 打开图片
            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            # 将图像转换为数组
            img_numpy = np.array(PIL_img, 'uint8')
            # 获取每张图片的id
            # print(os.path.split(imagePath))
            id = int(os.path.split(imagePath)[-1].split(".")[0])
            faces = face_cascade.detectMultiScale(img_numpy)
            for x, y, w, h in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return faceSamples, ids

    def shengcheng(self):
        path = self.path
        faces, ids = self.getImagesAndLabels(path)
        # 获取训练对象
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(ids))  # 要将ids从列表转换为数组
        # 保存模型
        recognizer.write('trainer12.yml')

    def shibie(self):
        self.plainTextEdit.appendPlainText(f'今年见，明年重见。春色如人面。生日快乐,{self.name}，愿你崭新的时光通透温热。')
        cap = cv2.VideoCapture(0)
        os.chdir(self.path)
        recognizer_MAINTAIN = cv2.face.LBPHFaceRecognizer_create()
        recognizer_MAINTAIN.read('trainer12.yml')
        idum_MAINTAIN = 0
        names = [str(self.name)]
        while (True):
            # 获取摄像头拍摄到的画面
            ret, frame = cap.read()
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            img = frame
            for (x, y, w, h) in faces:
                # 画出人脸框，蓝色，画笔宽度微
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
                face_area = gray[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(face_area)
                # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
                for (ex, ey, ew, eh) in eyes:
                    # 画出人眼框，绿色，画笔宽度为1
                    cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)
                    idnum_MAINTAIN, confidence_MAINTAIN = recognizer_MAINTAIN.predict(face_area)
                    if confidence_MAINTAIN < 45:
                        #idnum_MAINTAIN = names[idum_MAINTAIN]
                        print('confidence=', confidence_MAINTAIN)
                        # 注上姓名
                        cv2.putText(img, names[idum_MAINTAIN], (x, y - 6), 3, 1.2, (0, 0, 255), 2, cv2.LINE_AA)

            # 实时展示效果画面
            cv2.imshow('frame4', img)
            # 每5毫秒监听一次键盘动作
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        # 最后，关闭所有窗口
        cap.release()
        cv2.destroyWindow('frame4')

    def show_message(self):
        msgBox1 = QMessageBox()
        msgBox1.setWindowTitle("使用需知")
        msgBox1.setText("请先认真阅读附带的txt文件，后开始使用本程序")
        msgBox1.exec_()

    def show_message_again(self):
        msgBox2 = QMessageBox()
        msgBox2.setWindowTitle("关于")
        msgBox2.setText("这是一个基础的人脸识别demo\n风起鸿庄制作\n生日快乐我的朋友~")
        msgBox2.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 491, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAccessibleName("")
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 191, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 291, 121))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 310, 291, 121))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(270, 30, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 291, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("在这里输入你的名字")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 70, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 200, 91, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 231, 41))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(20, 140, 411, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 370, 331, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(20, 310, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 311, 491))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 200, 141, 111))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionjieshao = QtWidgets.QAction(MainWindow)
        self.actionjieshao.setObjectName("actionjieshao")
        self.actionguanyu = QtWidgets.QAction(MainWindow)
        self.actionguanyu.setObjectName("actionguanyu")
        self.menu.addAction(self.actionjieshao)
        self.menu_2.addAction(self.actionguanyu)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionjieshao.triggered.connect(self.show_message)
        self.actionguanyu.triggered.connect(self.show_message_again)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别demo"))
        self.label.setText(_translate("MainWindow", "摄像头检测人脸面部中..."))
        self.pushButton.setText(_translate("MainWindow", "识别人脸和眼睛"))
        self.pushButton.clicked.connect(self.easy_face1)
        self.pushButton_2.setText(_translate("MainWindow", "也可以识别微笑哦"))
        self.pushButton_2.clicked.connect(self.easy_face2)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "人脸检测"))
        self.pushButton_3.setText(_translate("MainWindow", "确认"))
        self.pushButton_3.clicked.connect(self.edit_name)
        self.pushButton_4.setText(_translate("MainWindow", "开始！"))
        self.pushButton_4.clicked.connect(self.catch_face)
        self.label_2.setText(_translate("MainWindow", "点击按钮开始录入人脸"))
        self.pushButton_5.setText(_translate("MainWindow", "生成人脸识别文件"))
        self.pushButton_5.clicked.connect(self.shengcheng)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "人脸训练"))
        self.pushButton_6.setText(_translate("MainWindow", "点击识别身份"))
        self.pushButton_6.clicked.connect(self.shibie)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "人脸身份识别"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.actionjieshao.setText(_translate("MainWindow", "基础操作"))
        self.actionguanyu.setText(_translate("MainWindow", "关于作者"))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
