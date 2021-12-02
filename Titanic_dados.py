#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando Bibliotecas


# In[2]:


import pandas as pd
import seaborn as sns


# In[3]:


#Lendo o dataset


# In[30]:


data=pd.read_csv(r'C:\Users\User\Downloads\train.csv')


# In[5]:


#Pré visualizando os dados


# In[31]:


display(data)


# In[7]:


#Verificando os NAN

data.isnull().sum()
# In[ ]:


#Renomeando as colunas para Português


# In[9]:


data.columns = ['IDPassageiro', 'Sobreviveu', 'ClasseSocial','Nome', 'Sexo', 'Idade', 'IrmãosConjugue',
       'Pais_Filhos', 'Ticket', 'Tarifa', 'Cabine', 'Embarque']


# In[ ]:


#Descrevendo os dados de forma estatística


# In[10]:


data.describe()


# In[ ]:


#Limpando os NaN


# In[11]:


data.describe(include='O')


# In[12]:


data['Idade'].mean()


# In[13]:


data['Idade'].fillna('29',downcast=dict ,inplace=True)


# In[ ]:


#Transformando os tipos de dados na coluna Idade


# In[14]:


data['Idade']=pd.to_numeric(data['Idade'])


# In[15]:


data['Sexo']=data['Sexo'].map({'male':'Homem','female':'Mulher'})


# In[27]:


data.loc[data['Embarque'].isnull()]


# In[17]:


data['Embarque'].unique()


# In[18]:


data['Embarque'].mode()


# In[19]:


data['Embarque'].fillna('S',inplace=True)


# In[20]:


data.drop('Cabine',axis=1,inplace=True)


# In[21]:


data.corr()


# In[22]:


data.shape


# # Gerando correlação linear entre as colunas

# In[23]:


sns.heatmap(data.corr())


# In[24]:


sns.heatmap(data.corr(),annot=True)


# In[25]:


sns.heatmap(data.corr(),annot=True,vmin=-1,vmax=1)


# In[26]:


sns.heatmap(data.corr(),annot=True,cmap='coolwarm')


# In[32]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




