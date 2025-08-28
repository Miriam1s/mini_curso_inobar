import pandas as pd

def test_leitura_vendas():
    try:
        df = pd.read_csv('vendas_lanchonete.csv')
        assert not df.empty, 'Arquivo de vendas está vazio.'
        assert 'Produto' in df.columns, 'Coluna Produto não encontrada.'
        assert 'Quantidade' in df.columns, 'Coluna Quantidade não encontrada.'
        print('Teste de leitura de vendas: OK')
    except Exception as e:
        print(f'Falha no teste de leitura de vendas: {e}')

def test_leitura_clientes():
    try:
        df = pd.read_csv('clientes.csv')
        assert not df.empty, 'Arquivo de clientes está vazio.'
        assert 'ID_Cliente' in df.columns, 'Coluna ID_Cliente não encontrada.'
        print('Teste de leitura de clientes: OK')
    except Exception as e:
        print(f'Falha no teste de leitura de clientes: {e}')

if __name__ == '__main__':
    test_leitura_vendas()
    test_leitura_clientes()
