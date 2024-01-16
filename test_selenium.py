import time

import bs4
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re


chrome_options = Options()
# Thêm User Agent mới (đổi thành User Agent mong muốn)
user_agent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

# Khởi tạo trình duyệt với các tùy chọn đã thêm
driver = webdriver.Chrome(options=chrome_options)
width = 180
height = 750
driver.set_window_size(width, height)
time.sleep(4)
# Mở Facebook
driver.get("https://facebook.com")

# Chuỗi cookie ban đầu
# cookie_string = "wd=1115x1269; datr=fE-lZR8_2L_m7NzLAMXIg0rl; fr=0z7ge5GFvkY7gjerK.AWVIl6usZCveOzThYQZ-Ny7f_L8.BlpVGJ.EN.AAA.0.0.BlpVJb.AWU6-Sql_Ck; sb=W1KlZWHe4D2XeNmTEU3ReZbL; locale=id_ID; c_user=61555297305843; xs=2:vbkRG-rRtbb0Og:2:1705333346:-1:-1"

info = "61555611835058|nellmmiujimenez495|EAAAAUaZA8jlABOZBIOGupkNwXmIcAj1ei6ZA83bszNPLQZBvQwjpzGaZCBIViJfsWdctZAtFZBV0Dbs5fCgskjpZCJux1CoeCUg7hPiUkOpoGrKblmMWc8Xge8iY6z7PcihXZCqXoWVbUwRkP0GbF6JY4MmehvIxZBrtZARnAZC7Xi9N4cDW2X4mpe9ylmNt5qUFvtZA8VKrv1nhZAZAAZDZD|c_user=61555611835058;xs=27:adIYvdcr-9MMDw:2:1705268232:-1:-1;fr=09Js9FPTfZwB8uFAP.AWVZA_wYZvYw9XNyY5gT2ORJURo.BlpFQI.Jz.AAA.0.0.BlpFQI.AWUzSRRsgUE;datr=81OkZZYWL5BPHxhPRfRzxdW1;||Nell_Jimenez|F|31/07/1990|01/15/2024_04:36:17|CO"

info_list = info.split("|")
# chọn thứ tự của cokie
cookie_string = info_list[2]
print(cookie_string)



# phần này nhập cookie vào tình duyệt 1 cái chứ k phải nhiều đâuuuu
# Tách chuỗi theo dấu chấm phẩy và khoảng trắng để lấy từng cookie riêng biệt
cookies_list = cookie_string.split("; ")
# Tạo danh sách các cookie từ thông tin bạn cung cấp
cookies = []
for cookie in cookies_list:
    try:
        name, value = cookie.split("=")
        cookies.append({'name': name, 'value': value})
    except ValueError:
        pass
# Thêm từng cookie vào trình duyệt
for cookie in cookies:
    driver.add_cookie(cookie)





# Làm mới trang để áp dụng cookie
driver.refresh()
time.sleep(5)
# Kiểm tra đã đăng nhập thành công chưa
try:
    driver.get("http://graph.facebook.com/oauth/authorize?client_id=737229396381522&scope=public_profile,user_friends,email,openid&redirect_uri=fbconnect://cct.com.moonactive.coinmaster&auth_type=rerequest&response_type=id_token,token,signed_request,graph_domain&response_type=token")

    time.sleep(3)
    #

    # Tìm phần tử cho trang cá nhân
    driver.find_element(By.NAME, "primary_consent_button").click()
    time.sleep(2)
    page = bs4.BeautifulSoup(driver.page_source,'lxml')
    matches = re.search(r"EAAK[a-zA-Z0-9_-]+", str(page))

    if matches:
        print(matches.group(0))
    else:
        print("Không tìm thấy phần cần trích xuất!")
    time.sleep(50)

    # print(check_mail)
    time.sleep(20)
    print("Đăng nhập thành công!")
except NoSuchElementException:
    print("Đăng nhập thất bại!")

# Đóng trình duyệt
driver.quit()
