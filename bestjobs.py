import requests
from bs4 import BeautifulSoup


headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.454"}
glassdoor = requests.get('https://www.glassdoor.com/List/Best-Jobs-in-America-LST_KQ0,20.htm', headers = headers_param)

jobs = glassdoor.content

soup = BeautifulSoup(jobs, "html.parser")

title = soup.title

#print(soup.find('h1').text) #get h1 tag
#print(soup.find_all('div')) #get all div tag
all_jobs = soup.find_all('p',{'class':'h2 m-0 entryWinner pb-std pb-md-0'})

for job in all_jobs:
    print(job.a.text)

all_data = soup.find_all('div',{'class':'col-6 col-lg-4 dataPoint'})

for data in all_data:
    print(data.text)