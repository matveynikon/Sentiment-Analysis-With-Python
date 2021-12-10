import requests
import pandas
from bs4 import BeautifulSoup
import numpy as np

d = 0
l1 = []
neutral = []
bad = []
good = []
df = pandas.read_csv('sentiment.csv')
sen = df["word"]
cat = df["sentiment"]
url='https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
for x in headlines:
    l1.append(x.text.strip().lower())
    for i in range(109):
        if sen[i] in x.text.strip().lower():
            if x.text.strip() not in l1:
                if cat[i] == 0:
                    bad.append(x.text.strip().lower())
                    print("Bad")
                else:
                    good.append(x.text.strip().lower())
                    print("Good")
            else:
                print("Headline exception")
        else:
            if x.text.strip().lower() not in bad and x.text.strip() not in good:
                neutral.append(x.text.strip().lower())


badp = (len(bad) / len(l1)) * 100
goodp = (len(good) / len(l1)) * 100
nep = ((len(neutral) / 82) / len(l1)) * 100
print(str(badp) + ' ' + str(goodp) + ' ' + str(nep))
