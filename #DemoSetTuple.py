#DemoSetTuple.py

a = {1, 2, 3, 3}
b = {3, 4, 4, 5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
#union : 합집합
#intersection : 교집합
#differnce : 차집합

print("---Tuple형식---")
tp = (1, 2, 3)
print(tp)
print(len(tp))
print(tp[0])
print("id: %s, name: %s" % ("im", "임영남"))

#함수 정의 
def calc(a, b):
    return a+b, a*b

#함수 호출
print(calc(3,4))

