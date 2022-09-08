from requests import get
from bs4 import BeautifulSoup


def extract_planet_jobs(keyword):
    base_url = "https://www.jobplanet.co.kr/search?query="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('div', class_="result_unit_info")
        for job in jobs:
            anchors = job.find_all('a', class_="posting_name")
            anchor = anchors[0]
            link = anchor['href']
            company = anchor['data-company-name']
            position = anchor['data-occupation-level2-name']
            find_location = job.find('div', class_="result_labels")
            location = find_location.find('span', class_="tags")
            job_data = {
                'link': f"https://www.jobplanet.co.kr{link}",
                'company': company,
                'location': location.string.replace(",", " "),
                'position': position.replace(",", " "),
            }
            results.append(job_data)
    return results
