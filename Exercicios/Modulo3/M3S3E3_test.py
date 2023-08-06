import M3S3E3


def test_gerar_codigo_lista_vazia():
    pecas = []
    codigo = gerar_codigo(pecas)
    assert codigo == 1

def test_gerar_codigo_lista_nao_vazia():
    pecas = [{'codigo': 1}]
    codigo = gerar_codigo(pecas)
    assert codigo == 2

def test_cadastrar_peca(mocker):
    pecas = []
    mocker.patch('builtins.input', side_effect=["Nome da Peça", "Fabricante", "10.0"])
    cadastrar_peca(pecas)
    assert len(pecas) == 1

def test_imprimir_peca(capsys):
    peca = {'codigo': 1, 'fabricante': 'Fabricante 1', 'valor': 10.0}
    imprimir_peca(peca)
    captured = capsys.readouterr()
    assert 'Código: 001' in captured.out
    assert 'Fabricante: Fabricante 1' in captured.out
    assert 'Valor: 10.00 R$' in captured.out

def test_consultar_pecas(mocker, capsys):
    pecas = [{'codigo': 1, 'fabricante': 'Fabricante 1', 'valor': 10.0}]
    mocker.patch('builtins.input', side_effect=["1", "4"])
    consultar_pecas(pecas)
    captured = capsys.readouterr()
    assert 'Código: 001' in captured.out
    assert 'Fabricante: Fabricante 1' in captured.out
    assert 'Valor: 10.00 R$' in captured.out

def test_remover_peca(mocker):
    pecas = [{'codigo': 1}]
    mocker.patch('builtins.input', side_effect=["1"])
    remover_peca(pecas)
    assert len(pecas) == 0
