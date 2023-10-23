# DemoIndexing.py

x = 100
y = 3.14

print(type(x))
print(type(y))

strA = "Python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))

list =[1,2,3]
#디버깅시에 중단점(break point)


for item in list:
    print(item)

#슬라이싱(인덱스)
print(strA[0])
print(strA[1])
print(strA[0:6])
print(strA[:6])
print(strA[-3:])
print(strA[-8:])
print(strA[:])

strC = """이 문자열은
다중라인으로
저장합니다.
"""

print(strC)
print("이 문자열은\t를 출력합니다.")

colors = ["red", "blue", "green"]
print(type(colors))
print(colors)
colors.append("yellow")
print(colors)
