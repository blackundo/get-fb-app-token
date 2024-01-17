import requests
from bs4 import BeautifulSoup
import re
from urlparse import urlparse, parse_qs
import json


def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        # print(f'Error fetching {url}: {e}')
        return None

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    pattern = re.compile(r"https://rewards\.coinmaster\.com/rewards/rewards\.html\?c=\w+")
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if pattern.match(href):
            links.append(href)
    return links

def extract_c_param(links):
    # c_params = []
    c_params = set()  # Use a set to store unique values
    for link in links:
        parsed_url = urlparse(link)
        query_params = parse_qs(parsed_url.query)
        if 'c' in query_params:
            c_params.add(query_params['c'][0])
    return list(c_params)  # Convert the set back to a list

def main(urls):
    all_links = []
    for url in urls:
        html = fetch_html(url)
        if html:
            links = extract_links(html)
            all_links.extend(links)
    return extract_c_param(all_links)

if __name__ == "__main__":
    urls = [
        "https://www.topzone.vn/tekzone/cach-nhan-spin-coin-master-1556360",
        "https://www.thegioididong.com/game-app/3-cach-nhan-hang-tram-luot-spin-mien-phi-trong-coin-m-1257965",  # Replace with your list of URLs
        "https://cellphones.com.vn/sforum/link-nhan-code-coin-master-spin",
        "https://levvvel.com/vi/free-spin-code-coin-master/",
        "https://gamevui.vn/huong-dan/link-nhan-spin-va-thuong-vang-mien-phi-game-coin-master-90",
        "https://viettelstore.vn/tin-tuc/huong-dan-nhan-spin-coin-master-moi-nhat"
    ]
    codes = main(urls)
    # for code in codes:
    #     print(code)
    codes_json = [{"code": code} for code in codes]
    with open('spinfree.json', 'w') as json_file:
        json.dump(codes_json, json_file, indent=2)
    
    print("JSON file 'codes.json' created successfully.")