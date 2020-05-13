import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get("https://www.cbr.ru/currency_base/daily/")
html = BeautifulSoup(r.content, features="html.parser")
data = []
table = html.find("table")
for tr in table.find_all("tr"):
    data.append([td.get_text().replace(" "," ") for td in tr.find_all("td")])
data = pd.DataFrame(data[1:], columns=['Цифровой код', "Буквенный код", "Единиц", "Валюта", "Курс"])
funt = data.loc[data.loc[:, 'Валюта'] == 'Фунт стерлингов Соединенного королевства'][:]
funt = funt['Курс']
dollar = data.loc[data.loc[:, 'Валюта'] == 'Доллар США'][:]
dollar = dollar['Курс']
euro = data.loc[data.loc[:, 'Валюта'] == 'Евро'][:]
euro = euro['Курс']
kit = data.loc[data.loc[:, 'Валюта'] == 'Китайский юань'][:]
kit = kit['Курс']
frank = data.loc[data.loc[:, 'Валюта'] == 'Швейцарский франк'][:]
frank = frank['Курс']
lira = data.loc[data.loc[:, 'Валюта'] == 'Турецкая лира'][:]
lira = lira['Курс']
yena = data.loc[data.loc[:, 'Валюта'] == 'Японских иен'][:]
yena = yena['Курс']

