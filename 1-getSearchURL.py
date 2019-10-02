from selenium import webdriver
from selenium.webdriver.common.keys import Keys

baseurl="https://www.google.com.vn/?gws_rd=ssl"

driver = webdriver.Firefox()
driver.get(baseurl)
driver.find_element_by_id("lst-ib").click()
driver.find_element_by_id("lst-ib").clear()
driver.find_element_by_id("lst-ib").send_keys("vinpro")
driver.find_element_by_id("lst-ib").send_keys(Keys.RETURN)
driver.implicitly_wait(3)

link_name = driver.find_elements_by_xpath(
"/html/body//div[5]/div[4]/*/div[1]/div[3]/div/div[2]/div[2]/div/div/ol/*/*/div/h3/a")
for link in link_name:
    print(link.get_attribute("href"))

next = driver.find_elements_by_xpath(
"/html/body//div[5]/div[4]/*/div[1]/div[3]/div/div[5]/div/span[1]/div/table/tbody/tr/td[12]/a")
for link in next:
    print(link.get_attribute("href"))
