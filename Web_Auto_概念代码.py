#_*_conding:utf-8_*_
#@Time    :2020/3/215:36
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


"""
窗口切换

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("柠檬班")

driver.find_element_by_id("su").click()

loc = (By.XPATH,'//a[text()="_腾讯课堂"]')

WebDriverWait(driver,20,1).until(EC.visibility_of_element_located(loc))

driver.find_element(*loc).click()

wins =driver.window_handles
print("当前的所有句柄为：",wins)

wins1 = driver.current_window_handle
print("当前的句柄：",wins1)

driver.switch_to.window(wins[1])



下拉框操作的两种方式select/option 和其他方式
select/option
    引入 from selenium.webdriver.support.ui import Select
    创建select类
    根据select类的文本内容、索引、Value值来选择
通过元素定位点点点来选择
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
loc = (By.XPATH,'//div[@id="u1"]//a[@class="pf"]')
driver.find_element(*loc).click()
time.sleep(1)
loc_1 = (By.XPATH,'//a[text()="高级搜索"]')
WebDriverWait(driver,10,1).until(EC.visibility_of_element_located(loc_1))
driver.find_element(*loc_1).click()
time.sleep(1)
select = Select(driver.find_element_by_name("ft"))
#根据索引来选择下拉框
# select.select_by_index(2)
#根据option的value值来选择
#select.select_by_value("ppt")
#根据文本内容来选择
select.deselect_by_visible_text("所有格式")
time.sleep(5)
driver.quit()


#js滚动条处理  execute_script 用来执行js语句
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()

loc_2 = (By.XPATH,'//a[text()="_百度图片"]')
#等待元素可见
WebDriverWait(driver,10,1).until(EC.presence_of_element_located(loc_2))

#找到元素
loc_3 = driver.find_element_by_xpath('//a[text()="_百度图片"]')
#顶端与当前窗口的顶部对齐（执行js语句）
# driver.execute_script("arguments[0].scrollIntoView();",loc_3)
#顶端与当前窗口的底部对齐
driver.execute_script("arguments[0].scrollIntoView(false);",loc_3)
time.sleep(2)
driver.quit()
"""

#js处理日历控件
driver = webdriver.Chrome()
driver.get("http://www.12306.cn/index/")
driver.maximize_window()

set_out = "var a = document.getElementById('fromStationText');a.value='北京';"
set_out_1 = "var b = document.getElementById('fromStation');b.value='BJP';"
driver.execute_script(f"{set_out};{set_out_1}")
time.sleep(2)
arrived = "var c = document.getElementById('toStationText');c.value= '兰州';"
arrived_1 = "var d = document.getElementById('toStation');d.value= 'LZP';"
driver.execute_script(f"{arrived};{arrived_1}")
time.sleep(2)
date = "var e = document.getElementById('train_date');e.readOnly=false;e.value='2020-01-21';"
driver.execute_script(date)

loc = (By.ID,'search_one')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
time.sleep(0.5)
driver.find_element(*loc).click()

time.sleep(5)

driver.quit()





