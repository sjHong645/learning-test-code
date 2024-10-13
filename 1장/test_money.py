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

# RED를 진행하고 나서 만든 Dollar 클래스 
class Dollar : 

    # 순서 3
    # 1. 클래스 자체를 만들기는 했으나 아직 아무런 인자를 받을 수 없다.
    """
    pass
    """

    # 순서 4
    # 2. 테스트 내용을 보면 1개의 인자를 받아야 한다.
    # 물론, 이것만 작성하면 또 실패한다. 
    # times 라는 메소드가 구현되어 있지 않기 때문이다.
    """ def __init__(self, amount) : 
        pass """

    # 순서 5
    # 3. 테스트를 통과하려면 10달러를 반환해야 한다.
    # 그러니 times의 반환값이 10달러가 되도록 고정했다. 
    """ def __init__(self, amount) : 
        self.amount = amount

    def times(self, multiplier) : 
        return Dollar(10) """
    
    # 순서 6
    # Refactor 진행
    # 물론, 앞서 실행한 3번은 하드코딩을 이용해 테스트를 성공한 것이다. 
    def __init__(self, amount) : 
        self.amount = amount

    def times(self, multiplier) : 
        return Dollar(self.amount * multiplier)




class TestMoney(unittest.TestCase) : 

    # 5 USD * 2 = 10 USD가 되는지를 테스트하는 메소드
    def testMultiplication(self) : 

        # 순서 1
        # RED 
        # 간단한 산술연산 테스트를 통과하는 최소한의 코드를 작성했다. 
        # 아직 Dollar 클래스를 정의하지 않았기 때문에 실패한다.
        """ fiver = Dollar(5)
        tenner = fiver.times(2)

        self.assertEqual(10, tenner.amount) """

        
        # 순서 2
        # GREEN
        # Dollar의 abstraction을 만들어야 테스트를 통과할 수 있다.
        # 여기서 abstraction 이란 소스 코드 상의 구조체나 클래스를 말한다.
        fiver = Dollar(5)
        tenner = fiver.times(2)

        self.assertEqual(10, tenner.amount)

if __name__ == '__main__' : 
    unittest.main()