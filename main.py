from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

base_url = 'https://kr.indeed.com/jobs?q='
keyword = 'python'

browser.get(f"{base_url}{keyword}")

results = []
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList css-0")
jobs = job_list.find_all('li', recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        anchor = job.select("h2 a")
        print(anchor)
        """
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          'link': f"https://kr.indeed.com/{link}",
          'company': company.string,
          'location': location.string,
          'position': title
        }
    results.append(job_data)
for result in results:
  print(result, "\n//////////\n")
    """
