import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

base_url = "https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?jb_type_long_cd=0100000000&wrk_plc_long_cd=0313000000&wrk_plc_long_cd=0313100000&wrk_plc_long_cd=0314000000&curnum={}"

for i in range(3):
    r = requests.get(base_url.format(1+50*i))
    sleep(3)

    soup = BeautifulSoup(r.content, 'lxml')
    posts = soup.select('ul.rnn-jobOfferList > li')

    d_list = []
    for i, post in enumerate(posts):
        post_url = "https://next.rikunabi.com" + post.select_one('a').get('href').replace('nx1', 'nx2')
        post_r = requests.get(post_url)
        post_soup = BeautifulSoup(post_r.content, 'lxml')

        try:
            company_name = post_soup.select_one('.rn3-companyOfferCompany__info:first-of-type > p > a').text.strip(' ')
        except:
            company_name = 'None'

        try:
            company_link = "https://next.rikunabi.com" + post_soup.select_one('.rn3-companyOfferCompany__info:first-of-type > p > a').get('href')
        except:
            company_link = 'None'

        d = {
            'company_name': company_name,
            'link': company_link
        }
        d_list.append(d)


df = pd.DataFrame(d_list)
df.to_csv('result.csv', index=None, encoding='utf-8-sig')
