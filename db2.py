#db1.py
import sqlite3

#연결객체(파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db") 
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
print(cur.fetchall())

#작업 완료(무조건 작업 완료 전에 commit하고 마무리 필요. 안그러면 rollback함)
con.commit()


# #검색
# cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

#주의 : SQLite는 커밋을 하지 않으면 저장되지 않고 무조건 rollback이 된다. 
