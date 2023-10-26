# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
#크롤링시에 해당 사이트에서 ip가 막히는 경우가 있는데, 그 경우가 헤더 메세지가 없는 경우이다. 그래서 위 처럼 강제로 헤더메세지를 입력해줘야 하는 경우가 있다. 
#웹봇 처럼 안보이기 위해서 작성이 필요한 경ㅇ가 있다. 

#파일에 저장하는 방법 (가장 바깥의 루프전에 적어줘야됨.)
f = open("c:\\work\\today.txt", "wt", encoding="utf-8")
for n in range(1,11):
        #오늘의 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우 (아래 코드 작성)
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

# <td class="subject">
# <a href="/board/view.php?table=bestofbest" target="_top">우리나라 지금 현재 전쟁나면 필패인 이유 추가</a><span class="list_memo_count_span"> [18]
# </span>   </td>

        for item in list:
                #에러처리 (try ~ catch)
                try:
                        title = item.find("a").text.strip()
                        if re.search("미국", title):
                            print(title)
                            f.write(f"{title}\n")
                except:
                        pass   #에러가 나면 그냥 skip하고 루프를 계속 돌려라 라는 의미. 
        
f.close()

