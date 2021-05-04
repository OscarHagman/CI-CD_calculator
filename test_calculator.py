from calculator import Calc


class TestCalc:
    def test_add(self):
        assert 4 == Calc.add(2, 2)
        assert 10 == Calc.add(4, 6)

    def test_sub(self):
        assert 5 == Calc.sub(6, 1)
        assert 10 == Calc.sub(20, 10)

    def test_mul(self):
        assert 100 == Calc.mul(10, 10)
        assert 50 == Calc.mul(5, 10)
