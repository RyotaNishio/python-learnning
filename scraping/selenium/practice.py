import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument(
    '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get('https://news.yahoo.co.jp/')
sleep(3)

search_bar = driver.find_element(by=By.CSS_SELECTOR, value='input.sc-kgoBCf')
search_bar.send_keys('機械学習')
sleep(3)

search_bar.submit()
sleep(3)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(2)
more_button = driver.find_element(by=By.CSS_SELECTOR, value='div.sc-fMIdLG > span > button')
sleep(2)
more_button.click()

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(2)
    more_button = driver.find_elements(by=By.CSS_SELECTOR, value='div.SearchMore__ButtonWrapper-bAaGOz > span > button')
    sleep(2)
    if more_button:
        more_button[0].click()
        sleep(2)
    else:
        break

d_list = []
a_tags = driver.find_elements(by=By.CSS_SELECTOR, value='a.newsFeed_item_link')
for a_tag in a_tags:
    title = a_tag.find_element(by=By.CSS_SELECTOR, value='div.newsFeed_item_title').text
    link = a_tag.get_attribute('href')

    d = {
        'title': title,
        'link': link
    }
    d_list.append(d)
#

driver.quit()

df = pd.DataFrame(d_list)
df.to_csv('result.csv')