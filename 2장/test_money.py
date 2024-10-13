"""
    - 간단한 산술연산 (테스트할 내용)
    1. 5 USD * 2 = 10 USD
    2. 10 EUR * 2 = 20 EUR
    3. 4002 KRW / 4 = 1000.5 KRW 

    - 통화 간 환전 (테스트할 내용) - 1 ERU = 1.2 USD / 1 USD = 1100KRW 라고 가정
    1. 5 USD + 10 EUR = 17 USD
    2. 1 USD + 1100 KRW = 2200 KRW
"""

import unittest

# 1장에서 최종적으로 작성한 부분
""" 
class Dollar : 

    def __init__(self, amount) : 
        self.amount = amount

    def times(self, multiplier) : 
        return Dollar(self.amount * multiplier) """
# 순서 3 
# Dollar 클래스를 삭제했다. 
# 왜냐하면, Money 클래스의 기능은 Dollar 클래스의 상위집합이기 때문에 Dollar는 더 이상 필요없다. 
# 이 상태에서 테스트를 실행하면, 기존에 Dollar를 사용했던 테스트는 실패한다. 
# 참고로 테스트 이름은 testMultiplication ==> testMultiplicationInDollars로 변경

    

# 순서 2 
# 정의되지 않은 Money 클래스를 새롭게 정의했다. 
# 정의하면 순서 1에서 작성한 내용의 테스트는 통과한다.
class Money : 

    def __init__(self, amount, currency) : 
        self.amount = amount
        self.currency = currency

    def times(self, multiplier) : 
        return Money(self.amount * multiplier, self.currency)
    
    # 순서 6 
    # divide 메소드를 추가한다. times 메소드는 곱셈을 했으니 여기서는 나눗셈을 하면 된다.
    def divide(self, divisor) : 
        return Money(self.amount / divisor, self.currency)
    
    # 순서 7 
    # 지금까지 테스트했던 내용들을 살펴보면 
    # Money 클래스의 인스턴스들을 가지고 amount, currency 값들이 동일한지 일일이 비교해왔다.
    # 이러한 비교를 한 줄로 해결할 수 있는 방법이 있다. 

    # Python에서 두 객체가 동일한 지 여부는 결국 __eq__ 메소드를 호출하는 것이다. 
    # 해당 메소드에서 정의된 내용에 의해 두 객체가 같으면 true, 아니면 false를 반환한다. 
    # 필요한 경우 __eq__를 오버라이딩 해서 객체의 동일성 여부를 정의할 수 있다. 

    # 아래와 같이 정의하고 나면 1줄로 Money 객체를 비교할 수 있다. 
    def __eq__(self, other) -> bool:
        return self.amount == other.amount and self.currency == other.currency
    

class TestMoney(unittest.TestCase) : 

    # 1장에서 최종적으로 작성한 부분 - 5 USD * 2 = 10 USD
    """ def testMultiplication(self) : 

        fiver = Dollar(5)
        tenner = fiver.times(2)

        self.assertEqual(10, tenner.amount) """
    
    # 순서 4
    # 순서 3에서 Dollar 클래스를 삭제했기 때문에 이 부분도 Money를 이용해서 테스트 코드를 만들어야 한다. 
    # 아래와 같이 수정하고 나면 테스트를 통과하는 걸 확인할 수 있다. 여기서 README.md 파일로 잠시 넘어간다.
    """ def testMultiplicationInDollars(self) : 

        fiver = Money(5, 'USD')
        tenner = fiver.times(2)

        self.assertEqual(10, tenner.amount)
        self.assertEqual('USD', tenner.currency) """

    # 2장에서는 10 EUR * 2 = 20 EUR을 테스트하려 한다. 
    """ def testMultiplicationInEuros(self) : 

        # 순서 1
        # 당연히 Money 클래스를 아직 정의하지 않았기 때문에 테스트는 실패한다.
        tenEuros = Money(10, "EUR") # 이전에 Dollar 클래스에서 정의했던 amount
                                    # 이번에는 통화 단위 currency 정보까지 필요로 하는 Money 클래스가 있으면 좋을 거 같다.
        
        twentyEuros = tenEuros.times(2)

        self.assertEqual(20, twentyEuros.amount)
        self.assertEqual("EUR", twentyEuros.currency) """

    # 순서 5 
    # 4002 KRW / 4 = 1000.5 KRW 를 테스트하려 한다.
    # 이전과 달리 2개의 인스턴스(actualMoneyAfterDivision, expectedMoneyAfterDivision)를 정의했고
    # 당연히 이 상태에서 테스트를 실행하면 divide 메소드를 정의하지 않았기 때문에 실패한다.
    """ def testDivision(self) : 
        originalMoney = Money(4002, 'KRW')
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, 'KRW')

        self.assertEqual(expectedMoneyAfterDivision.amount, actualMoneyAfterDivision.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency, actualMoneyAfterDivision.currency) """
    
    # 순서 7을 적용한 이후
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
    

if __name__ == '__main__' : 
    unittest.main()