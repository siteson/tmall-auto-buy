#python3.6.5
#coding:utf-8

'''
@author:抢口罩定制
@time:2020-04-27
程序利用自动测试工具模拟用户下单操作，完成商品的抢购
仅作为学习过程中的实践，无商业用途
'''

from selenium import webdriver
import datetime
import time

#创建浏览器对象
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.416.64 Safari/537.36"')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

#窗口最大化显示
# driver.maximize_window()

def login(url,mall):
    '''
    登陆函数
    
    url:商品的链接
    mall：商城类别
    '''
    print("请登录")
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)
    #淘宝和天猫的登陆链接文字不同
    if mall=='1':
        #找到并点击淘宝的登陆按钮
        driver.find_element_by_link_text("亲，请登录").click()
    else:
        #找到并点击天猫的登陆按钮
        driver.find_element_by_link_text("请登录").click()
    print("30秒后开始自动抢购")
    #用户扫码登陆
    time.sleep(30)
    
def buy(buy_time,mall):
    '''
    购买函数
    
    buy_time:购买时间
    mall:商城类别
    
    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    '''
    print("正在抢购，请等待...")

    if mall=='1':
        #"立即购买"的css_selector
        btn_buy='#J_juValid > div.tb-btn-buy > a'
        #"立即下单"的css_selector
        btn_order='#submitOrder_1 > div.wrapper > a'
    else:
        btn_buy='#J_LinkBuy'
        btn_order='#submitOrder_1 > div > a'

    while True:
        #现在时间大于预设时间则开售抢购
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')>buy_time:
            try:
                #找到“立即购买”，点击
                if driver.find_element_by_id("J_LinkBuy"):
                # if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    break
                time.sleep(0.1)
            except Exception as ee:
                print("Error: %s"%( str(ee) ))
                time.sleep(0.3)

    while True:
        try:
            #找到“立即下单”，点击，
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                #下单成功，跳转至支付页面
                print("购买成功")
                break
        except:
            time.sleep(0.5)
    

if __name__ == "__main__":
    url="https://detail.tmall.com/item.htm?spm=a220o.1000855.1998025129.2.58c93f82deVVa4&pvid=8cd41041-5d74-4355-831b-730c3e724715&pos=2&acm=03054.1003.1.2768562&id=549873556688&scm=1007.16862.95220.23864_0_0&utparam=%7B%22x_hestia_source%22:%2223864%22,%22x_object_type%22:%22item%22,%22x_mt%22:5,%22x_src%22:%2223864%22,%22x_pos%22:2,%22x_pvid%22:%228cd41041-5d74-4355-831b-730c3e724715%22,%22x_object_id%22:549873556688%7D"
    mall=input("请选择商城（淘宝 1  天猫 2  输入数字即可）： ")
    buydate = datetime.date.today()
    buytime = input("请输入开售时间【默认今天 10:00:00】")
    if buytime=="":
        bt = str(buydate) + " 10:00:00"
    else:
        bt = str(buydate) + " " + buytime
    print("选定的抢购时间：%s"%(bt))
    login(url,mall)
    buy(bt,mall)
        
    