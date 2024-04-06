from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建Chrome浏览器对象
browser = webdriver.Firefox()
# 加载指定的页面
browser.get('https://www.baidu.com/')
# 通过元素ID获取元素

kw_input=browser.find_element(By.ID,'kw')
kw_input.send_keys('Python')
# # 通过CSS选择器获取元素
# su_button = browser.find_element(By.CSS_SELECTOR, '#su')
# # 模拟用户点击行为
# su_button.click()
