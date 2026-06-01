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

