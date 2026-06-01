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