from common.Driver import Driver
import time,random

class bid_opening(Driver):
    def open(self,url):
        self.driver.get(url)

    def Login(self,username,password):#首页登录
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_id('submit').click()

    def Sign_in(self):

        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/ul/li[4]/a/i').click()
        time.sleep(2)
        list=self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[2]/table/tbody/tr')
        number=[]
        # for i in list:
        #     # print(i.text.split('\n')){random.choice(number)}
        #     number.append(i.get_attribute('data-index'))
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/table/tbody/tr[4]/td[6]/div/a').click()
        # time.sleep(3)
        # xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe3"]')
        # self.driver.switch_to_frame(xf)
        # if self.driver.find_element_by_xpath('//*[@id="sign"]').text != '已签到':
        #     self.driver.find_element_by_xpath('//*[@id="sign"]').click()
        #     self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[2]/div/form/div[3]/div/input').send_keys(510302199506190017)
        #     self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[2]/div/form/div[4]/div/input').send_keys('测试')
        #     self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a[1]').click()
        #     print(self.driver.switch_to.alert.text)
        #     self.driver.switch_to.default_content()
        # else:
        #     self.driver.switch_to.default_content()
        # self.driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').click()

    def opening(self):

        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/ul/li[4]/a/i').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/ul/li[4]/a/i').click()
        project_name = input("请输入项目名称")
        self.driver.find_element_by_xpath('//*[@id="projectInstanceName"]').send_keys(project_name)
        self.driver.find_element_by_xpath('//*[@id="search-form"]/div/button').click()
        list=self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[2]/table/tbody/tr')
        for i in range(len(list)):
           if list[i].text.split('\n')[3] == '待开标':
               time.sleep(2)
               self.driver.find_element_by_xpath(f'//*[@id="content"]/div[2]/div[1]/div[2]/table/tbody/tr[{i+1}]/td[6]/div/a').click()
               break
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[2]/table/tbody/tr[9]/td[6]/div/a').click()
        time.sleep(4)
        # self.driver.find_element_by_xpath('//*[@id="optBtnGroup"]/button[1]').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="layui-layer8"]/div[3]/a[1]').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="layui-layer10"]/div[3]/a').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="startFirstDecrypt"]').click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[2]/div/div[3]/div/div/div/div/form/div/div/button[2]').click()
        # number=3
        # self.driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[2]/div/form/div[1]/div[1]/input').send_keys(1)
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="layui-layer6"]/div[2]/div/form/div[2]/div/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="optBtnGroup"]/button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layui-layer6"]/div[3]/a[1]').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').click()

    def logoout(self):
        self.driver.find_element_by_xpath('//*[@id="logout"]/span').click()

test=bid_opening()
test.open('http://testkb.jcebid.com/login')
test.Login('zhangjinli', '123456')
test.opening()
    # test.logoout()
