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

# import win32gui
# import win32con
#
#
# def upload(filePath, browser_type="chrome"):
#     '''
#     通过pywin32模块实现文件上传的操作
#     :param filePath: 文件的绝对路径
#     :param browser_type: 浏览器类型（默认值为chrome）
#     :return:
#     '''
#     # 找元素
#     # 一级窗口"#32770","打开"
#     dialog = win32gui.FindWindow("#32770", title)
#     # 向下传递
#     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
#     comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)   # 三级
#     # 编辑按钮
#     edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
#     # 打开按钮
#     button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
#
#     # 输入文件的绝对路径，点击“打开”按钮
#     win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
#     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
#
# upload(r'C:\Users\hp\Desktop\pdf测试数据\投标文件测试数据\不分标段(招标文件).pdf')
from selenium import webdriver
import unittest
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动ie浏览器
        self.driver = webdriver.Ie(executable_path = "g:\\IEDriverServer")

    def test_uploadFileBySendKeys(self):
        url = "http://127.0.0.1/test_upload_file.html"
        # 访问自定义网页
        self.driver.get(url)
        try:
            # 创建一个显示等待对象
            wait = WebDriverWait(self.driver, 10, 0.2)
            # 显示等待判断被测试页面上的上传文件按钮是否处于可被点击状态
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException as e:
            # 捕获TimeoutException异常
            print (traceback.print_exc())
        except NoSuchElementException as e:
            # 捕获NoSuchElementException异常
            print (traceback.print_exc())
        except Exception as e:
            # 捕获其他异常
            print (traceback.print_exc())
        else:
            # 查找页面上ID属性值为“file”的文件上传框
            fileBox = self.driver.find_element_by_id("file")
            # 在文件上传框的路径框里输入要上传的文件路径“g:\\test.txt”
            # send_keys之后会默认关闭文件选择弹窗
            fileBox.send_keys("g:\\test.txt")
            # 暂停查看上传的文件
            time.sleep(4)
            # 找到页面上ID属性值为“filesubmit”的文件提交按钮对象
            fileSubmitButton = self.driver.find_element_by_id("filesubmit")
            # 单击提交按钮，完成文件上传操作
            fileSubmitButton.click()
            # 因为文件上传需要时间，所以这里可以添加显示等待场景，
            # 判断文件上传成功后，页面是否跳转到文件上传成功的页面。
            # 通过EC.title_is()方法判断跳转后的页面的Title
            # 值是否符合期望，如果匹配将继续执行后续代码
            #wait.until(EC.title_is(u"文件上传成功"))

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()