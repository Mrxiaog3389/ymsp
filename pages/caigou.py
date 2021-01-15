from common.Driver import Driver
import time,random,string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class testzh(Driver):
    def open(self,url):
        self.driver.get(url)

    def Login(self,username,password):#首页登录
        time.sleep(3)
        xf = self.driver.find_element_by_xpath('//*[@id="loginIframe"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_id('LAY-user-login-username').send_keys(username)  # 输入账号
        self.driver.find_element_by_id('LAY-user-login-password').send_keys(password)  # 输入密码
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="LoginPage"]/div/div/div[2]/div/div[1]/div[4]/button').click()  # 点击登录
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[8]/a').click()
        self.driver.find_element_by_xpath('//*[@id="LeftMenus"]/ul/li[8]/dl/dd[2]/a').click()
        time.sleep(2)

        a=['岳红','刘南缨']
        for i in range(len(a)):
            xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
            self.driver.switch_to_frame(xf)
            time.sleep(2)

            self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/a").click()  # 点击新增按钮
            self.driver.switch_to.default_content()
            time.sleep(2)
            xf = self.driver.find_element_by_xpath(f'//*[@id="layui-layer-iframe{i+1}"]')
            self.driver.switch_to_frame(xf)
            self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div[1]/div/div/input[1]').send_keys(a[i])
            self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div[2]/div/div/input').send_keys(a[i])
            self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div[3]/div/div/input').send_keys(a[i])

            self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div[5]/div/div/input').send_keys('18483663883')
            self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div[6]/div/div/input').send_keys('18483663883@163.com')
            self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div[7]/div[1]/div/input').send_keys('123456')
            self.driver.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/div[7]/div[2]/div/div/input').send_keys('123456')

            self.driver.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[4]/td[1]/div/div/i").click()

            self.driver.switch_to.default_content()
            self.driver.find_element_by_xpath(f'//*[@id="layui-layer{i+1}"]/div[3]/a[1]').click()





test=testzh()
test.open('http://ryplan.jcebid.com/sys/user/login.html')
test.Login('FZB550000','123456')
# test.create_bidding_project()