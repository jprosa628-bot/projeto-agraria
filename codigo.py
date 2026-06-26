import pandas as pd

# Lê a planilha sem definir cabeçalho, pois o cabeçalho ocupa várias linhas
df = pd.read_excel("sec21.xlsx", header=None)

# A linha 3 contém os anos e a linha 4 contém as culturas
anos = df.iloc[3]
culturas = df.iloc[4]

# Cria os nomes das colunas no formato "Ano_Cultura"
novas_colunas = []

for ano, cultura in zip(anos, culturas):
    if pd.notna(ano) and pd.notna(cultura):
        novas_colunas.append(f"{ano}_{cultura}")
    else:
        novas_colunas.append(cultura)

# Os dados começam na linha 5
dados = df.iloc[5:].copy()

# Define os novos nomes das colunas
dados.columns = novas_colunas

# Renomeia a coluna da Unidade da Federação
dados.rename(
    columns={"Unidade da Federação": "Uf"},
    inplace=True
)

# Converte a tabela do formato largo para o formato longo
dados_long = dados.melt(
    id_vars=["Uf"],
    var_name="Ano_Cultura",
    value_name="Area_plantada"
)

# Separa a coluna Ano_Cultura em Ano e Cultura
dados_long[["Ano", "Cultura"]] = (
    dados_long["Ano_Cultura"]
    .str.split("_", expand=True)
)

# (Opcional) Remove a coluna original
dados_long.drop(columns=["Ano_Cultura"], inplace=True)

# Exibe o resultado
print(dados_long)

# (Opcional) Salva em Excel
dados_long.to_excel("dados_formatados.xlsx", index=False)