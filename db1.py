#db1.py
import sqlite3

#연결객체 :보통 정해져있음. 아래와 같이 
con = sqlite3.connect(":memory:")
#커서객체 
cur = con.cursor()
#테이블 구조 생성
cur.execute("""create table if not exists PhoneBook
    (id integer primary key autoincrement, name text, phoneNum text);
    """)

#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('전우치', '010-222');")

#입력 파라메터 처리 
name = "홍길동"
phoneNumber = "010-333"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);",
    (name, phoneNumber))
#여러개를 한번에 입력하는거는 무조건 Tupel()

#다중으로 행을 입력
datalist = (("박문수", "010-333"), ("김길동", "010-567"))  #이차 행렬 데이터, 앞에 NO는 자동으로 증가시키는 구문이 위에 있으니 이거는 2행 3열 구문 
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);",
    datalist)
#executemany 여러개의 데이터를 한번에 넣을 경우에 execute 대신해서 사용함. 

#검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---")  #fetchone : 레코드 포인터가 하나 인경우 하나의 데이터를 읽고 버퍼(임시메모리)에다가 보여주고 사라짐 그리고 다음으로 넘어감 
print(cur.fetchone())
print("---fetchmany(2)---") #fetchmany : 두개의 데이터(다수)의 데이터를 읽고 보여주고 사라짐. 그리고 다음으로 넘어감
print(cur.fetchmany(2))
print("---fetchall()---") #fetchall : 모든 데이터를 보여줌. 그러나 이번 예제에는 앞에 one / many에서 1/ 2를 보여주고 사라짐으로 안보임
cur.execute("select * from PhoneBook;") # 이전 one / many에서 사라진 버퍼아의 데이터를 다시 reset 시킨다 라는 말.  
print(cur.fetchall())

# #검색
# cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)