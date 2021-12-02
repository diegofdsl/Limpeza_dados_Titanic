

#Importando Bibliotecas


import pandas as pd
import seaborn as sns

#Lendo o dataset

data=pd.read_csv(r'C:\Users\User\Downloads\train.csv')

#Pré visualizando os dados

display(data)

#Verificando os NAN

data.isnull().sum()

#Renomeando as colunas para Português

data.columns = ['IDPassageiro', 'Sobreviveu', 'ClasseSocial','Nome', 'Sexo', 'Idade', 'IrmãosConjugue',
       'Pais_Filhos', 'Ticket', 'Tarifa', 'Cabine', 'Embarque']


#Descrevendo os dados de forma estatística


data.describe()


#Limpando os NaN


data.describe(include='O')

data['Idade'].mean()

data['Idade'].fillna('29',downcast=dict ,inplace=True)

#Transformando os tipos de dados na coluna Idade

data['Idade']=pd.to_numeric(data['Idade'])


data['Sexo']=data['Sexo'].map({'male':'Homem','female':'Mulher'})


data.loc[data['Embarque'].isnull()]

data['Embarque'].unique()


data['Embarque'].mode()


data['Embarque'].fillna('S',inplace=True)


data.drop('Cabine',axis=1,inplace=True)



# # Gerando correlação linear entre as colunas

sns.heatmap(data.corr())


sns.heatmap(data.corr(),annot=True)


sns.heatmap(data.corr(),annot=True,vmin=-1,vmax=1)

sns.heatmap(data.corr(),annot=True,cmap='coolwarm')


