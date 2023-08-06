
import M3S3E2

def test_ler_dimensoes_objeto():
    preco_volume = M3S3E2.ler_dimensoes_objeto()
    assert preco_volume == 6000.0

def test_ler_peso_objeto():
    multiplicador_peso = M3S3E2.ler_peso_objeto()
    assert multiplicador_peso == 2.0

def test_ler_rota():
    multiplicador_rota = M3S3E2.ler_rota()
    assert multiplicador_rota == 1.5


def test_calcular_frete():
    total = M3S3E2.calcular_frete(5000, 2.0, 1.5)
    assert total == 15000.0
