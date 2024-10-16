import unittest

# 프로덕션 코드를 다른 파일로 분리하고 나서 import하는 부분
from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase) : 

    # 곱셈에 대한 테스트가 중복되기 때문에 삭제
    # 그리고 Dollar 계산 부분을 지운 이유는 
    # 곱셈은 유로, 나눗셈은 원화, 덧셈은 달러로 진행함으로써 
    # 자연스럽게 하나의 Money 클래스에 대해 서로 다른 통화를 테스트하기 때문이다.
    """ def testMultiplicationInDollars(self) : 

        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')

        self.assertEqual(tenDollars, fiveDollars.times(2)) """

    def testMultiplicationInEuros(self) : 

        tenEuros = Money(10, "EUR")         
        twentyEuros = Money(20, "EUR")

        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self) : 
        originalMoney = Money(4002, 'KRW')
        expectedMoneyAfterDivision = Money(1000.5, 'KRW')

        self.assertEqual(expectedMoneyAfterDivision, originalMoney.divide(4))

    def testAddition(self) : 
        fiveDollars = Money(5, 'USD')
        tenDollars = Money(10, 'USD')
        fiftennDollars = Money(15, 'USD')

        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)

        self.assertEqual(fiftennDollars, portfolio.evaluate('USD'))

    

if __name__ == '__main__' : 
    unittest.main()