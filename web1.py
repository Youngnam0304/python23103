#web1.py
#웹크롤링
from bs4 import BeautifulSoup
#뷰티풀수프 선언 방법 (약자 bs4 사용)

#페이지 로딩 
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()  #open 하고나서 바로 read를 붙이면 change가 됨
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")  #뷰티풀수프 초기화 로직
#전체보기
print(soup.prettify())

