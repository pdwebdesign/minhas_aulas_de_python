import pandas as pd
import numpy as np

df = pd.read_csv('Salaries.csv',low_memory=False)
#df = pandas.read_csv(file_path)
for pessoa_index, pessoa in df.iterrows():
    pessoa_nome = pessoa['EmployeeName']
    pessoa_salario = pessoa['BasePay']
    print(df)
