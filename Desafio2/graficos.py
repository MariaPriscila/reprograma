import pandas as pd
import matplotlib.pyplot as plt

# Dados para o gráfico de barras
dados_barras = {
    'Renda mensal per capita': ['Até 1 salário mínimo', 'De 1 a 3 salários', 'De 3 a 5 salários', 'Acima de 5 salários'],
    'Antes do curso': [12, 44, 8, 36],
    'Após o curso': [8, 22, 38, 32]
}

# Dados para o gráfico de pizza
dados_pizza = {
    'Situação de emprego': ['Empregada', 'Desempregada'],
    'Antes do curso': [66, 34],
    'Após o curso': [78, 22]
}

# Dados para o gráfico de rosca
dados_rosca = {
    'Emprego na área de TI': ['Na área de TI', 'Fora da área de TI', 'Desempregada'],
    'Antes do curso': [12, 54, 34],
    'Após o curso': [72, 28, 0]
}

# Dados para o gráfico de barras agrupadas
dados_barras_agrupadas = {
    'Suficiência de renda': ['Antes do curso', 'Após o curso'],
    'Suficiente': [56, 63],
    'Insuficiente': [44, 37]
}

# Criação dos DataFrames
df_barras = pd.DataFrame(dados_barras)
df_pizza = pd.DataFrame(dados_pizza)
df_rosca = pd.DataFrame(dados_rosca)
df_barras_agrupadas = pd.DataFrame(dados_barras_agrupadas)

# Estilo dos gráficos com cor lilás e derivados
plt.style.use('seaborn-pastel')
cores = ['#a683ba', '#b399cc', '#bfaedf', '#cec4f2']

# Gráfico de barras
ax = df_barras.set_index('Renda mensal per capita').plot(kind='bar', figsize=(8, 6), color=cores)
ax.set_ylabel('Porcentagem')
ax.set_title('Renda mensal per capita antes e após o curso {reprograma}')
plt.savefig('grafico_barras.png', bbox_inches='tight')

# Gráfico de pizza
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
df_pizza.plot(kind='pie', y='Antes do curso', labels=df_pizza['Situação de emprego'], autopct='%1.1f%%', legend=False, ax=axes[0], colors=cores)
df_pizza.plot(kind='pie', y='Após o curso', labels=df_pizza['Situação de emprego'], autopct='%1.1f%%', legend=False, ax=axes[1], colors=cores)
axes[0].set_title('Antes do curso {reprograma}')
axes[1].set_title('Após o curso {reprograma}')
plt.gca().add_artist(plt.Circle((0, 0), 0.5, fc='white'))
plt.savefig('grafico_pizza.png', bbox_inches='tight')

# Gráfico de rosca
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
df_rosca.plot(kind='pie', y='Antes do curso', labels=df_rosca['Emprego na área de TI'], autopct='%1.1f%%', legend=False, ax=axes[0], colors=cores)
df_rosca.plot(kind='pie', y='Após o curso', labels=df_rosca['Emprego na área de TI'], autopct='%1.1f%%', legend=False, ax=axes[1], colors=cores)
axes[0].set_title('Antes do curso {reprograma}')
axes[1].set_title('Após o curso {reprograma}')
plt.gca().add_artist(plt.Circle((0, 0), 0.5, fc='white'))
plt.savefig('grafico_rosca.png', bbox_inches='tight')

# Gráfico de barras agrupadas
ax = df_barras_agrupadas.set_index('Suficiência de renda').plot(kind='bar', figsize=(6, 6), color=cores)
ax.set_ylabel('Porcentagem')
ax.set_title('Suficiência de renda antes e após o curso {reprograma}')
plt.savefig('grafico_barras_agrupadas.png', bbox_inches='tight')

# Criação do arquivo com todos os dados
df_dados = pd.concat([df_barras, df_pizza.drop(columns='Situação de emprego'), df_rosca.drop(columns='Emprego na área de TI'), df_barras_agrupadas])
df_dados.to_csv('dados_reprograma.csv', index=False)
