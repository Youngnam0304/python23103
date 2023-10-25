#챗GPT로 생성한 클래스.py

class Person:
    def __init__(self, id, phoneNumber):
        self.id = id
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print(f"ID: {self.id}")  # ID 출력
        print(f"전화번호: {self.phoneNumber}")  # 전화번호 출력


class Manager(Person):
    def __init__(self, id, phoneNumber, skill):
        super().__init__(id, phoneNumber)
        self.skill = skill

    def printInfo(self):
        super().printInfo()  # 상위 클래스의 printInfo 메서드 호출
        print(f"스킬: {self.skill}")  # 스킬 출력


class Employee(Person):
    def __init__(self, id, phoneNumber, title):
        super().__init__(id, phoneNumber)
        self.title = title

    def printInfo(self):
        super().printInfo()  # 상위 클래스의 printInfo 메서드 호출
        print(f"직급: {self.title}")  # 직급 출력

# 아래는 이러한 클래스를 사용하여 객체를 생성하고 정보를 출력하는 예시 코드입니다.

# Person 객체 생성
person = Person("12345", "555-555-5555")
print("Person 정보:")
person.printInfo()
print()

# Manager 객체 생성
manager = Manager("56789", "777-777-7777", "리더십")
print("Manager 정보:")
manager.printInfo()
print()

# Employee 객체 생성
employee = Employee("98765", "999-999-9999", "소프트웨어 개발자")
print("Employee 정보:")
employee.printInfo()


# Sample code to create and use objects of these classes

# Create a Person
person = Person("12345", "555-555-5555")
print("Person Info:")
person.printInfo()
print()

# Create a Manager
manager = Manager("56789", "777-777-7777", "Leadership")
print("Manager Info:")
manager.printInfo()
print()

# Create an Employee
employee = Employee("98765", "999-999-9999", "Software Developer")
print("Employee Info:")
employee.printInfo()
