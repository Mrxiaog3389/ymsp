from common.Driver import Driver
import time,random,string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import win32gui
import win32con

class testzh(Driver):
    def open(self,url):
        self.driver.get(url)

    def upload(self,filePath, browser_type="chrome"):
        '''
        通过pywin32模块实现文件上传的操作
        :param filePath: 文件的绝对路径
        :param browser_type: 浏览器类型（默认值为chrome）
        :return:
        '''
        if browser_type.lower() == "chrome":
            title = "打开"
        elif browser_type.lower() == "firefox":
            title = "文件上传"
        elif browser_type.lower() == "ie":
            title = "选择要加载的文件"
        else:
            title = ""  # 这里根据其它不同浏览器类型来修改

        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

        # 输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

    def Login(self,username,password):#首页登录
        time.sleep(2)
        xf = self.driver.find_element_by_xpath('//*[@id="loginIframe"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_id('LAY-user-login-username').send_keys(username)  # 输入账号
        self.driver.find_element_by_id('LAY-user-login-password').send_keys(password)  # 输入密码
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="LoginPage"]/div/div/div[2]/div/div[1]/div[4]/button').click()  # 点击登录

    def create_project(self,num):#创建项目
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/a/cite').click()   # 点击项目管理
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/dl/dd[1]/a').click()  # 点击项目
        time.sleep(3)
        self.driver.switch_to.frame(1)
        time.sleep(3)
        self.driver.find_elements_by_xpath("//button[text()='新增']")[-1].click()    # 点击新增按钮
        self.driver.switch_to.default_content()
        time.sleep(3)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf)  # str(random.randint(1,5))
        time.sleep(6)
        # 选择采购方式
        self.driver.find_element_by_xpath(f"/html/body/div/form/div[1]/div[2]/div/div[1]/div/div[{str(num)}]/i").click()
        # 采购单位
        ele6 = self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[2]/div[1]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele6).perform()
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[2]/div[1]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[2]/div[1]/div/div/dl/dd[4]').click()
        # 联系人(代理)
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[4]/div[1]/div/input').send_keys('山西正大方工程项目管理有限公司')
        # 联系方式(代理)
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[4]/div[2]/div/input').send_keys('18483663883')
        # 项目编号
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[5]/div[1]/div/input').send_keys('155151515414')
        # 项目所属地区
        self.driver.find_element_by_xpath('//*[@id="regionName"]').click()

        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys('成都市',Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="node_name"]').click()
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()
        # 项目名称
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[6]/div/input').send_keys('成都测试'+time.strftime('%d%m%Y')+str(num))
        # 项目分类
        ele7 = self.driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[2]/div/div[7]/div/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele7).perform()
        self.driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[2]/div/div[7]/div/div/div/div/input').click()
        self.driver.find_element_by_xpath(f'/html/body/div/form/div[1]/div[2]/div/div[7]/div/div/div/dl/dd[{str(random.randint(2,5))}]').click()
        # 项目概况
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[8]/div/textarea').send_keys('成都测试' + time.strftime('%d%m%Y'))
        # 资金来源及落实情况
        self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div/div[9]/div/textarea').send_keys('成都测试' + time.strftime('%d%m%Y'))
        # 点击保存按钮
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()
        # 点击确定按钮
        time.sleep(10)
        print(self.driver.find_element_by_xpath('//*[@id="layui-layer4"]/div[2]').text)
        self.driver.find_element_by_xpath('//*[@id="layui-layer4"]/div[3]/a').click()

    def common_project(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/a/cite').click()  # 点击项目管理
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/dl/dd[1]/a').click()  # 点击项目
        time.sleep(3)
        self.driver.switch_to.frame(1)
        time.sleep(3)
        # 点击进入按钮
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/div/a").click()
        self.driver.switch_to.default_content()
        xf1 = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[3]/iframe')
        self.driver.switch_to.frame(xf1)
        time.sleep(2)
        xf2 = self.driver.find_element_by_xpath('//*[@id="panelMenuBodys"]/div[1]/iframe')
        self.driver.switch_to.frame(xf2)
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/span/button[1]').click()

        self.driver.switch_to.default_content()
        time.sleep(3)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf)
        # 标段(包)名称
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div/div/input[1]').send_keys('一期标段')
        # 标段(包)合同估算价
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[2]/div[1]/input').send_keys(800000)
        # 采购单位
        ele1 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[1]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele1).perform()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[1]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div[1]/div/div/dl/dd[2]').click()
        # 是否缴纳保证金
        ele2 = self.driver.find_element_by_xpath('//*[@id="parent"]/div/div/input')
        ActionChains(self.driver).move_to_element(ele2).perform()
        self.driver.find_element_by_xpath('//*[@id="parent"]/div/div/input').click()
        self.driver.find_element_by_xpath('//*[@id="parent"]/div/dl/dd[2]').click()
        # 收取采购文件费
        ele3 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/div[1]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele3).perform()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/div[1]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/div[1]/div/div/dl/dd[3]').click()
        # 评标流程
        ele4 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[6]/div[2]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele4).perform()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[6]/div[2]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[6]/div[2]/div/div/dl/dd[2]').click()
        # 标段(包)内容
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[8]/div/textarea').send_keys("一期标段")
        # 点击保存按钮
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()
        # 点击确定按钮
        print(self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[2]').text)
        self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()

    def increace_file(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/a/cite').click()  # 点击项目管理
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[1]/dl/dd[1]/a').click()  # 点击项目
        time.sleep(3)
        self.driver.switch_to.frame(1)
        time.sleep(3)
        # 点击进入按钮
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/div/a").click()
        self.driver.switch_to.default_content()
        xf1 = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[3]/iframe')
        self.driver.switch_to.frame(xf1)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='panelMenus']/li[3]").click()
        xf2 = self.driver.find_element_by_xpath('//*[@id="panelMenuBodys"]/div[3]/iframe')
        self.driver.switch_to.frame(xf2)
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/span/button[1]').click()
        self.driver.switch_to.default_content()
        time.sleep(3)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf)
        # 采购文件名称
        self.driver.find_element_by_xpath('//*[@id="documentName"]').send_keys('招标文件')
        # 关联标段（包）
        self.driver.find_element_by_xpath('//*[@id="sectionSelect"]/div/i').click()
        # 点击保存按钮
        self.driver.find_element_by_xpath('//*[@id="btnSave"]').click()
        # 点击确定按钮
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()
        time.sleep(2)
        xf4 = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe4"]')
        self.driver.switch_to_frame(xf4)
        # file_path=r'C:\Users\hp\Desktop\pdf测试数据\投标文件测试数据\不分标段(招标文件).pdf'
        # self.driver.find_element_by_xpath('//*[@id="uploadBiddingFile"]/i').click()
        # self.upload(file_path)
        self.driver.find_element_by_xpath('//*[@id="info"]').click()
        xf5 = self.driver.find_element_by_xpath('//*[@id="infoContent"]')
        self.driver.switch_to_frame(xf5)
        ele2 = self.driver.find_element_by_xpath('//*[@id="info-basic"]/div[5]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele2).perform()
        self.driver.find_element_by_xpath('//*[@id="info-basic"]/div[5]/div/div/div/input').click()
        self.driver.find_element_by_xpath('//*[@id="info-basic"]/div[5]/div/div/dl/dd[2]').click()

        self.driver.find_element_by_xpath('//*[@id="info-basic"]/div[10]/button').click()

        time.sleep(3)
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath('//*[@id="showReviewItems"]').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="singleLetterItemsMenu"]/li[2]').click()
        # self.driver.find_element_by_xpath('//*[@id="tree_1612540855024_2_span"]').click()
        self.driver.find_element_by_xpath('//*[@id="showSummarySheetForBidOpening"]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="showCatalogForTenderFile"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="menuTree-light"]/div/div[1]/div/button[1]').click()



    def logout(self):
        time.sleep(3)
        exit_1 = self.driver.find_element_by_xpath('//*[@id="userProfile"]/a/span')
        ActionChains(self.driver).move_to_element(exit_1).perform()
        self.driver.find_element_by_xpath('//*[@id="logout"]/a').click()

    def seal(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="LAY_app"]/div/div[1]/ul[2]/li[1]/a/i').click()
        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
        self.driver.switch_to_frame(xf)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="LAY-app-message"]/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[8]/div/a[1]').click()


#https://caigou.jcebid.com/test/src/views/sys/user/login.html   http://ysdfzb.jcebid.com/nobid_ui/views/sys/user/login.html
test=testzh()
test.open('https://caigou.jcebid.com/test/src/views/sys/user/login.html')
# for i in range(1,5):
test.Login('cszbdl','123456')
test.increace_file()
# test.create_project(4)
# test.logout()

