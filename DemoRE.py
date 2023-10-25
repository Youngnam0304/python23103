#DemoRE.py
#정규표현식 (특정한 규칙)

import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

#함정 추가(공백)
#search는 끝까지 찾아서 일치하면 가져옴
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#함정 추가(공백)
# #match는 정확하게 일치하는 것만 가져오므로, 공백을 만나서 가져오지 못하는 상황임. 
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())

#함정 추가(대문자) - 기존 로직으로는 검색 불가
#그래서 lower()사용해서 소문자화 시켜놓고 re.search 진행
result = re.search("apple", "this is Apple".lower())
print(result.group())

result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52300")
print(result.group())

#컴파일 함수를 사용
data = "Apple is big company and apple is delicious"
c = re.compile("apple", re.IGNORECASE) #re.IGNORECASE : 대소문자를 구분하지 말라는 옵션
print(c.findall(data)) #findall : '다 찾아'라는 함수 

data = """다중 라인으로 
만든 문자열 

데이터"""

c = re.compile("^.+", re.MULTILINE)  
#^ : 시작 패턴 / . : 문자 1개 / + : 1 ~ N번   #^.+ : 시작할때, 글자가 1개라도 나와야한다. 
#re.MULTILINE : '모든 라인을 다 봐야해' 라는 옵션 
print(c.findall(data))

