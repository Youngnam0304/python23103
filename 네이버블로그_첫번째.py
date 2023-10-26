import requests
from bs4 import BeautifulSoup

# URL to crawl
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200: #크롤링이 문제 없으면 200 코드가 나옴
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements that contain the desired information
    results = soup.find_all("li", class_="bx")

    for result in results:
        # Extract blog name
        blog_name = result.find("a", class_="sub_name").text.strip()

        # Extract blog address
        blog_address = result.find("a", class_="sub_txt").get("href")

        # Extract post title
        post_title = result.find("a", class_="api_txt_lines").text.strip()

        # Extract date
        date = result.find("span", class_="sub_time").text.strip()

        # Print the extracted information
        print("Blog Name:", blog_name)
        print("Blog Address:", blog_address)
        print("Post Title:", post_title)
        print("Date:", date)
        print("\n")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
