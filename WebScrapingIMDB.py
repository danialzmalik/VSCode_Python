
# source material based on where im learning from
# https://medium.com/@nishantsahoo/which-movie-should-i-watch-5c83a3c0f5b1
# resources:
# https://urllib3.readthedocs.io/en/stable/user-guide.html
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# https://realpython.com/beautiful-soup-web-scraper-python/

import urllib3
from bs4 import BeautifulSoup

# userURL = input("Enter URL: ")
userURL = "https://www.imdb.com/search/title/?release_date="
year = input("Enter the year you want to check the movies of (####): ")
ourURL = urllib3.PoolManager().request('GET', userURL+year).data
soup = BeautifulSoup(ourURL, "lxml")
results = soup.find(id="main")
movies = results.findAll("h3", class_="lister-item-header")

_ = 1
for i in movies:
    if _ > 10: break
    ranking = i.find("span", class_="lister-item-index unbold text-primary")
    titles = i.find("a")
    print(ranking.text, end="\t")
    print(titles.text)
    _+=1
# movieTitles = results.find_all("a")
# print(movieTitles)



#find a way to print only the top 10 imdb movie titles