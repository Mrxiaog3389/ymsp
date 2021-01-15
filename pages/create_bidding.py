from common.Driver import Driver
import time,random,string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class testzh(Driver):
    def open(self,url):
        self.driver.get(url)

    def Login(self,username,password):#首页登录
        self.driver.find_element_by_id('LAY-user-login-username').send_keys(username)  # 输入账号
        self.driver.find_element_by_id('LAY-user-login-password').send_keys(password)  # 输入密码
        time.sleep(2)
        self.driver.find_element_by_id('submit').click()  # 点击登录
        time.sleep(2)

    def create_project(self):#创建项目
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[1]/a').click()   # 点击项目管理
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[1]/dl/dd[1]').click()  # 点击项目
        time.sleep(2)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.driver.find_elements_by_xpath("//button[text()='新增']")[-1].click()    # 点击新增按钮
        self.driver.switch_to.default_content()
        time.sleep(2)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe2"]')
        self.driver.switch_to_frame(xf)
        # 选择招标人
        ele6 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele6).perform()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/dl/dd[2]').click()
        time.sleep(2)
        # 项目审批时间
        ele5 = self.driver.find_element_by_id('approvalDate')
        ActionChains(self.driver).move_to_element(ele5).click(ele5).perform()
        self.driver.find_element_by_xpath('//*[@id="approvalDate"]').click()
        self.driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[2]/div/span[2]').click()
        time.sleep(2)
        # 输入项目名称
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[2]/div/input').send_keys('成都测试'+time.strftime('%d%m%Y'))
        # 输入项目地址
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys('四川省成都市')
        # 输入项目行政划分
        self.driver.find_element_by_xpath('//*[@id="regionName"]').click()

        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys('龙岩市',Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="node_name"]').click()
        self.driver.switch_to.default_content()
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe2"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()

        # 联系人（招标人）
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[5]/div[1]/div/input').send_keys('山西正大方工程项目管理有限公司')
        # 输入法人单位名称
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[4]/div[2]/div/input').send_keys('山西正大方工程项目管理有限公司')
        # 输入联系方式（招标人）
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[5]/div[2]/div/input').send_keys('0813-4696132')
        # 输入项目行业类型
        self.driver.find_element_by_xpath('//*[@id="industryTypesName"]').click()

        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe2"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('//*[@id="address"]').send_keys('专业技术服务业', Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="node_name"]').click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe2"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()
        # 投资金额
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[7]/div[1]/div/div[1]/input').send_keys(70)
        # 项目批文名称
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[7]/div[2]/div/input').send_keys('成都测试'+time.strftime('%d%m%Y'))
        # 招标方案核准号
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[8]/div[1]/div/input').send_keys([random.choice(string.digits) for i in range(20)])
        # 项目审批单位
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[9]/div[1]/div/input').send_keys('招标办')
        # 批文号
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[9]/div[2]/div/input').send_keys([random.choice(string.digits) for i in range(20)])

        # 资金来源
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[13]/div/textarea').send_keys('国有资金')
        # 项目规模
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[14]/div/textarea').send_keys('包含一期标段、二期标段')
        # 点击保存按钮
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()
        # 点击确定按钮
        self.driver.find_element_by_xpath('//*[@id="layui-layer4"]/div[3]/a').click()

    def create_bidding_project(self):#创建招标项目
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[1]/a').click()  # 点击项目管理
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[1]/dl/dd[2]').click() #点击招标项目
        time.sleep(2)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        self.driver.find_elements_by_xpath("//button[text()='新增']")[-1].click()  # 点击新增按钮
        self.driver.switch_to.default_content()

        time.sleep(2)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe4"]')
        self.driver.switch_to_frame(xf)
        # 选择招标人
        ele6 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele6).perform()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/div/input').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div[1]/div/div/dl/dd[2]').click()



    def logout(self):

        exit_1 = self.driver.find_element_by_xpath('//*[@id="LAY_app"]/div/div[1]/ul[2]/li[7]/a/span')
        ActionChains(self.driver).move_to_element(exit_1).perform()
        self.driver.find_element_by_xpath('//*[@id="logout"]/a').click()


test=testzh()
test.open('http://testzh.jcebid.com/sys/user/login.html')
test.Login('zhangjinli','123456')
test.create_bidding_project()
# test.create_project()
# test.logout()