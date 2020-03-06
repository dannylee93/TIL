# 1.크롤링 할 때 사용할 모듈 불러오기
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from time import sleep

# 2.크롤러 모델링
td_data = []

for nums in range(1, 1342, +1):
    page = requests.get("URL-주소(임의 변경)".format(nums))
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('tbody')
    th_data = [item.get_text().strip() for item in table.select('th')]
    td_data.append([item.get_text().strip() for item in table.select('td')])
    #sleep(5)


# 3.데이터 저장하기
column_data = np.array(th_data)
row_data = np.array(td_data)
companies = pd.DataFrame(data=row_data, columns=column_data)