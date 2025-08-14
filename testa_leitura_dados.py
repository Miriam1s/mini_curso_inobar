"""
Script simples para iniciantes: Testa a leitura e limpeza dos dados da lanchonete.
Execute este arquivo para garantir que o pandas está funcionando e os dados estão corretos!
"""
import pandas as pd

# Caminho do arquivo (pode ser local ou online)
url = 'https://raw.githubusercontent.com/Miriam1s/mini_curso_inobar/main/vendas_lanchonete.csv'
df = pd.read_csv(url)

# Limpeza básica (igual ao notebook)
df['ID_Cliente'] = df['ID_Cliente'].fillna(0)
df['Preco'] = df['Preco'].str.replace(',', '.').astype(float)
df['ID_Cliente'] = df['ID_Cliente'].astype(int)
df['Data'] = pd.to_datetime(df['Data'])
df['Total_Venda'] = df['Preco'] * df['Quantidade']

print('Primeiras linhas dos dados:')
print(df.head())
print('\nTipos das colunas:')
print(df.dtypes)
print('\nTudo certo! Se não aparecer erro acima, você está pronto para analisar os dados no notebook.')
