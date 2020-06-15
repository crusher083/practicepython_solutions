import bs4
import requests

res = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
res.raise_for_status()
site = bs4.BeautifulSoup(res.text, features="lxml")
art = site.select("p")
new_file = input("Name article file:")
with open(f'{new_file}', 'w', encoding="utf-8") as file:
    for i in art[3:-6]:
        line = i.getText().strip()
        file.write(str(line + '\n'))




