#마우스로 그림 그리기(마우스 이벤트 처리)
# 함수 사용, 아직 배우지 않음
# 기능 1 : 마우스 왼쪽 버튼 클릭 이전 좌표에서 마우스 왼쪽 버튼 클리한 위치까지 임의의 색상
# 기능 2 : 마우스 오른쪽 버튼 클릭 이전 좌표에서 마우스 오른쪽 버튼 클릭한 위치까지 선을 기기
# 기능 3 : 마우스 중앙 버튼 클릭 거북이를 임의의 크기로 변경, 선도 임의의 색으로 변경
# random 라이브러리 사용, 사용법 검색
# random(), randrange(), onscreenclick()

import turtle as t
import random as ra

def mLeft(x, t):
    global r, g, b
    t.color((r,g,b))
    t.down()
    t.goto(x,y)

def mRight(x, t):
    t.up()
    t.goto(x,y)
    

def mMid(x, t):
    global r, g, b
    pSize = ra.randrange(1, 6)
    t.pensize(pSize)
    r = ra.random()
    r = ra.random()
    r = ra.random()
    
def kClear():
    t.clear()
    
def kQuit():
    t.bye()
                
                
                
                
r ,g ,b = 0.0, 0.0, 0.0

# t.tilt("마우스로 그림 그리기")
t.onscreenclick(mLeft, 1)
t.onscreenclick(mMid, 2)
t.onscreenclick(mRight, 3)

s.onKet(kClear, "c")
s.onKey(kQuit, "q")

t.done()