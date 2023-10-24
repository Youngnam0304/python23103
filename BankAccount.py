# BankAccount.py

#파이썬의 단점이 고객에게 전달 시 소스코드를 통채로 전달해야 하는 상황이나, exe 기계어 코드로 변경은 가능하다. 
#파이썬에서 숨김처리 하는 방법은 __를 앞에만 붙여서 숨김 처리가 가능하다. 

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #멤버변수 숨김
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    #인스턴스의 문자열(상태)
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, 
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#읽기
print(account1.__balance)
#숨김처리가 되어 있기 때문에 디버깅시 오류가 발생한다. 

