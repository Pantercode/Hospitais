#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd


# In[48]:




pessoas = [
     {'Nome': "Carlos", 'Profissão': 'oncologista', 'Local_trabalho': "hospital", 'Estado': "MG"},
     {'Nome': "Ana", 'Profissão': "dentista", 'Local_trabalho': "clinica", 'Estado': "SP"},
     {'Nome': "Fernanda", 'Profissão': "enfermeira", 'Local_trabalho': "hospital", 'Estado': "AM"},
     {'Nome': "Sandra", 'Profissão': "pediatra", 'Local_trabalho': "clinica", 'Estado': "PE"},
     {'Nome': "Fatima", 'Profissão': "dentista", 'Local_trabalho': "clinica", 'Estado': "MA"},
     {'Nome': "Gilmar", 'Profissão': "cardiologista", 'Local_trabalho': "hospital", 'Estado': "RR"},
     {'Nome': "Fabio", 'Profissão': "pediatra", 'Local_trabalho': "clinica", 'Estado': "RO"},
     {'Nome': "Hilton", 'Profissão': "enfermeiro", 'Local_trabalho': "clinica", 'Estado': "SC"},
     {'Nome': "Paulo", 'Profissão': "farmaceutico", 'Local_trabalho': "clinica", 'Estado': "BA"},
     {'Nome': "Gilberto", 'Profissão': "pediatra", 'Local_trabalho': "hospital", 'Estado': "PB"}
]

df_p = pd.DataFrame(pessoas)



# In[63]:


df_p


# In[66]:


df_p['Profissão'] = df_p['Profissão'].str.capitalize()
df_p['Local_trabalho'] = df_p['Local_trabalho'].str.capitalize()
df_p


# In[50]:


df = pd.read_csv("Salario.txt", sep=",")


# In[51]:


df


# In[52]:


df = df.rename(columns={'Carlos': 'Colaborador', '1000': 'Sálario'})


# In[53]:


df


# In[54]:


salario = [
    {'Colaborador': "Carlos", 'Salário': '10000'}
]
df2 = pd.DataFrame(salario)


# In[55]:


df2


# In[56]:


df_sal = pd.concat([df, df2], ignore_index=True)


# In[57]:


df_sal 


# In[60]:


df_sal = df.rename(columns={'10000': 'Sálario'})


# In[61]:


df_sal

