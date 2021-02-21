from common.Driver import Driver
import time,random,pytesseract
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

class Oalogin(Driver):
    def open(self):
        self.driver.get('http://ymsp.jcebid.com/login.html')  # 打开oa主页

    def Login(self,name,password):#oa首页登录
        self.driver.find_element_by_name('loginName').send_keys(name) #输入用户名
        self.driver.find_element_by_name('password').send_keys(password) #输入密码
        time.sleep(6)
        # self.driver.save_screenshot("scr_img.png")
        # time.sleep(2)
        # code_ele = self.driver.find_element_by_id("LAY-user-get-vercode")
        # time.sleep(2)
        # x0 = code_ele.location["x"]
        # y0 = code_ele.location["y"]
        # x1 = code_ele.size["width"] + x0
        # y1 = code_ele.size["height"] + y0
        # img = Image.open("scr_img.png")
        # image = img.crop((x0, y0, x1, y1))  # 左、上、右、下
        # image.save("code_img.png")  # 将验证码图片保存为code_img.png
        # qq = Image.open('code_img.png')
        # text = pytesseract.image_to_string(qq).strip()  # 使用image_to_string识别验证码
        # print(text)
        # if '-' in text:
        #     list = text.split('-')
        #     list1 = list[1].split('=')
        #     a = int(list[0]) - int(list1[0])
        # else:
        #     list = text.split('+')
        #     list1 = list[1].split('=')
        #     a = int(list[0]) - int(list1[0])
        # self.driver.find_element_by_name('vercode').send_keys(a)
        time.sleep(1)
        self.driver.find_element_by_id('LAY-user-login-submit').click() #点击登录
        time.sleep(1)

    def logout(self):
        time.sleep(5)
        exit_1 = self.driver.find_element_by_xpath('//*[@id="userProfile"]/a/span')
        ActionChains(self.driver).move_to_element(exit_1).perform()
        self.driver.find_element_by_xpath('//*[@id="logout"]/a').click()

    def increase_Project(self,num):
        # self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[7]/a/cite').click()
        # self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[7]/dl/dd[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/a/span').click()
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/dl/dd[1]/a').click()
        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]/a[1]').click()
        time.sleep(1)

        xf1 = self.driver.find_element_by_xpath(f'//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf1)

        # 输入项目名称
        self.driver.find_element_by_id('projectName').send_keys('测试V1.1.6.2'+str(num))
        # 选择组织类型
        ele = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div')
        ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        self.driver.find_element_by_xpath(f'/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div/dl/dd[{str(num+1)}]').click()
        # 选择资金来源
        ele1 = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div/input')
        ActionChains(self.driver).move_to_element(ele1).click(ele1).perform()
        self.driver.find_element_by_xpath(f'/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div/div/dl/dd[{str(num+1)}]').click()
        # 输入单项合同估算价(万元)
        self.driver.find_element_by_id('contractPrice').send_keys(200)
        # 选择组织方式
        ele2 = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[4]/div[1]/div/div')
        ActionChains(self.driver).move_to_element(ele2).click(ele2).perform()
        a=random.randint(2,7)
        if a==2 or a==3:
            self.driver.find_element_by_xpath(f'/html/body/div/div/div[1]/div[2]/div[4]/div[1]/div/div/dl/dd[{a}]').click()
            time.sleep(1)
            ele_fangshi = self.driver.find_element_by_xpath('//*[@id="invitationModeDiv"]/div/div')
            ActionChains(self.driver).move_to_element(ele2).click(ele_fangshi).perform()
            self.driver.find_element_by_xpath(f'//*[@id="invitationModeDiv"]/div/div/dl/dd[{a}]').click()

        else:
            self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[4]/div[1]/div/div/dl/dd[4]').click()

        # 输入年度资金计划(万元)
        self.driver.find_element_by_id('fundingPlan').send_keys(500)
        # # 选择组织单位
        ele3 = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[5]/div[2]/div/div')
        ActionChains(self.driver).move_to_element(ele3).click(ele3).perform()
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[5]/div[2]/div/div/dl/dd[2]').click()
        # 选择评审时间
        ele5 = self.driver.find_element_by_id('startWorkDate')
        ActionChains(self.driver).move_to_element(ele5).click(ele5).perform()
        self.driver.find_element_by_xpath('//*[@class="layui-laydate"]/div[2]/div/span[2]').click()
        # 输入招标内容
        self.driver.find_element_by_id('biddingContent').send_keys('测试测试')
        #点击保存按钮
        self.driver.find_element_by_xpath('//*[@id="next"]').click()

        ele4 = self.driver.find_element_by_xpath('// *[ @ class = "layui-layer layui-layer-dialog"]')
        ActionChains(self.driver).move_to_element(ele4).perform()
        self.driver.find_element_by_xpath('//*[@ class = "layui-layer layui-layer-dialog"]/div[3]/a[1]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@ class = "layui-layer layui-layer-dialog"]/div[3]/a').click()
        self.driver.switch_to.default_content()

    def Generate_project_filing(self):
        time.sleep(3)
        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[18]/div/a[2]').click()
        ele6 = self.driver.find_element_by_xpath('// *[ @ class = "layui-layer layui-layer-dialog"]')
        ActionChains(self.driver).move_to_element(ele6).perform()
        self.driver.find_element_by_xpath('//*[@ class = "layui-layer layui-layer-dialog"]/div[3]/a[1]').click()
        self.driver.switch_to.default_content()

    def project_filing(self,num):
        ac = ActionChains(self.driver)
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/dl/dd[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="LAY_app_tabsheader"]/li[2]/i').click()

        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
        self.driver.switch_to_frame(xf)
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[18]/div/a[2]').click()

        time.sleep(1)

        xf1 = self.driver.find_element_by_xpath(f'//*[@id="layui-layer-iframe{str(num)}"]')
        self.driver.switch_to_frame(xf1)

        # 滑动滚动条至中间位置
        js = "var q=document.documentElement.scrollTop=50"
        self.driver.execute_script(js)
        time.sleep(3)

        # 选择审批流程
        ele = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[8]/div[1]/div[1]/div')
        ac.move_to_element(ele) #悬浮
        ac.click(ele) #点击
        ac.perform()
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[8]/div[1]/div[1]/div/dl/dd[2]').click()

        self.driver.find_element_by_xpath('//*[@id="next"]').click()
        self.driver.find_element_by_xpath('//*[@class="layui-layer layui-layer-dialog"]/div[3]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="attachmentFrom"]/div/div/div/button[2]').click()

        ele6 = self.driver.find_element_by_xpath('// *[ @ class = "layui-layer layui-layer-dialog"]')
        ActionChains(self.driver).move_to_element(ele6).perform()
        self.driver.find_element_by_xpath('//*[@ class = "layui-layer layui-layer-dialog"]/div[3]/a[1]').click()
        self.driver.switch_to.default_content()
    # 审批
    def to_examine(self,username,password):
        self.Login(username, password)
        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div/iframe')
        self.driver.switch_to_frame(xf)
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/table/tbody/tr/td[7]/div/a').click()
        time.sleep(2)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe2"]')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('//*[@id="next"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        ele6 = self.driver.find_element_by_xpath('// *[ @ class = "layui-layer layui-layer-dialog"]')
        ActionChains(self.driver).move_to_element(ele6).perform()
        self.driver.find_element_by_xpath('//*[@ class = "layui-layer layui-layer-dialog"]/div[3]/a[1]').click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.logout()
    # 盖章
    def seal(self,username,password):
        self.Login(username, password)
        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div/iframe')
        self.driver.switch_to_frame(xf)
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/table/tbody/tr/td[7]/div/a').click()
        time.sleep(2)
        xf = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe2"]')
        self.driver.switch_to_frame(xf)
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        ele6 = self.driver.find_element_by_xpath('// *[ @ class = "layui-layer layui-layer-dialog"]')
        ActionChains(self.driver).move_to_element(ele6).perform()
        self.driver.find_element_by_xpath('//*[@ class = "layui-layer layui-layer-dialog"]/div[3]/a[1]').click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.logout()

    def Bidding_control(self):
        O.Login('admin',123456)
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/a/span').click()
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/dl/dd[2]/a').click()

        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
        self.driver.switch_to_frame(xf)

        time.sleep(1)
        list=self.driver.find_elements_by_xpath('/html/body/div/div/div/div/div[2]/div[2]/table/tbody/tr')
        project_number=[]
        for i in list:
           if '审核通过' in i.text.split('\n'):
               project_number.append(i.text.split('\n')[1])

        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="LAY_app_tabsheader"]/li[2]/i').click()
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/dl/dd[3]/a').click()

        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
        self.driver.switch_to_frame(xf)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]/div[1]/button').click()
        time.sleep(2)
        self.driver.switch_to.default_content()
        xf1 = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf1)
        self.driver.find_element_by_xpath('//*[@id="filingNum"]').send_keys(random.choice(project_number))
        self.driver.find_element_by_xpath('//*[@id="findFilingNum"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="ChooseCostConsultingAgency"]').click()
        time.sleep(2)
        self.driver.switch_to.default_content()
        xf2 = self.driver.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to_frame(xf2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/div/i').click()

    def seal12(self):
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/a').click()
        self.driver.find_element_by_xpath('//*[@id="LAY-system-side-menu"]/li[4]/dl/dd[4]/a').click()
        xf = self.driver.find_element_by_xpath('//*[@id="LAY_app_body"]/div[2]/iframe')
        self.driver.switch_to_frame(xf)
        # 滑动滚动条至中间位置
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

O=Oalogin()
O.open()
O.Login('apisxy',123456)
O.increase_Project(1)
O.Generate_project_filing()
O.project_filing(1)
O.logout()
