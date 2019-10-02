from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymysql
import time

baseurl = "https://www.google.com.vn/?gws_rd=ssl"
query = "vinpro"
xpath = "/html/body//div[5]/div[4]/*/div[1]/div[3]/div/div[2]/div[2]/div/div/*/*/*//div/h3/a"

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='P@ssword', db='mysql', charset='utf8')
#, unix_socket='/tmp/mysql.sock', passwd=None
cur = conn.cursor()
cur.execute("USE scraping")

def insertLink(keyword, url):
    #cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)))
    #if cur.rowcount == 0:
    cur.execute("INSERT INTO google_search (keyword, url) VALUES (%s, %s)", ((keyword), (url)))
    conn.commit()
	
link_name = set()
next = set()

def getGoogleSearch(url, recursionLevel):
    global link_name
    global next
    if recursionLevel > 5:
        return;
    time.sleep(8)
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get(url)
    if recursionLevel == 0:
        driver.find_element_by_id("lst-ib").click()
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys(query)
        driver.find_element_by_id("lst-ib").send_keys(Keys.RETURN)
    #driver.implicitly_wait(3)
    time.sleep(3)

    link_name = driver.find_elements_by_xpath(xpath)
    for link in link_name:
        print(link.get_attribute("href"))
        insertLink(query, link.get_attribute("href"))
        time.sleep(0.5)

    next = driver.find_elements_by_xpath(
"/html/body//div[5]/div[4]/*/div[1]/div[3]/div/div[5]/div/span[1]/div/table/tbody/tr/td[12]/a")
    for link in next:
        print(link.get_attribute("href"))
        getGoogleSearch(link.get_attribute("href"), recursionLevel + 1)
    driver.quit()

getGoogleSearch(baseurl, 0)
cur.close()
conn.close()
