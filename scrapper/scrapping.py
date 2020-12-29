import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="19141918",
  database="sun"
)

my_cursor = my_db.cursor()

URL = 'http://127.0.0.1:5500/planets.html'
page = requests.get(URL)

table = soup(page.content, 'html.parser')
table_rows = table.find_all('tr')

data = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip().replace('\n', '') for tr in td]
    data.append(row)

df = pd.DataFrame(data, columns=["photo", "name", "mass", "diameter", "description", "more_info"])
df.drop(df.columns[[0]], axis=1, inplace=True)
df = df.iloc[1:-1]
print(df)

df.to_csv("C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\b professor\\planets\\planets.csv", sep= ";")
df.to_json("C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\\PYTHON\\b professor\\planets\\planets.json")

cols = "`,`".join([str(i) for i in df.columns.tolist()])
for i,row in df.iterrows():
    sql = "INSERT INTO `planets` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    my_cursor.execute(sql, tuple(row))
    my_db.commit()
