# Mini-Projeto Avaliativo - Análise de Dados com Python
# Autor: Evandro - Turma T1
# Objetivo: Realizar uma Análise Exploratória de Dados (AED) aplicada ao varejo

# Importação das bibliotecas necessárias para o porjeto
import pandas as pd
import numpy as np

# Sprint 1 - Importação dos dados
df = pd.read_csv("Base_Varejo.csv", sep=";", encoding="utf-8")

print("Número de registros:", len(df)) 
print("Colunas da base:", df.columns.tolist())
print("\nTipos de dados:")
print(df.dtypes)

# Remover colunas extras (Unnamed)
df = df.drop(columns=[c for c in df.columns if "Unnamed" in c])

# Sprint 2 - Transformação de tipos
df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')

# Sprint 3 - Limpeza de nulos e duplicatas
print("\nValores nulos por coluna:")
print(df.isnull().sum())

df['PR_CAT'] = df['PR_CAT'].fillna("Sem Categoria")
df = df.drop_duplicates()

print("\nApós limpeza:")
print(df.isnull().sum())

# Sprint 4 - Estatística descritiva (Número de filhos)
col = 'CL_FHL'

print("\nEstatísticas da coluna Número de Filhos:")
print("Média:", df[col].mean())
print("Mediana:", df[col].median())
print("Moda:", df[col].mode()[0])
print("Desvio Padrão:", df[col].std())
print("Máximo:", df[col].max())
print("Mínimo:", df[col].min())
print("Quartis:\n", df[col].quantile([0.25, 0.5, 0.75]))
print("Contagem:", df[col].count())

# Sprint 5 - Agrupamentos
print("\nNúmero de compras por gênero:")
print(df.groupby('CL_GENERO')['CO_ID'].count())

print("\nNúmero de compras por categoria:")
print(df.groupby('PR_CAT')['CO_ID'].count())

# Sprint extra - Validação do identificador de compra (CO_ID)
print("\nVerificação de identificador de compra (CO_ID):")
print("Duplicados em CO_ID:", df['CO_ID'].duplicated().sum())