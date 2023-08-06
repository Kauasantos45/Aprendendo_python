import pytest

from M3S3E1 import calcular_valor_total

def test_calcular_valor_total():
    assert calcular_valor_total(10.0, 5) == (50.0, 50.0)
    assert calcular_valor_total(5.0, 15) == (75.0, 71.25)
    assert calcular_valor_total(20.0, 150) == (3000.0, 2700.0)
    assert calcular_valor_total(8.0, 1200) == (9600.0, 8160.0)

if __name__ == '__main__':
    test_calcular_valor_total()
