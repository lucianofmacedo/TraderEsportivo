import streamlit as st
import pandas as pd
import numpy as np
import base64

st.title("App Análise Luciano Félix Macedo")

st.sidebar.header("Liga")
selected_league = st.sidebar.selectbox('Liga',['Alemanha - Bundesliga 1','Alemanha - Bundesliga 2','Bélgica - Liga Jupiler','Escócia - Premiere League','Escócia - Divisão 1','Escócia - Divisão 2','Escócia - Divisão 3','Espanha - La Liga 1','Espanha - La Liga 2','França - League 1','França - League 2','Grécia - Super Liga','Holanda - Eredivisie','Inglaterra - Premiere League','Inglaterra - Championship','Inglaterra - League 1','Inglaterra - League 2','Inglaterra - Conference','Italia 1','Itália - Serie A','Itália - Serie B','Portugal - Liga 1','Turquia - Super Liga'])

st.sidebar.header("Temporada")
selected_season = st.sidebar.selectbox('Temporada', ['2022/2023','2021/2022','2020/2021','2019/2020','2018/2019','2017/2018','2016/2017','2015/2016','2014/2015','2013/2014'])

# WebScraping Football Data
def load_data(league, season):
  
  if selected_league == 'Alemanha - Bundesliga 1':
    league = 'D1'
  if selected_league == 'Alemanha - Bundesliga 2':
    league = 'D2'
  if selected_league == 'Bélgica - Liga Jupiler':
    league = 'B1'
  if selected_league == 'Escócia - Premiere League':
    league = 'SC0'
  if selected_league == 'Escócia - Divisão 1':
    league = 'SC1'
  if selected_league == 'Escócia - Divisão 2':
    league = 'SC2'
  if selected_league == 'Escócia - Divisão 3':
    league = 'SC3'
  if selected_league == 'Espanha - La Liga 1':
    league = 'SP1'
  if selected_league == 'Espanha - La Liga 2':
    league = 'SP2'
  if selected_league == 'França - League 1':
    league = 'F1'
  if selected_league == 'França - League 2':
    league = 'F2'
  if selected_league == 'Grécia - Super Liga':
    league = 'G1'
  if selected_league == 'Holanda - Eredivisie':
    league = 'N1'
  if selected_league == 'Inglaterra - Premiere League':
    league = 'E0'
  if selected_league == 'Inglaterra - Championship':
    league = 'E1'
  if selected_league == 'Inglaterra - League 1':
    league = 'E2'
  if selected_league == 'Inglaterra - League 2':
    league = 'E3'
  if selected_league == 'Inglaterra - Conference':
    league = 'E4'
  if selected_league == 'Itália - Serie A':
    league = 'I1'
  if selected_league == 'Itália - Serie B':
    league = 'I2'
  if selected_league == 'Portugal - Liga 1':
    league = 'P1'
  if selected_league == 'Turquia - Super Liga':
    league = 'T1'
    
  if selected_season == '2022/2023':
    season = '2223'
  if selected_season == '2021/2022':
    season = '2122'
  if selected_season == '2020/2021':
    season = '2021'
  if selected_season == '2019/2020':
    season = '1920'
  if selected_season == '2018/2019':
    season = '1819'
  if selected_season == '2017/2018':
    season = '1718'
  if selected_season == '2016/2017':
    season = '1617'
  if selected_season == '2015/2016':
    season = '1516'
  if selected_season == '2014/2015':
    season = '1415'
  if selected_season == '2013/2014':
    season = '1314'
    
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

st.title("App Análise Luciano Félix Macedo")
