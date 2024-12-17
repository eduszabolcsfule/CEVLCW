import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_excel("data.xlsx")

df = load_data()


st.set_page_config(
    page_title="Óriás Pandák Napi Teendői",
    page_icon="🐼",
    layout="centered"
)
st.title("Óriás Pandák Napi Teendői 🐼")

fig = px.pie(df, 
             names="Tevékenység", 
             values="Órák száma", 
             title="Óriás Pandák Napi Tevékenységei",
             color_discrete_sequence=px.colors.qualitative.Set1)

st.plotly_chart(fig)

