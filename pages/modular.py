from common.slideVerfication import SlideVerificationCode
from common.Driver import Driver
import time

class testzh(Driver):
    def open(self):
        self.driver.get("https://qzone.qq.com/")

    def login(self):
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_id("switcher_plogin").click()

        self.driver.find_element_by_id("u").send_keys("350978786")
        self.driver.find_element_by_id("p").send_keys("12131311")
        time.sleep(2)
        self.driver.find_element_by_id("login_button").click()

        iframe_sli = self.driver.find_element_by_id("tcaptcha_iframe")
        self.driver.switch_to.frame(iframe_sli)

        # 3.1 定位滑块背景图
        bg_ele = self.driver.find_element_by_id("slideBg")
        # 3.2 定位滑动的图片
        block_ele = self.driver.find_element_by_id("slideBlock")

        # 3.3 定位滑动的按钮
        sil_btn = self.driver.find_element_by_id("tcaptcha_drag_thumb")
        # 3.4 创建一个验证码滑动的对象
        sli_code = SlideVerificationCode()
        # 3.5、获取验证码背景图的缺口位置
        x = sli_code.get_element_slide_distance(block_ele, bg_ele)
        # 3.6 根据页面图片的缩放比进行调整
        loc_x = x * (280 / 680) - 31
        # 3.7模拟拖动鼠标进行滑动验证
        sli_code.slide_verification(self.driver, sil_btn, loc_x)

# # 1.2 打开qq登录页面
# driver.get("https://e.oppomobile.com/")
# first_window=driver.current_window_handle
# time.sleep(3)
# driver.find_element_by_link_text("广告投放管理").click()
# time.sleep(3)
# #切换窗口
# windows=driver.window_handles
# for i in windows:
#     if i == first_window:
#         continue
#     else:
#         driver.switch_to.window(i)