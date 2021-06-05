import requests
from bs4 import BeautifulSoup 
import csv

URL = "https://github.com/topics/google"
result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
title = soup.find_all("h1", {"class":"f3 color-text-secondary text-normal lh-condensed"})
captions = soup.find_all("div", {"class", "px-3 pt-3"})


for i in title:
    solution = i.text
    solution = solution.replace("\n", " ")
    solution = solution.replace(" ", "")
    f = open("file.txt", "w")
    f.write(solution)
    f.write('\n')
    f.close()
        

