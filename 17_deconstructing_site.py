import bs4
import requests

res = requests.get('http://nytimes.com')
res.raise_for_status()
nytimes = bs4.BeautifulSoup(res.text, features="lxml")
titles = nytimes.select('h2')
for title in titles[3:-2]:  # those were some ads in same css format
    header = title.getText()
    if not header.isspace():
        print(header.replace("\n", " ").strip())