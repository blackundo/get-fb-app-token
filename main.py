# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tooltokenpygui.ui'
#
# Ui creator by: PyQt5 UI code generator
#
# Author: Black Undo
#
# version: 1.0.0
# done: get token app with cookie, save result to file, etc...
# todo: get token app with token full, call api import token result to database server, update ui, etc...


import re
import threading
import time
import requests

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check_live_uid(uid):
    api = f"https://graph.facebook.com/{uid}/picture?redirect=false"
    response = requests.get(api)

    response_data = response.json()
    # print(response_data)
    # Kiểm tra xem 'data' có tồn tại trong JSON không
    if 'data' in response_data:
        # Kiểm tra xem 'width' có tồn tại trong 'data' không
        width = response_data['data'].get('width')

        if width is not None:
            return 'live'
        else:
            return 'die'
    else:
        return 'wrong'


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Baloo")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 60, 521, 211))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.input_width = QtWidgets.QSpinBox(self.groupBox)
        self.input_width.setObjectName("input_width")
        self.input_width.setRange(0, 9999)
        self.horizontalLayout.addWidget(self.input_width)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.input_height = QtWidgets.QSpinBox(self.groupBox)
        self.input_height.setObjectName("input_height")
        self.input_height.setRange(0, 9999)
        self.horizontalLayout_2.addWidget(self.input_height)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.input_user_agent = QtWidgets.QLineEdit(self.groupBox)
        self.input_user_agent.setObjectName("input_user_agent")
        self.horizontalLayout_3.addWidget(self.input_user_agent)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 270, 521, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.input_stt = QtWidgets.QSpinBox(self.groupBox_2)
        self.input_stt.setObjectName("input_stt")
        self.horizontalLayout_6.addWidget(self.input_stt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.input_listck = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.input_listck.setObjectName("input_listck")
        self.horizontalLayout_4.addWidget(self.input_listck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(240, 530, 131, 41))
        self.btn_run.setObjectName("btn_run")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event
        self.btn_run.clicked.connect(self.run_task_thread)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BLACK UNDO VIP"))
        self.label.setText(_translate("MainWindow", "TOOL TỰ LẤY TOKEN APP CM"))
        self.groupBox.setTitle(_translate("MainWindow", "trình duyệt"))
        self.label_2.setText(_translate("MainWindow", "chiều rộng"))
        self.label_3.setText(_translate("MainWindow", "chiều dài"))
        self.label_4.setText(_translate("MainWindow", "user agent"))
        self.input_user_agent.setText(_translate("MainWindow",
                                                 "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"))
        self.input_width.setValue(180)
        self.input_height.setValue(720)
        self.input_stt.setValue(2)
        self.groupBox_2.setTitle(_translate("MainWindow", "Auto"))
        self.label_5.setText(_translate("MainWindow", "Thứ tự cookie"))
        self.label_6.setText(_translate("MainWindow", "List clone"))
        self.btn_run.setText(_translate("MainWindow", "Chạy"))

    def run_task_thread(self):
        # threads = []

        thread = threading.Thread(target=self.loop_chay_trinh_duyet)
        thread.start()

    #     threads.append(thread)
    #
    # for thread in threads:
    #     thread.join()
    # print("Tất cả các luồng đã kết thúc.")

    def loop_chay_trinh_duyet(self):
        arr_info = str(self.input_listck.toPlainText()).strip().splitlines()
        count_live = 0
        count_die = 0
        file = open('results_token.txt', 'a')
        file.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]\n')
        file.close()
        fileErr = open('error.txt', 'a')
        fileErr.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]\n')
        fileErr.close()
        for i, info in enumerate(arr_info):
            info_list = info.split("|")
            uid = info_list[0]
            print(f'chạy lần {i + 1} - đang get của: {uid}')
            check_live = check_live_uid(uid)
            if check_live == 'die':
                print('die')
                count_die += 1
            elif check_live == 'live':
                print('live')
                count_live += 1
                # mo trinh duyet
                self.chay_trinh_duyet(info)
            else:
                print('wrong')

        print('Xong, Tổng số live: {} - die {}'.format(count_live, count_die))

    def chay_trinh_duyet(self, info):
        # i_listck = str(self.input_listck.toPlainText()).strip()
        i_width = int(self.input_width.text())
        i_height = int(self.input_height.text())
        i_stt = int(self.input_stt.text())
        # căắt ra mảng
        info_list = info.split("|")

        chrome_options = Options()
        # Thêm User Agent mới (đổi thành User Agent mong muốn)
        user_agent = str(self.input_user_agent.text()).strip()
        chrome_options.add_argument(f"user-agent={user_agent}")

        # Khởi tạo trình duyệt với các tùy chọn đã thêm
        driver = webdriver.Chrome(options=chrome_options)
        width = i_width
        height = i_height
        driver.set_window_size(width, height)
        time.sleep(2)
        # Mở Facebook
        driver.get("https://facebook.com")

        # Chuỗi cookie ban đầu
        # cookie_string = "wd=1115x1269; datr=fE-lZR8_2L_m7NzLAMXIg0rl; fr=0z7ge5GFvkY7gjerK.AWVIl6usZCveOzThYQZ-Ny7f_L8.BlpVGJ.EN.AAA.0.0.BlpVJb.AWU6-Sql_Ck; sb=W1KlZWHe4D2XeNmTEU3ReZbL; locale=id_ID; c_user=61555297305843; xs=2:vbkRG-rRtbb0Og:2:1705333346:-1:-1"

        # chọn thứ tự của cokie
        cookie_string = info_list[i_stt]

        # phần này nhập cookie vào tình duyệt 1 cái chứ k phải nhiều đâuuuu
        # Tách chuỗi theo dấu chấm phẩy và khoảng trắng để lấy từng cookie riêng biệt
        cookies_list = cookie_string.split(";")
        # Tạo danh sách các cookie từ thông tin bạn cung cấp
        cookies = []
        for cookie in cookies_list:
            name, value = cookie.split("=")
            cookies.append({'name': name.strip(), 'value': value.strip()})
        # Thêm từng cookie vào trình duyệt
        for cookie in cookies:
            driver.add_cookie(cookie)
        # log token
        # script = 'javascript:!function(){function o(e,o){var r=new XMLHttpRequest;r.open("GET",e,!0),r.setRequestHeader("Content-Type","text/plain;charset=UTF-8"),r.onreadystatechange=function(){this.readyState==XMLHttpRequest.DONE&&o(this.response)},r.send()}function r(e){var o=(e=JSON.parse(e)).session_cookies;if(null!=e.error_msg)return alert(e.error_msg),!1;o.forEach(function(e,o,r){var t="";Object.keys(e).forEach(function(o){"xs"==o&&(e[o]=encodeURIComponent(e[o])),t+=o+"="+e[o]+";"}),t=t.replace("name=","").replace(";value=","=").replace("httponly=true;",""),document.cookie=t}),location.href="https://fb.com"}o("https://graph.facebook.com/app?access_token="+e,function(t){if(null!=(t=JSON.parse(t)).error)return alert(t.error.message),!1;o("https://api.facebook.com/method/auth.getSessionforApp?access_token="+e+"&format=json&generate_session_cookies=1&new_app_id="+t.id,r)})}();'
        # driver.execute_script(f"""
        #     var e = "{cookie_string}";
        #     {script}
        # """)

        # Làm mới trang để áp dụng cookie
        driver.refresh()
        time.sleep(4)
        # Kiểm tra đã đăng nhập thành công chưa
        file = open('results_token.txt', 'a')
        file_err = open('error.txt', 'a')
        try:

            driver.get(
                "http://graph.facebook.com/oauth/authorize?client_id=737229396381522&scope=public_profile,user_friends,email,openid&redirect_uri=fbconnect://cct.com.moonactive.coinmaster&auth_type=rerequest&response_type=id_token,token,signed_request,graph_domain&response_type=token")

            time.sleep(3)
            #

            # Tìm phần tử cho trang cá nhân
            driver.find_element(By.NAME, "primary_consent_button").click()
            time.sleep(7)
            page = BeautifulSoup(driver.page_source, 'lxml')
            matches = re.search(r"EAAK[a-zA-Z0-9_-]+", str(page))
            if matches:
                # print(matches.group(0))
                file.write(matches.group(0) + '\n')
                # import leen serrver
                url = "https://spin.modundo.com/ajaxs/admin/import-clone.php?token=oqNBfFaEhdWiRCcvbuLgOsYKAGpkDrUXVxzmTtjPJlwZIQSMHny"

                payload = f'token=oqNBfFaEhdWiRCcvbuLgOsYKAGpkDrUXVxzmTtjePJlwZIQSMHny&tokenfb={matches.group(0)}&cost=800'
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                try:
                    response = requests.request("POST", url, verify=False, headers=headers, data=payload, timeout=20)
                    print(response.text)
                except requests.exceptions.Timeout:
                    print("Yêu cầu vượt quá thời gian chờ.")
                    file_err.write(f'{info}\n')
                except requests.exceptions.ConnectionError:
                    print("Yêu cầu vượt quá thời gian chờ.")
                    file_err.write(f'{info}\n')
                except requests.exceptions.RequestException as e:
                    print(f"Lỗi kết nối: {e}")
                    file_err.write(f'{info}\n')
                except Exception as e:
                    print(f"Lỗi kết nối: {e}")
                    file_err.write(f'{info}\n')
            else:
                file_err.write(f'{info}\n')
                print("Không tìm thấy phần cần trích xuất!")


        except NoSuchElementException:
            file_err.write(f'{info}\n')
            print("Đăng nhập thất bại! cookie hếthan or chưa đủ 60p")

        # Đóng trình duyệt
        driver.quit()
        file.close()
        file_err.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
