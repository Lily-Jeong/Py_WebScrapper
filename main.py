from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&l&vjk=9f50e72b1130520d")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList css-0")
jobs = job_list.find_all("li")
for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
  if zone == None:
    anchor = job.select("h2 a")
    print(anchor)
    print("///////////")
    