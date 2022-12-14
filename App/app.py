import streamlit as st
import pandas as pd
import numpy as np
import base64

st.title("App Análise Luciano Félix Macedo")

st.sidebar.header("Liga")
selected_league = st.sidebar.selectbox('Liga',['Alemanha 1','Alemanha 2','Bélgica','Escócia 1','Escócia 2','Escócia 3','Escócia 4','Espanha 1','Espanha 2','França 1','França 2','Grécia','Holanda','Inglaterra 1','Inglaterra 2','Inglaterra 3','Inglaterra 4','Inglaterra 5','Italia 1','Italia 2','Portugal','Turquia'])

st.sidebar.header("Temporada")
selected_season = st.sidebar.selectbox('Temporada', ['2021/2022','2020/2021','2019/2020'])

# WebScraping Football Data
def load_data(league, season):
  
  if selected_league == 'England':
    league = 'E0'
  if selected_league == 'Germany':
    league = 'D1'
  if selected_league == 'Italy':
    league = 'I1'
  if selected_league == 'Spain':
    league = 'SP1'
  if selected_league == 'France':
    league = 'F1'
   
  if selected_season == '2021/2022':
    season = '2122'
  if selected_season == '2020/2021':
    season = '2021'
  if selected_season == '2019/2020':
    season = '1920'
    
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)

st.subheader("Liga: "+selected_league)
st.dataframe(df)

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="Base_de_Dados.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df), unsafe_allow_html=True)
