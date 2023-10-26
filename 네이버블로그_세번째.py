import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 데이터를 저장할 워크북 및 워크시트 생성
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Naver Blog Data"

# 워크시트에 헤더 추가
worksheet.append(["블로그 이름", "블로그 주소", "글 제목", "날짜"])

# 1페이지부터 100페이지까지 검색 결과 수집
for page in range(1, 101):
    # URL을 동적으로 생성
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81&page={page}"

    # HTTP GET 요청을 보냄
    response = requests.get(url)

    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # BeautifulSoup로 페이지 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 검색 결과를 담고 있는 엘리먼트 찾기
        results = soup.find_all("li", class_="bx")

        # 각 검색 결과에 대한 정보 추출 및 워크시트에 추가
        for result in results:  
            blog_name = result.find("a", class_="sub_name").text.strip()
            blog_address = result.find("a", class_="sub_txt").get("href")
            post_title = result.find("a", class_="api_txt_lines").text.strip()
            date = result.find("span", class_="sub_time").text.strip()

            # 워크시트에 데이터 추가
            worksheet.append([blog_name, blog_address, post_title, date])

    else:
        print(f"페이지 {page}를 가져오지 못했습니다. 상태 코드: {response.status_code}")
        continue

# 결과를 Excel 파일로 저장
workbook.save("c:\\work\\result.xlsx")
