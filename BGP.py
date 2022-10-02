from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BGP:
    IP_list = ['120.29.7.220','120.29.7.221']
    status=[]
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://ssp2.gin.ntt.net/lg/looking_glass_web_gitRepo/lg.cgi')
    router = browser.find_element(By.XPATH, "//select[@name='router']/optgroup[2]/option[2]")
    query = browser.find_element(By.XPATH, "//select[@name='query']/option[2]")
    IPselect = browser.find_element(By.XPATH, "//input[@value='IP']")
    inputip = browser.find_element(By.XPATH, "//input[@name='addr']")

    submit = browser.find_element(By.XPATH, "//input[@id='submit']")

    def __init__(self,ip):
       self.ip= ip
    @staticmethod
    def load():
        time.sleep(10)
        self.router.click()
        self.query.click()
        self.IPselect.click()
    def input(self):
        self.inputip.send_keys(self.ip)
        self.submit.click()
        time.sleep(4)
    def clear(self):
       # self.inputip.send_keys(Keys.CONTROL + 'a')
       # self.inputip.send_keys(Keys.CONTROL+ u'\ue003' )
        clearnow = self.browser.find_element(By.XPATH, "//input[@value='" + self.ip + "']")
        clearnow.clear()
        time.sleep(18)
    def input2(self):
        input2 = self.browser.find_element(By.XPATH, "//input[@value= ' ']")
        input2.send_keys(self.ip)
    def quit(self):
        self.browser.quit()




if __name__ == '__main__':


    for o in BGP.IP_list:
        g = BGP(o)
        g.load()
        g.input()
        time.sleep(10)
        g.clear()
        BGP.status.append(o)
        print(BGP.status)








