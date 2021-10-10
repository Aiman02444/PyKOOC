# coding: utf-8
# fourcalculation.py
"""A class for four arithmetic calculations""" #설명

class FourCalculation: 
    #클래스는 대문자로 시작, 단어와 단어는 대문자로 구분, 나머지는 소문자
    """A class for four arithmetic calculation"""
    #docstring을 통해 clas를 정의하고 시작한다

    def __init__(self, first, second): #모든 클래스의 시작(initialize)
        #__init__(self, 변수1, 변수2)에서 class의 method를 불러올 때 
        #self가 자동적으로 전달되게 하기 위해 self는 꼭 써야 한다.
        self.first = first
        self.second = second #로컬변수로 만들어 사용한다
        
        if second == 0:
            raise ValueError('the number must NOT be zero')
        #exception, 어떤 해서는 안될 일이 발생할 때 미연에 방지하기 위함
        
    def add(self): #새로운 method를 내가 만들어준다!
        return self.first + self.second #내부변수의 활용
        
    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second
    
    def div(self):
        return self.first / self.second

        
