from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sqlite3
import os
import threading
from flask import Flask, request
from werkzeug.serving import make_server
import subprocess
import psutil
import time
import gostcrypto

appf = Flask(__name__)
server = None  # Переменная для хранения сервера
thread = None  # Переменная для хранения потока сервера
stop_event = threading.Event()  # Событие для остановки сервера

@appf.route('/suspicious_cookies', methods=['POST'])
def suspicious_cookies():
    data = request.json
    for cookie in data:
        domain = cookie.get('domain')
        name = cookie.get('name')
        secure = cookie.get('secure')
        httponly = cookie.get('httpOnly')
        # Обновляем UI с полученными куками
        ui.textEdit.append(f"- Домен: {domain}, Имя: {name}, Secure: {secure}, HttpOnly: {httponly}")  # Добавляем информацию о куки в textEdit
    return '', 204

def run_flask():
    global server
    server = make_server('127.0.0.1', 5000, appf)
    while not stop_event.is_set():  # Проверяем флаг остановки
        server.handle_request()  # Обрабатываем один запрос
    server.shutdown()  # Останавливаем сервер после обработки текущих запросов

def stop_flask():
    stop_event.set()  # Устанавливаем событие остановки
    print("Сервер останавливается...")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1800, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(68, 68, 68);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 751, 281))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(70)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255)")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 1821, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("cookie2.png"))
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1430, 30, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.btn_yandex = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yandex.setGeometry(QtCore.QRect(1430, 90, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.btn_yandex.setFont(font)
        self.btn_yandex.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_yandex.setObjectName("btn_yandex")
        self.btn_google = QtWidgets.QPushButton(self.centralwidget)
        self.btn_google.setGeometry(QtCore.QRect(1430, 150, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.btn_google.setFont(font)
        self.btn_google.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_google.setObjectName("btn_google")
        self.btn_firefox = QtWidgets.QPushButton(self.centralwidget)
        self.btn_firefox.setGeometry(QtCore.QRect(1430, 210, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.btn_firefox.setFont(font)
        self.btn_firefox.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_firefox.setObjectName("btn_firefox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1680, 80, 51, 51))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Yandex logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1680, 140, 51, 51))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Google logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1680, 200, 51, 51))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Firefox logo.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 370, 601, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255); selection-background-color: white; selection-color: black;")
        self.btn_display = QtWidgets.QPushButton(self.centralwidget)
        self.btn_display.setGeometry(QtCore.QRect(250, 810, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_display.setFont(font)
        self.btn_display.setAcceptDrops(False)
        self.btn_display.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_display.setObjectName("btn_display")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(490, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_delete.setFont(font)
        self.btn_delete.setAcceptDrops(False)
        self.btn_delete.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_start_monitoring = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_monitoring.setGeometry(QtCore.QRect(740, 320, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_start_monitoring.setFont(font)
        self.btn_start_monitoring.setAcceptDrops(False)
        self.btn_start_monitoring.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_start_monitoring.setObjectName("btn_start_monitoring")
        self.btn_stop_monitoring = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop_monitoring.setGeometry(QtCore.QRect(990, 320, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_stop_monitoring.setFont(font)
        self.btn_stop_monitoring.setAcceptDrops(False)
        self.btn_stop_monitoring.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_stop_monitoring.setObjectName("btn_stop_monitoring")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(740, 370, 981, 431))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(270, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_encrypt.setFont(font)
        self.btn_encrypt.setAcceptDrops(False)
        self.btn_encrypt.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_block = QtWidgets.QPushButton(self.centralwidget)
        self.btn_block.setGeometry(QtCore.QRect(50, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_block.setFont(font)
        self.btn_block.setAcceptDrops(False)
        self.btn_block.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_block.setObjectName("btn_block")
        self.btn_encrypt_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt_back.setGeometry(QtCore.QRect(430, 320, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_encrypt_back.setFont(font)
        self.btn_encrypt_back.setAcceptDrops(False)
        self.btn_encrypt_back.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_encrypt_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("undo logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_encrypt_back.setIcon(icon)
        self.btn_encrypt_back.setObjectName("btn_encrypt_back")
        self.btn_block_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_block_back.setGeometry(QtCore.QRect(210, 320, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_block_back.setFont(font)
        self.btn_block_back.setAcceptDrops(False)
        self.btn_block_back.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_block_back.setText("")
        self.btn_block_back.setIcon(icon)
        self.btn_block_back.setObjectName("btn_block_back")
        self.btn_analysis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analysis.setGeometry(QtCore.QRect(1240, 320, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_analysis.setFont(font)
        self.btn_analysis.setAcceptDrops(False)
        self.btn_analysis.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_analysis.setObjectName("btn_analysis")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(1490, 320, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.btn_update.setFont(font)
        self.btn_update.setAcceptDrops(False)
        self.btn_update.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_update.setObjectName("btn_update")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(1310, 820, 411, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btn_yandex.raise_()
        self.btn_google.raise_()
        self.btn_firefox.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.tableWidget.raise_()
        self.btn_display.raise_()
        self.btn_delete.raise_()
        self.btn_start_monitoring.raise_()
        self.btn_stop_monitoring.raise_()
        self.textEdit.raise_()
        self.btn_encrypt.raise_()
        self.btn_block.raise_()
        self.btn_encrypt_back.raise_()
        self.btn_block_back.raise_()
        self.btn_analysis.raise_()
        self.btn_update.raise_()
        self.radioButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_start_monitoring.clicked.connect(self.start_monitoring)
        self.btn_stop_monitoring.clicked.connect(self.stop_monitoring)
        self.btn_analysis.clicked.connect(self.analyze_cookies)
        self.btn_update.clicked.connect(self.delete_expired_cookies)
        self.radioButton.toggled.connect(self.toggle_auto_update)

        self.btn_block.clicked.connect(self.block_cookies)
        self.btn_block_back.clicked.connect(self.unblock_cookies)

        self.btn_encrypt.clicked.connect(self.encrypt_cookies)
        self.btn_encrypt_back.clicked.connect(self.decrypt_cookies)

        self.btn_delete.clicked.connect(self.delete_cookies)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CookieCaddy"))
        MainWindow.setWindowIcon(QIcon("Cookie Icon.png"))
        self.label_2.setText(_translate("MainWindow", "CookieCaddy"))
        self.label_3.setText(_translate("MainWindow", "Выберете браузер"))
        self.btn_yandex.setText(_translate("MainWindow", "Yandex"))
        self.btn_google.setText(_translate("MainWindow", "Google Chrome"))
        self.btn_firefox.setText(_translate("MainWindow", "Firefox"))
        self.btn_display.setText(_translate("MainWindow", "Отобразить cookie"))
        self.btn_display.setEnabled(False)
        self.btn_display.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_delete.setText(_translate("MainWindow", "Удалить"))
        self.btn_delete.setEnabled(False)
        self.btn_delete.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_start_monitoring.setText(_translate("MainWindow", "Начать мониторинг"))
        self.btn_start_monitoring.setEnabled(False)
        self.btn_start_monitoring.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_stop_monitoring.setText(_translate("MainWindow", "Остановить мониторинг"))
        self.btn_stop_monitoring.setEnabled(False)
        self.btn_stop_monitoring.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_encrypt.setText(_translate("MainWindow", "Зашифровать"))
        self.btn_encrypt.setEnabled(False)
        self.btn_encrypt.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_encrypt_back.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_block.setText(_translate("MainWindow", "Заблокировать"))
        self.btn_block.setEnabled(False)
        self.btn_block.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_block_back.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_analysis.setText(_translate("MainWindow", "Провести анализ"))
        self.btn_analysis.setEnabled(False)
        self.btn_analysis.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.btn_update.setText(_translate("MainWindow", "Обновить"))
        self.btn_update.setEnabled(False)
        self.btn_update.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
        self.radioButton.setText(_translate("MainWindow", "Автоматическое обновление cookie-файлов"))
        self.radioButton.setEnabled(False)
        self.radioButton.setStyleSheet("color: rgb(120, 120, 120); border: none;")

        self.btn_yandex.clicked.connect(lambda: self.set_browser("yandex"))
        self.btn_google.clicked.connect(lambda: self.set_browser("chrome"))
        self.btn_firefox.clicked.connect(lambda: self.set_browser("firefox"))
        self.btn_display.clicked.connect(self.display_cookies)

    def set_browser(self, browser_name):
        self.reset_button_styles()

        self.browser_paths = {
            "firefox": r"C:\Users\Дмитрий\AppData\Roaming\Mozilla\Firefox\Profiles\6tzg50mf.default-release\cookies.sqlite",
            "chrome": r"C:\Users\Дмитрий\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies",
            "yandex": r"C:\Users\Дмитрий\AppData\Local\Yandex\YandexBrowser\User Data\Default\Network\Cookies"
        }

        if browser_name in self.browser_paths:
            # Разблокирование кнопок
            self.btn_display.setEnabled(True)
            self.btn_display.setStyleSheet("color: rgb(255, 255, 255)")
            self.btn_start_monitoring.setEnabled(True)
            self.btn_start_monitoring.setStyleSheet("color: rgb(255, 255, 255)")
            self.btn_analysis.setEnabled(True)
            self.btn_analysis.setStyleSheet("color: rgb(255, 255, 255)")
            self.btn_update.setEnabled(True)
            self.btn_update.setStyleSheet("color: rgb(255, 255, 255)")
            self.radioButton.setEnabled(True)
            self.radioButton.setStyleSheet("color: rgb(255, 255, 255)")
            self.current_browser = self.browser_paths[browser_name]
            if browser_name == "firefox":
                self.btn_firefox.setStyleSheet("background-color: rgb(100, 100, 100); color: white; border: none;")
                self.textEdit.append("Выбран браузер Mozila Firefox")
            elif browser_name == "chrome":
                self.btn_google.setStyleSheet("background-color: rgb(100, 100, 100); color: white; border: none;")
                self.textEdit.append("Выбран браузер Google Chrome")
            elif browser_name == "yandex":
                self.btn_yandex.setStyleSheet("background-color: rgb(100, 100, 100); color: white; border: none;")
                self.textEdit.append("Выбран браузер Yandex Browser")

    def reset_button_styles(self):
        # Сбросить стиль для всех кнопок
        self.btn_yandex.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_google.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_firefox.setStyleSheet("color: rgb(255, 255, 255);")

    def is_browser_open(self, browser_name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'][:4] in self.current_browser.lower():
                return True
        return False

    def browser_close(self):
        # Закрытие браузера
        if 'chrome' in self.current_browser.lower():
            if self.is_browser_open('chrome.exe'):
                os.system('taskkill /F /IM chrome.exe')
                self.browser_is_open = False
        elif 'yandex' in self.current_browser.lower():
            if self.is_browser_open('browser.exe'):
                os.system('taskkill /F /IM browser.exe')
                self.browser_is_open = False
        elif 'firefox' in self.current_browser.lower():
            if self.is_browser_open('firefox.exe'):
                os.system('taskkill /F /IM firefox.exe')
                self.browser_is_open = False

    def browser_open(self):
        if self.current_browser and not self.is_browser_open(os.path.basename(self.current_browser)):
            try:
                if 'chrome' in self.current_browser.lower():
                    subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
                elif 'yandex' in self.current_browser.lower():
                    subprocess.Popen(['C:\\Program Files (x86)\\Yandex\\YandexBrowser\\Application\\browser.exe'])
                elif 'firefox' in self.current_browser.lower():
                    subprocess.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe'])
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось открыть браузер: {str(e)}")

    def display_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True

            self.tableWidget.clearContents()  # Очистка содержимого таблицы
            self.tableWidget.setRowCount(0)  # Сброс количества строк

            if not os.path.exists(self.current_browser):
                QtWidgets.QMessageBox.critical(None, "Ошибка", "Файл куков не найден.")
                return

            try:
                conn = sqlite3.connect(self.current_browser)
                conn.text_factory = lambda b: b.decode(errors='ignore')
                cursor = conn.cursor()

                # Определяем названия колонок в зависимости от браузера
                if 'firefox' in self.current_browser.lower():
                    cursor.execute("SELECT name, value, host, isSecure, isHttpOnly FROM moz_cookies")
                    column_names = ['Имя', 'Значение', 'Хост', 'Secure', 'HttpOnly']
                elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                    cursor.execute("SELECT name, encrypted_value, host_key, is_secure, is_httponly FROM cookies")
                    column_names = ['Имя', 'Зашифрованное значение', 'Хост', 'Secure', 'HttpOnly']
                else:
                    raise ValueError("Некорректный браузер")

                # Получаем данные
                rows = cursor.fetchall()

                # Установите количество колонок и названия
                self.tableWidget.setColumnCount(len(column_names))
                self.tableWidget.setHorizontalHeaderLabels(column_names)

                if not rows:
                    QtWidgets.QMessageBox.information(None, "Информация", "Куки не найдены.")
                else:
                    for row in rows:
                        row_position = self.tableWidget.rowCount()
                        self.tableWidget.insertRow(row_position)
                        for column, value in enumerate(row):
                            if isinstance(value, bytes):  # Если значение байт
                                try:
                                    value = value.decode('utf-8', 'ignore')  # Декодирование
                                except Exception as e:
                                    value = "<ошибка декодирования>"  # Обработка ошибки декодирования
                            self.tableWidget.setItem(row_position, column, QtWidgets.QTableWidgetItem(str(value)))

                            # Проверка на зашифрованные куки
                            if isinstance(row[1], bytes) and row[1].startswith(b"ENC_"):
                                for column in range(self.tableWidget.columnCount()):
                                    item = self.tableWidget.item(row_position, column)
                                    if item:
                                        self.tableWidget.item(row_position, column).setBackground(QtGui.QColor(0, 100, 0))

                conn.close()

                self.tableWidget.setColumnWidth(0, 120)
                self.tableWidget.setColumnWidth(1, 190)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.resizeColumnToContents(3)
                self.tableWidget.resizeColumnToContents(4)

                self.btn_block.setEnabled(True)
                self.btn_block.setStyleSheet("color: rgb(255, 255, 255)")
                self.btn_block_back.setEnabled(True)
                self.btn_block_back.setStyleSheet("color: rgb(255, 255, 255)")
                self.btn_encrypt.setEnabled(True)
                self.btn_encrypt.setStyleSheet("color: rgb(255, 255, 255)")
                self.btn_encrypt_back.setEnabled(True)
                self.btn_encrypt_back.setStyleSheet("color: rgb(255, 255, 255)")
                self.btn_delete.setEnabled(True)
                self.btn_delete.setStyleSheet("color: rgb(255, 255, 255)")

                for row in range(self.tableWidget.rowCount()):
                    if self.tableWidget.item(row, 0).text().endswith(" (blocked)"):
                        for column in range(self.tableWidget.columnCount()):
                            item = self.tableWidget.item(row, column)
                            if item:
                                self.tableWidget.item(row, column).setBackground(QtGui.QColor(40, 40, 40))

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось получить куки: {str(e)}")

            # Открываем браузер только если он был закрыт
            if not is_open:
                self.browser_open()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось отобразить куки: {str(e)}")

    def start_monitoring(self):
        try:
            global thread, stop_event
            self.btn_start_monitoring.setEnabled(False)  # Отключить кнопку во время мониторинга
            self.btn_start_monitoring.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
            self.btn_stop_monitoring.setEnabled(True)  # Включить кнопку остановки
            self.btn_stop_monitoring.setStyleSheet("color: rgb(255, 255, 255)")

            # Запуск Flask сервера в отдельном потоке
            stop_event.clear()  # Сбрасываем событие перед запуском
            thread = threading.Thread(target=run_flask, daemon=True)
            thread.start()
            self.textEdit.append("Мониторинг начат...")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось начать мониторинг: {str(e)}")

    def stop_monitoring(self):
        try:
            stop_flask()  # Останавливаем сервер
            self.btn_stop_monitoring.setEnabled(False)
            self.btn_stop_monitoring.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(170, 170, 170); border: none;")
            self.btn_start_monitoring.setEnabled(True)  # Включаем кнопку начала мониторинга
            self.btn_start_monitoring.setStyleSheet("color: rgb(255, 255, 255)")
            self.textEdit.append("Мониторинг остановлен.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось остановить мониторинг: {str(e)}")

    def is_suspicious_cookie(self, cookie):
        value = cookie[2]
        suspicious_names = ['sessionid', 'token', 'auth', 'login']
        suspicious_domains = ['malicious.com', 'fake.com']

        # Проверяем, что куки не имеют secure и httpOnly
        if cookie[3] or cookie[4]:  # is_secure, is_httponly
            return False

        elif len(value) > 100:
            return True  # Слишком длинное значение

        # Проверяем имя куки на наличие подозрительных подстрок
        elif any(name in cookie[1].lower() for name in suspicious_names):  # cookie[1] - name
            return True  # Подозрительное имя

        # Проверяем домен куки (можно добавить свои подозрительные домены)
        elif cookie[0] in suspicious_domains:  # cookie[0] - host_key
            return True  # Подозрительный домен

        else:
            return False  # Кука не подозрительная

    def analyze_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True

            suspicious_cookies = []  # Список для хранения подозрительных куков
            try:
                conn = sqlite3.connect(self.current_browser)
                conn.text_factory = lambda b: b.decode(errors='ignore')
                cursor = conn.cursor()

                # Получаем куки
                if 'firefox' in self.current_browser.lower():
                    cursor.execute("SELECT host, name, value, isSecure, isHttpOnly FROM moz_cookies")
                    cookies = cursor.fetchall()

                    for cookie in cookies:
                        if self.is_suspicious_cookie(cookie):
                            suspicious_cookies.append({
                                'domain': cookie[0],
                                'name': cookie[1],
                                'value': cookie[2],
                                'secure': cookie[3],
                                'httpOnly': cookie[4]
                            })
                else:
                    # Обработка для других браузеров (Chrome, Yandex)
                    cursor.execute("SELECT host_key, name, encrypted_value, is_secure, is_httponly FROM cookies")
                    cookies = cursor.fetchall()

                    for cookie in cookies:
                        if self.is_suspicious_cookie(cookie):
                            suspicious_cookies.append({
                                'domain': cookie[0],
                                'name': cookie[1],
                                'value': cookie[2],
                                'secure': cookie[3],
                                'httpOnly': cookie[4],
                            })

                if suspicious_cookies:
                    self.textEdit.append("Подозрительные куки найдены:")
                    for cookie in suspicious_cookies:
                        self.textEdit.append(
                            f"Домен: {cookie['domain']}, Имя: {cookie['name']}, Secure: {cookie['secure']}, HttpOnly: {cookie['httpOnly']}")
                else:
                    self.textEdit.append("Подозрительных куков не найдено.")

                conn.close()
            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось выполнить анализ: {str(e)}")

            if not is_open:
                self.browser_open()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось выполнить анализ: {str(e)}")

    def delete_expired_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True

            self.textEdit.append('Обновление cookie-файлов')
            if 'chrome' in self.current_browser.lower():
                cookie_db_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User  Data', 'Default',
                                              'Network', 'Cookies')
            elif 'yandex' in self.current_browser.lower():
                cookie_db_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Yandex', 'YandexBrowser', 'User  Data', 'Default',
                                              'Network', 'Cookies')
            elif 'firefox' in self.current_browser.lower():
                # Путь к папке профиля Firefox
                profile_path = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')
                # Получаем первый профиль (может быть несколько)
                profiles = [d for d in os.listdir(profile_path) if d.endswith('.default-release') or d.endswith('.default')]
                if profiles:
                    cookie_db_path = os.path.join(profile_path, profiles[0], 'cookies.sqlite')
                else:
                    self.textEdit.append('Firefox profile not found')
                    raise ValueError("Firefox profile not found")
            else:
                self.textEdit.append('Unsupported browser')
                raise ValueError("Unsupported browser")
            try:
                # Подключение к базе данных куки
                conn = sqlite3.connect(self.current_browser)
                conn.text_factory = lambda b: b.decode(errors='ignore')
                cursor = conn.cursor()

                # Получаем текущее время
                current_time = int(time.time())

                # Запрос на выборку всех куки
                deleted_cookie = ''
                suspicious_cookies = []
                if 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                    cursor.execute("SELECT expires_utc, host_key, encrypted_value, is_secure, is_httponly, name FROM cookies")
                    cookies = cursor.fetchall()
                    for cookie in cookies:
                        if self.is_suspicious_cookie(cookie):
                            suspicious_cookies.append({
                                'expires_utc': cookie[0],
                                'domain': cookie[1],
                                'value': cookie[2],
                                'secure': cookie[3],
                                'httpOnly': cookie[4],
                                'name': cookie[5]
                            })
                    # Удаляем куки, у которых время существования истекло
                        expires_utc, domain, value, secure, httpOnly, name = cookie
                        # Преобразуем expires_utc в секунды
                        if isinstance(expires_utc, int):
                            print(cookie)
                            print(expires_utc / 1000000, current_time)
                            if expires_utc > 0 and expires_utc / 1000000 < current_time:  # Учитываем, что expires_utc хранится в микросекундах
                                print('f')
                                cursor.execute("DELETE FROM cookies WHERE name = ?", (name,))
                                deleted_cookie += f"- Домен: {cookie[1]}, Имя: {cookie[5]}, Secure: {cookie[3]}, HttpOnly: {cookie[4]}\n"
                    if deleted_cookie != '':
                        self.textEdit.append('Удаленные файлы-cookie с истекшим сроком действия:')
                        self.textEdit.append(deleted_cookie)
                    else:
                        self.textEdit.append('Файлов cookie с истекшим сроком действия не обнаружено.')

                elif 'firefox' in self.current_browser.lower():
                    cursor.execute("SELECT expiry, host, value, isSecure, isHttpOnly, name FROM moz_cookies")
                    cookies = cursor.fetchall()

                    for cookie in cookies:
                        if self.is_suspicious_cookie(cookie):
                            suspicious_cookies.append({
                                'expires_utc': cookie[0],
                                'domain': cookie[1],
                                'value': cookie[2],
                                'secure': cookie[3],
                                'httpOnly': cookie[4],
                                'name': cookie[5]
                            })
                        # Удаляем куки, у которых время существования истекло
                        expires_utc, domain, value, secure, httpOnly, name = cookie
                        # Преобразуем expires_utc в секунды
                        if isinstance(expires_utc, int):
                            if expires_utc > 0 and expires_utc / 1000000 < current_time:  # Учитываем, что expires_utc хранится в микросекундах
                                cursor.execute("DELETE FROM moz_cookies WHERE name = ?", (name,))
                                deleted_cookie += f"- Домен: {cookie[1]}, Имя: {cookie[5]}, Secure: {cookie[3]}, HttpOnly: {cookie[4]}\n"
                    if deleted_cookie != '':
                        self.textEdit.append('Удаленные файлы-cookie с истекшим сроком действия:')
                        self.textEdit.append(deleted_cookie)
                    else:
                        self.textEdit.append('Файлов cookie с истекшим сроком действия не обнаружено.')

                # Сохраняем изменения и закрываем соединение
                conn.commit()
                conn.close()

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось выполнить обновление: {str(e)}")

            if not is_open:
                self.browser_open()
        except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось провести обновление: {str(e)}")

    def toggle_auto_update(self):
        if self.radioButton.isChecked():
            self.textEdit.append("Автоматическое обновление включено.")
            self.start_auto_update()  # Запускаем автоматическое обновление
        else:
            self.textEdit.append("Автоматическое обновление отключено.")
            self.stop_auto_update()  # Останавливаем автоматическое обновление

    def start_auto_update(self):
        try:
            self.auto_update_thread = threading.Thread(target=self.auto_update_expired_cookies, daemon=True)
            self.auto_update_thread.start()
        except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось провести автоматическое обновление: {str(e)}")

    def stop_auto_update(self):
        self.auto_update_running = False  # Останавливаем цикл в потоке

    def auto_update_expired_cookies(self):
        self.auto_update_running = True
        while self.auto_update_running:
            self.delete_expired_cookies()  # Удаляем истекшие куки
            time.sleep(60)  # Ждем 60 секунд перед следующей проверкой

    def create_blocked_cookies_db(self):
        # Определяем имя файла базы данных в зависимости от браузера
        if self.current_browser == r"C:\Users\Дмитрий\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies":
            db_file = 'blocked_cookies_Google.db'
        elif self.current_browser == r"C:\Users\Дмитрий\AppData\Local\Yandex\YandexBrowser\User Data\Default\Network\Cookies":
            db_file = 'blocked_cookies_Yandex.db'
        elif self.current_browser == r"C:\Users\Дмитрий\AppData\Roaming\Mozilla\Firefox\Profiles\6tzg50mf.default-release\cookies.sqlite":
            db_file = 'blocked_cookies_Firefox.db'
        else:
            raise ValueError("Неизвестный браузер")

        if not os.path.exists(db_file):
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS blocked_cookies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    value TEXT,
                    domain TEXT,
                    secure INTEGER,
                    httponly INTEGER
                )
            ''')
            conn.commit()
            conn.close()

    def block_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True

            selected_items = self.tableWidget.selectedItems()
            if not selected_items:
                QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пожалуйста, выберите куки для блокировки.")
                return

            # Создаем базу данных для заблокированных куков
            self.create_blocked_cookies_db()

            blocked_cookies = set()  # Для вывода уникальных заблокированных куков

            for item in selected_items:
                row = item.row()
                original_cookie_name = self.tableWidget.item(row, 0).text()  # Оригинальное имя куки
                cookie_value = self.tableWidget.item(row, 1).text()
                cookie_domain = self.tableWidget.item(row, 2).text()
                cookie_secure = self.tableWidget.item(row, 3).text()
                cookie_httponly = self.tableWidget.item(row, 4).text()

                # Проверяем, является ли куки уже заблокированным
                if original_cookie_name.endswith(" (blocked)"):
                    self.textEdit.append(f"Куки '{original_cookie_name}' уже заблокированы.")
                    continue  # Пропускаем этот кук, так как он уже заблокирован

                # Создаем имя заблокированного куки
                blocked_cookie_name = f"{original_cookie_name} (blocked)"

                # Проверяем, добавлен ли куки в базу данных
                if blocked_cookie_name not in blocked_cookies:
                    # Сохранение куков в базу данных заблокированных куков
                    if self.current_browser == r"C:\Users\Дмитрий\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies":
                        conn = sqlite3.connect('blocked_cookies_Google.db')
                    elif self.current_browser == r"C:\Users\Дмитрий\AppData\Local\Yandex\YandexBrowser\User Data\Default\Network\Cookies":
                        conn = sqlite3.connect('blocked_cookies_Yandex.db')
                    elif self.current_browser == r"C:\Users\Дмитрий\AppData\Roaming\Mozilla\Firefox\Profiles\6tzg50mf.default-release\cookies.sqlite":
                        conn = sqlite3.connect('blocked_cookies_Firefox.db')
                    else:
                        raise ValueError("Неизвестный браузер")

                    cursor = conn.cursor()
                    cursor.execute(
                        'INSERT INTO blocked_cookies (name, value, domain, secure, httponly) VALUES (?, ?, ?, ?, ?)',
                        (blocked_cookie_name, cookie_value, cookie_domain, cookie_secure, cookie_httponly))
                    conn.commit()
                    conn.close()

                    blocked_cookies.add(blocked_cookie_name)  # Добавляем в множество для вывода

                # Изменение кука в оригинальной базе данных
                conn = sqlite3.connect(self.current_browser)
                cursor = conn.cursor()

                # Используем оригинальное имя куки для обновления
                if 'firefox' in self.current_browser.lower():
                    cursor.execute(
                        'UPDATE moz_cookies SET name = ?, value = ?, host = ?, isSecure = ?, isHttpOnly = ? WHERE name = ? AND host = ?',
                        (blocked_cookie_name, "-", "-", "-", "-", original_cookie_name, cookie_domain))
                elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                    cursor.execute(
                        'UPDATE cookies SET name = ?, encrypted_value = ?, host_key = ?, is_secure = ?, is_httponly = ? WHERE name = ? AND host_key = ?',
                        (blocked_cookie_name, "-", "-", "-", "-", original_cookie_name, cookie_domain))
                conn.commit()
                conn.close()

                # Обновляем имя куки в таблице
                self.tableWidget.item(row, 0).setText(blocked_cookie_name)

                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item:
                        self.tableWidget.item(row, column).setBackground(QtGui.QColor(40, 40, 40))

            # Выводим сообщения
            if blocked_cookies:
                self.textEdit.append(f"Заблокированы куки: {', '.join(blocked_cookies)}")

            if not is_open:
                self.browser_open()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось заблокировать куки: {str(e)}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось заблокировать куки: {str(e)}")

    def unblock_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True

            selected_items = self.tableWidget.selectedItems()
            if not selected_items:
                QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пожалуйста, выберите куки для разблокировки.")
                return

            # Получаем имя файла базы данных заблокированных куков
            if 'firefox' in self.current_browser.lower():
                db_file = 'blocked_cookies_Firefox.db'
            elif 'chrome' in self.current_browser.lower():
                db_file = 'blocked_cookies_Google.db'
            elif 'yandex' in self.current_browser.lower():
                db_file = 'blocked_cookies_Yandex.db'
            if not os.path.exists(db_file):
                QtWidgets.QMessageBox.warning(None, "Предупреждение", "Нет заблокированных куков для восстановления.")
                return

            # Подключение к базе данных заблокированных куков
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # Подключение к оригинальной базе данных куков браузера
            original_conn = sqlite3.connect(self.current_browser)
            original_cursor = original_conn.cursor()

            for item in selected_items:
                row = item.row()
                blocked_cookie_name = self.tableWidget.item(row, 0).text()  # Имя заблокированного куки

                # Проверяем, является ли куки заблокированным
                if not blocked_cookie_name.endswith(" (blocked)"):
                    QtWidgets.QMessageBox.warning(None, "Предупреждение",
                                                  "Выберите заблокированный куки для разблокировки.")
                    continue

                # Удаляем "(blocked)" из имени куки
                original_cookie_name = blocked_cookie_name[:-10]  # Убираем " (blocked)"

                # Получаем данные из базы данных заблокированных куков
                cursor.execute("SELECT value, domain, secure, httponly FROM blocked_cookies WHERE name = ?",
                               (blocked_cookie_name,))
                blocked_cookie_data = cursor.fetchone()

                if blocked_cookie_data:
                    cookie_value, cookie_domain, cookie_secure, cookie_httponly = blocked_cookie_data

                # Восстанавливаем куки в оригинальной базе данных
                if 'firefox' in self.current_browser.lower():
                    original_cursor.execute(
                        'UPDATE moz_cookies SET name = ?, value = ?, host = ?, isSecure = ?, isHttpOnly = ? WHERE name = ?',
                        (original_cookie_name, cookie_value, cookie_domain, cookie_secure, cookie_httponly, original_cookie_name + ' (blocked)'))
                elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                    original_cursor.execute(
                        'UPDATE cookies SET name = ?, encrypted_value = ?, host_key = ?, is_secure = ?, is_httponly = ? WHERE name = ?',
                        (original_cookie_name, cookie_value, cookie_domain, cookie_secure, cookie_httponly, original_cookie_name + ' (blocked)'))

                # Удаляем куки из базы данных заблокированных куков
                cursor.execute("DELETE FROM blocked_cookies WHERE name = ?", (blocked_cookie_name,))

                # Обновляем имя куки в таблице
                self.tableWidget.item(row, 0).setText(original_cookie_name)

                # Меняем цвет фона строки на стандартный
                for column in range(self.tableWidget.columnCount()):
                    self.tableWidget.item(row, column).setBackground(QtGui.QColor(68, 68, 68))

            # Сохраняем изменения
            original_conn.commit()
            original_conn.close()
            conn.commit()
            conn.close()

            self.textEdit.append("Заблокированные куки восстановлены.")

            if not is_open:
                self.browser_open()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось восстановить куки: {str(e)}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось провести разблокировку: {str(e)}")

    def load_key(self, file_path):
        with open(file_path, 'rb') as key_file:
            key = key_file.read()
        return key

    def encrypt_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True

            selected_items = self.tableWidget.selectedItems()
            if not selected_items:
                QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пожалуйста, выберите куки для шифрования.")
                return

            # Генерация ключа
            key = self.load_key('encryption_key.bin')

            for item in selected_items:
                row = item.row()
                cookie_name = self.tableWidget.item(row, 0).text()
                cookie_domain = self.tableWidget.item(row, 2).text()

                try:
                    conn = sqlite3.connect(self.current_browser)
                    cursor = conn.cursor()

                    if 'firefox' in self.current_browser.lower():
                        cursor.execute(
                            'SELECT value FROM moz_cookies WHERE name = ? AND host = ?',
                            (cookie_name, cookie_domain))
                    elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                        cursor.execute(
                            'SELECT encrypted_value FROM cookies WHERE name = ? AND host_key = ?',
                            (cookie_name, cookie_domain))

                    result = cursor.fetchone()
                    conn.close()

                    if result is None:
                        QtWidgets.QMessageBox.warning(None, "Предупреждение",
                                                      f"Куки '{cookie_name}' не найдены.")
                        continue

                    cookie_value = result[0]

                    # Проверка, зашифрованы ли куки
                    if isinstance(cookie_value, bytes) and cookie_value.startswith(b"ENC_"):
                        self.textEdit.append(f"Куки '{cookie_name}' уже зашифрованы.")
                        continue

                    # Преобразуем значение куки в байты, если это необходимо
                    if not isinstance(cookie_value, bytes):
                        cookie_value = cookie_value.encode('utf-8')  # Преобразуем в байты для шифрования

                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось получить куки: {str(e)}")
                    continue

                # Шифрование значения куки
                try:
                    cipher = gostcrypto.gostcipher.new('kuznechik', key, gostcrypto.gostcipher.MODE_ECB)
                    # Дополняем значение до 32 байт
                    padded_value = cookie_value.ljust(32)
                    encrypted_value = cipher.encrypt(padded_value)  # Шифруем текущее значение

                    # Добавляем префикс для обозначения зашифрованного значения
                    encrypted_value_with_prefix = b"ENC_" + encrypted_value

                    # Обновление значения куки в базе данных
                    conn = sqlite3.connect(self.current_browser)
                    cursor = conn.cursor()

                    if 'firefox' in self.current_browser.lower():
                        cursor.execute(
                            'UPDATE moz_cookies SET value = ? WHERE name = ? AND host = ?',
                            (encrypted_value_with_prefix, cookie_name, cookie_domain))
                    elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                        cursor.execute(
                            'UPDATE cookies SET encrypted_value = ? WHERE name = ? AND host_key = ?',
                            (encrypted_value_with_prefix, cookie_name, cookie_domain))
                    conn.commit()
                    conn.close()

                    # Обновление значения в таблице приложения
                    self.tableWidget.item(row, 1).setText(encrypted_value_with_prefix.hex())
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item:
                            item.setBackground(QtGui.QColor(0, 100, 0))

                    self.textEdit.append(f"Значение куки '{cookie_name}' было зашифровано.")

                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось зашифровать куки: {str(e)}")

            if not is_open:
                self.browser_open()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось зашифровать куки: {str(e)}")

    def decrypt_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True

            selected_items = self.tableWidget.selectedItems()
            if not selected_items:
                QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пожалуйста, выберите куки для расшифровки.")
                return

            # Загрузка ключа
            key = self.load_key('encryption_key.bin')

            # Проходим по выбранным кукам и расшифровываем их значения
            try:
                for item in selected_items:
                    row = item.row()
                    cookie_name = self.tableWidget.item(row, 0).text()  # Имя куки
                    cookie_domain = self.tableWidget.item(row, 2).text()  # Домен куки

                    # Подключение к базе данных
                    conn = sqlite3.connect(self.current_browser)
                    cursor = conn.cursor()

                    # Получаем зашифрованное значение куки
                    if 'firefox' in self.current_browser.lower():
                        cursor.execute(
                            'SELECT value FROM moz_cookies WHERE name = ? AND host = ?',
                            (cookie_name, cookie_domain))
                    elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                        cursor.execute(
                            'SELECT encrypted_value FROM cookies WHERE name = ? AND host_key = ?',
                            (cookie_name, cookie_domain))

                    result = cursor.fetchone()
                    conn.close()

                    if result is None:
                        QtWidgets.QMessageBox.warning(None, "Предупреждение", f"Куки '{cookie_name}' не найдены.")
                        continue

                    encrypted_value = result[0]

                    # Убедимся, что значение начинается с префикса 'ENC_'
                    if isinstance(encrypted_value, bytes) and encrypted_value.startswith(b"ENC_"):
                        encrypted_value = encrypted_value[4:]  # Убираем префикс

                    # Расшифрование значения куки
                    cipher = gostcrypto.gostcipher.new('kuznechik', key, gostcrypto.gostcipher.MODE_ECB)
                    decrypted_value = cipher.decrypt(encrypted_value)  # Расшифровка
                    decrypted_value = decrypted_value.rstrip(b'\x00')  # Удаляем дополнение

                    # Декодирование с обработкой ошибок
                    try:
                        decrypted_value = decrypted_value.decode('utf-8', errors='replace')  # Заменяем некорректные байты
                    except Exception as e:
                        QtWidgets.QMessageBox.warning(None, "Предупреждение", f"Не удалось декодировать куки: {str(e)}")
                        continue

                    # Обновление значения куки в базе данных
                    conn = sqlite3.connect(self.current_browser)
                    cursor = conn.cursor()
                    if 'firefox' in self.current_browser.lower():
                        cursor.execute(
                            'UPDATE moz_cookies SET value = ? WHERE name = ? AND host = ?',
                            (decrypted_value, cookie_name, cookie_domain))
                    elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                        cursor.execute(
                            'UPDATE cookies SET encrypted_value = ? WHERE name = ? AND host_key = ?',
                            (decrypted_value, cookie_name, cookie_domain))
                    conn.commit()
                    conn.close()

                    # Обновление значения в таблице приложения
                    self.tableWidget.item(row, 1).setText(decrypted_value)  # Отображаем расшифрованное значение
                    for column in range(self.tableWidget.columnCount()):
                        self.tableWidget.item(row, column).setBackground(QtGui.QColor(68, 68, 68))

                self.textEdit.append(f"Зашифрованные куки восстановлены.")

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось расшифровать куки: {str(e)}")

            if not is_open:
                self.browser_open()
        except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось расшифровать куки: {str(e)}")

    def delete_cookies(self):
        try:
            self.browser_close()
            # Проверка, открыт ли браузер
            is_open = self.is_browser_open(os.path.basename(self.current_browser))
            if is_open:
                self.browser_close()  # Закрываем браузер, если он открыт
                is_open = False
            else:
                is_open = True
            selected_items = self.tableWidget.selectedItems()
            if not selected_items:
                QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пожалуйста, выберите куки для удаления.")
                return

            # Подтверждение удаления
            reply = QtWidgets.QMessageBox.question(None, "Подтверждение",
                                                   "Вы уверены, что хотите удалить выбранные куки?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.No:
                return

            # Проходим по выбранным кукам и удаляем их
            for item in selected_items:
                row = item.row()
                cookie_name = self.tableWidget.item(row, 0).text()  # Имя куки
                cookie_domain = self.tableWidget.item(row, 2).text()  # Домен куки

                try:
                    conn = sqlite3.connect(self.current_browser)
                    cursor = conn.cursor()

                    # Удаляем куки из базы данных
                    if 'firefox' in self.current_browser.lower():
                        cursor.execute(
                            'DELETE FROM moz_cookies WHERE name = ? AND host = ?',
                            (cookie_name, cookie_domain))
                    elif 'chrome' in self.current_browser.lower() or 'yandex' in self.current_browser.lower():
                        cursor.execute(
                            'DELETE FROM cookies WHERE name = ? AND host_key = ?',
                            (cookie_name, cookie_domain))

                    conn.commit()
                    conn.close()

                    # Удаляем куки из таблицы приложения
                    self.tableWidget.removeRow(row)
                    self.textEdit.append(f"Куки '{cookie_name}' были удалены.")

                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.critical(None, "Ошибка базы данных", f"Не удалось удалить куки: {str(e)}")

            if not is_open:
                self.browser_open()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось удалить куки: {str(e)}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
