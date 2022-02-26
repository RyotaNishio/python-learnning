import  chromedriver_binary
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# driverを作成
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument(
    '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# アクセス
driver.get('https://news.yahoo.co.jp')
sleep(3)

height = driver.execute_script('return document.body.scrollHeight')
sleep(3)
driver.execute_script(f'window.scrollTo(0, {height})')
sleep(3)

driver.quit()