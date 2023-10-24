#전역 변수 
str = "Not Class Member"
class GString:
    def __init__(self):
        #멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #self누락
        print(self.str)

g = GString()
g.set("First Message")
g.print()
