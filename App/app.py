#Importar as bibliotecas

import streamlit as st
import pandas as pd
import numpy as np

#Criar título para o App

st.title("Aplicativo Dados Esportivos Luciano Félix Macedo")

#Criação da barra lateral

st.sidebar.header("Liga")
selected_Liga = st.sidebar.selectbox('Liga',['Alemanha','Bélgica','Escócia','Espanha','França','Grécia','Holanda','Inglaterra','Italia','Portugal','Turquia']

st.sidebar.header("Temporada")
selected_Temporada = st.sidebar.selectbox('Temporada',['2023/2022','2022/2021','2021/2020','2020/2019','2019/2018','2018/2017','2017/2016','2016/2015','2015/2014','2014/2013']
                                       
#Fazer webscraping Footbal Data


  
def load_data(Liga, Temporada):
  url = "https://www.football-data.co.uk/mmz4281/"+Temporada+"/"+Liga+".csv"
  data = pd.read_csv(url)
  return data

df - load_data(selected_liga, selected_temporada)

