# class 선언
class myClass:
    def __init__(self,x): #생성자
        self.x = x
        print("생성자가 호출되었음")

inst = myClass(10)
print(inst.x)

#모듈 가져오기
import random as rd
from random import randrange as rdr
from random import *

v = [rdr(1,101) for i in range(10)]
print(v)