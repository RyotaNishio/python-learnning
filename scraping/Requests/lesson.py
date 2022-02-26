import requests
from bs4 import  BeautifulSoup
import pandas as pd

url = 'https://www.python.org/'
r = requests.get(url)
r.raise_for_status()

html = r.content
soup = BeautifulSoup(html, 'lxml')
post= soup.find('div', class_='blog-widget')

d_list = []
for li in post.find_all('li'):
    date = li.find('time').text
    title = li.find('a').text
    link = li.find('a').get('href')
    d = {
        "date": date,
        "title": title,
        'link': link
    }
    d_list.append(d)

df = pd.DataFrame(d_list)
print(df)
df.to_csv('python_web_posts.csv', index=None, encoding='utf-8-sig')




