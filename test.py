# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get('https://caigou.jcebid.com/test/')
# time.sleep(2)
# xf = driver.find_element_by_xpath('//*[@id="loginIframe"]')
# driver.switch_to_frame(xf)
# driver.find_element_by_id('LAY-user-login-username').send_keys('cszbdl')  # 输入账号
# driver.find_element_by_id('LAY-user-login-password').send_keys('123456')  # 输入密码
# captchaCode=input("请输入验证码：")
# driver.find_element_by_id('captchaCode').send_keys(captchaCode)  # 验证码
# driver.find_element_by_xpath('//*[@id="LoginPage"]/div/div/div[2]/div/div[1]/div[4]/button').click()  # 点击登录
#
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/a/cite').click()  # 点击项目管理
# driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/dl/dd[1]/a').click()  # 点击项目
# time.sleep(3)
# driver.switch_to.frame(1)
# time.sleep(3)
# # 点击进入按钮
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/div/a").click()
#
# driver.switch_to.default_content()
#
# xf1 = driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[3]/iframe')
# driver.switch_to.frame(xf1)
# time.sleep(2)
# xf2 = driver.find_element_by_xpath('//*[@id="panelMenuBodys"]/div[1]/iframe')
# driver.switch_to.frame(xf2)
# time.sleep(3)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/span/button[1]').click()

import win32gui
import win32con


def upload(filePath, browser_type="chrome"):
    '''
    通过pywin32模块实现文件上传的操作
    :param filePath: 文件的绝对路径
    :param browser_type: 浏览器类型（默认值为chrome）
    :return:
    '''
    # 找元素
    # 一级窗口"#32770","打开"
    dialog = win32gui.FindWindow("#32770", title)
    # 向下传递
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)   # 三级
    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

    # 输入文件的绝对路径，点击“打开”按钮
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

upload(r'C:\Users\hp\Desktop\pdf测试数据\投标文件测试数据\不分标段(招标文件).pdf')