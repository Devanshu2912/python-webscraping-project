import requests
from bs4 import BeautifulSoup
import pandas as pd

name_list = []
price_list = []
review_list = []
desc_list = []


url = "https://www.airbnb.co.in/s/Delhi--India/homes?adults=1&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJL_P_CXMEDTkRw0ZdG-0GVvw&location=Delhi%2C+India"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

try:
    while True:

        name = soup.find_all('div', {'class': 't1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_hfv0h6 atm_cs_1mexzig atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr'})
        for i in name:
            name_list.append(i.text)
        #print(name_list)

        price = soup.find_all('span', {'class': 'u174bpcy atm_7l_mhi6a6 atm_cs_80qqwn atm_rd_14k51in atm_rq_glywfm atm_cs_l3jtxx__1v156lz dir dir-ltr'})
        for i in price:
            price_list.append(i.text)
        #print(price_list)

        review = soup.find_all('span', {'class': 'r4a59j5 atm_h_1h6ojuz atm_9s_1txwivl atm_7l_hfv0h6 atm_84_iv6dct atm_mk_h2mmj6 atm_mj_glywfm dir dir-ltr'})
        for i in review:
            review_list.append(i.text)
        #print(review_list)

        desc = soup.find_all('div', {'class': 's1cjsi4j atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vlb1yz atm_7l_xeyu1p atm_ks_zryt35__1rgatj2 f1v0rf5q atm_da_cbdd7d dir dir-ltr'})
        for i in desc:
            desc_list.append(i.text)
        #print(desc_list)

        np = soup.find('a', {'aria-label': 'Next'}).get('href')
        cnp = "https://www.airbnb.co.in/"+np
        #print(cnp)

        url = cnp
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')    
except:
    pass
lengths = [len(name_list), len(price_list), len(review_list), len(desc_list)]
minlen = min(lengths)
if len(set(lengths)) != 1:
    print("unequal lengths, truncating to", minlen, lengths)
    name_list = name_list[:minlen]
    price_list = price_list[:minlen]
    review_list = review_list[:minlen]
    desc_list = desc_list[:minlen]

df = pd.DataFrame({
    'Name': name_list, 
    'Price': price_list, 
    'Review': review_list, 
    'Description': desc_list
})   
print(df)

df.to_csv('Airbnb.csv')