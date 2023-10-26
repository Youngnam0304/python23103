#web1.py
#웹크롤링
from bs4 import BeautifulSoup
#뷰티풀수프 선언 방법 (약자 bs4 사용)

#페이지 로딩 
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()  #open 하고나서 바로 read를 붙이면 change가 됨
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")  #뷰티풀수프 초기화 로직

#전체보기
#print(soup.prettify()) 

#<p>태그 전체를 검색 
#print(soup.find_all("p"))

#첫번째 <p>만 검색
#print(soup.find("p"))

#<p class="outer-text">형태만 검색 - 원하는 키워드만 검색하는 경우에 사용
#print(soup.find_all("p", class_="outer-text"))  #class라는 키워드가 기존 파이썬에 있기 때문에 뷰티풀수프에서 사용시에 뒤에 '_'를 사용해서 충돌을 방지함 

#attrs 를 사용 (Attributes) - 위의 '_'를 사용하지 않는 추세이기 때문에 아래와 같이 arrts 변수 지정해서 사용을 많이 한다 
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#특정 태그만 지정할 경우 id속성  - 아래 구문은 id 에 first를 지정한 경우임 
#print(soup.find_all(id="first"))

#태그 내부의 컨텐츠를 가져오기. : .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)




