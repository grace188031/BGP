from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import time
from selenium.common import exceptions
import pandas as pd

LOGIN_URL = 'https://ssp2.gin.ntt.net/lg/lg.cgi'

browser = webdriver.Chrome('chromedriver.exe')
browser.get(LOGIN_URL)


class BGP:

    status=[]
    query = browser.find_element(By.XPATH, "//select[@name='query']/option[2]")
    IPselect = browser.find_element(By.XPATH, "//input[@value='IP']")
    inputip = browser.find_element(By.XPATH, "//input[@name='addr']")
    submit = browser.find_element(By.XPATH, "//input[@value='Submit']")
    router = browser.find_element(By.XPATH, "//select[@name='router']/optgroup[2]/option[2]")
    IP_list = ['120.29.7.220', '120.29.7.221']
    sender_recipient = 'zabala_marygrace31@yahoo.com'

    def __init__(self,ip):
       self.ip= ip

    @classmethod
    def load(cls):
        time.sleep(10)
        cls.router.click()
        cls.query.click()
        cls.IPselect.click()

    def input(self):
        self.inputip.send_keys(self.ip)
        self.submit.click()
        time.sleep(4)
    def clear(self):
       # self.inputip.send_keys(Keys.CONTROL + 'a')
       # self.inputip.send_keys(Keys.CONTROL+ u'\ue003' )
        clearnow = browser.find_element(By.XPATH, "//input[@value='" + IP_list[0] + "']")
        clearnow.clear()
        time.sleep(10)
    def input2(self):
        input2 = browser.find_element(By.XPATH, "//input[@value='120.29.7.220']")
        input2.send_keys(self.ip)
        time.sleep(8)
        self.submit.click()
    #    time.sleep(4)
    def quit(self):
        browser.quit()
    def submits(self):
        self.submit.click()
    @classmethod
    def send_Outlook(cls):
        outlook = win32.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.SentOnBehalfOfName = cls.sender_recipient
        mail.To = cls.sender_recipient
        mail.Subject = 'BGP STATUS MAILER'
        mail.Body = 'str(df_states)'
        mail.HTMLBody = 'str(df_states)'  # this field is optional
        # To attach a file to the email (optional):
        # attachment = "C:\Users\zabal\PycharmProjects\pythonProject1\bgp.csv"
        # .Attachments.Add(attachment)
        mail.Send()
#  def outer_function(cls):
#      cls.load()





if __name__ == '__main__':
    IP_list = ['120.29.7.220', '120.29.7.221']
    status = []
    #BGP.load()

    for o in IP_list:
        g = BGP(o)
        BGP.load()
        g.input()
#        if str(IP_list[0]) == o:
#            g.input()
 #       else:
 #           try:
 #               g.input2()
 #           except exceptions.StaleElementReferenceException as e:
  #              print(e)

        try:
           browser.find_element(By.XPATH, "//font[contains(text(), 'Success rate is 100 percent')]")
           bgp_status = "UP"

        except:
            bgp_status="DOWN"

        status.append(bgp_status)
        browser.refresh()
        browser.get(LOGIN_URL)
       # g.clear()




    dict_states={'BGP_IP':IP_list,'Status':status}
    df_states = pd.DataFrame.from_dict(dict_states)
    df_states.to_csv('bgp.csv',index=False)
    print(str(df_states))

schedule.every(3).minutes.do(BGP.load())

schedule.every(6).minutes.do(BGP.send_Outlook())

while True:
    schedule.run_pending()
    time.sleep(2)











