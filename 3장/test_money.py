"""
- 통화 간 환전 (테스트할 내용) - 1 ERU = 1.2 USD / 1 USD = 1100KRW 라고 가정
    1. 5 USD + 10 USD = 15 USD
    2. 5 USD + 10 EUR = 17 USD
    3. 1 USD + 1100 KRW = 2200 KRW
"""

import unittest

# 순서 2-2에서 추가된 모듈
import functools
import operator
  
class Money : 

    def __init__(self, amount, currency) : 
        self.amount = amount
        self.currency = currency

    def times(self, multiplier) : 
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divisor) : 
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other) -> bool:
        return self.amount == other.amount and self.currency == other.currency

# 순서 2 
# Portfolio 클래스를 정의하자 
class Portfolio : 

    # 순서 5
    # 이렇게 정의하고 테스트를 실행하면 또 오류가 발생한다. 
    # self.moneys 배열은 정의했지만 이 배열에 무언가를 추가하는 동작이 아무것도 이뤄지지 않았기 때문이다. 
    # 이를 위해서 add 메소드를 정의해줘야 한다. 

    # 위와 같은 문제도 있지만 배열이 비어있어도 코드는 동작해야 한다. 
    def __init__(self) : 
        self.moneys = []

    # 순서 3
    # 이렇게만 정의하면 순서 1에서 정의한 테스트를 통과할 수 있다.
    # 물론, 해당 테스트만 통과한다.
    """ def add(self, *moneys)  : 
        pass

    def evaluate(self, currency) : 
        return Money(15, 'USD') """
    
    # 순서 4
    # evaluate 메소드에 하드코딩된 15를 Money 객체들의 amount를 실제로 합하는 코드로 바꿀 수 있다.
    """ def add(self, *moneys)  : 
        pass

    def evaluate(self, currency) : 
        
        # 람다식을 이용해 self.moneys 배열을 각 Money 객체의 amount로만 구성된 map으로 매핑한다
        # functools.reduce에서 operator.add 연산을 이용해 map을 하나의 값으로 축약한다.
        # 그 값을 total에 할당했다.

        # 여기까지 완료하고 테스트를 실행하면 당연히 self.moneys를 아직 선언하지 않았기 때문에 
        # 오류가 발생한다. 
        total = functools.reduce(
            operator.add, map(lambda m: m.amount, self.moneys)
        )

        return Money(total, currency) """
    
    # 순서 6
    # 아래와 같이 메소드들을 정의하고 나면 모든 테스트가 제대로 동작한다.

    # 물론, 아직 다른 통화간의 덧셈 식이 제대로 동작하는지는 확인되지 않았지만
    # 분할 정복 전략을 사용하여 
    # 두 개의 Money 엔티티들을 더하고 같은 통화의 모든 Portfoilo의 값들을 계산하는 것 까지는 확인했다.
    def add(self, *moneys)  : 
        self.moneys.extend(moneys) # 전달받는 Money 엔티티들을 배열에 추가

    def evaluate(self, currency) : 

        # 누적되는 결과의 초기값을 0으로 설정 
        total = functools.reduce(
            operator.add, map(lambda m: m.amount, self.moneys), 0
        )

        return Money(total, currency)


class TestMoney(unittest.TestCase) : 

    def testMultiplicationInDollars(self) : 

        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')

        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuros(self) : 

        tenEuros = Money(10, "EUR")         
        twentyEuros = Money(20, "EUR")

        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self) : 
        originalMoney = Money(4002, 'KRW')
        expectedMoneyAfterDivision = Money(1000.5, 'KRW')

        self.assertEqual(expectedMoneyAfterDivision, originalMoney.divide(4))

    # 순서 1 
    # 통화가 같기 때문에 계산식 자체는 문제가 될 게 없다.
    # 다만, Portfolio를 정의하지 않았기 때문에 당연히 오류가 발생한다. 
    def testAddition(self) : 
        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')
        fiftennDollars = Money(15, 'USD')

        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)

        self.assertEqual(fiftennDollars, portfolio.evaluate('USD'))

    

if __name__ == '__main__' : 
    unittest.main()