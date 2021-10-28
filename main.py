import requests
from bs4 import BeautifulSoup
import json
######


response = requests.get('https://www.empireonline.com/tv/features/best-tv-shows-ever-2/')
site_data = response.text

soup = BeautifulSoup(site_data, "html.parser")
# print(soup.prettify())
# title = soup.find_all(name="script", id='__NEXT_DATA__', type="application/json")

x = soup.findAll(name='script', id ='__NEXT_DATA__', attrs={'type': 'application/json'})

tv_shows_list = []
for i, script in enumerate(x):
    if i == 0:
        json_data = json.loads(script.text)
        tv_shows_raw = json_data['props']['pageProps']['data']['getArticleByFurl']['_layout'][6]['content']['images']
        for x in range(len(tv_shows_raw)):
            tv_shows_list.append(tv_shows_raw[x]['titleText'])

tv_shows_top = tv_shows_list[::-1]

print(tv_shows_top)

for show in tv_shows_top:
    with open('tvshows.txt', 'a') as file:
        file.write(f'{show}\n')
