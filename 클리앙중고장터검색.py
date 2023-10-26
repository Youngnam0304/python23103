# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
#크롤링시에 해당 사이트에서 ip가 막히는 경우가 있는데, 그 경우가 헤더 메세지가 없는 경우이다. 그래서 위 처럼 강제로 헤더메세지를 입력해줘야 하는 경우가 있다. 
#웹봇 처럼 안보이기 위해서 작성이 필요한 경ㅇ가 있다. 

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우 (아래 코드 작성)
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        # <span class="subject_fixed" data-role="list-title-text" title="아이폰 13프로 256 블루 (북미판) 새로 리퍼 받은 S급">
	# 						아이폰 13프로 256 블루 (북미판) 새로 리퍼 받은 S급
	# </span>

        for item in list:
                try:
                        title = item.text.strip()
                        print(title)
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
