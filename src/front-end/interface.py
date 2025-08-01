import streamlit as st
import requests

st.title("Guia de Turismo com IA")

tab1, tab2 = st.tabs(["Planejador de Roteiros", "Informações sobre Atrações"])

with tab1:
    st.header("Crie seu roteiro personalizado")
    
    days = st.slider("Número de dias", 1, 14, 3)
    interests = st.multiselect("Seus interesses", 
                             ["História", "Arte", "Natureza", "Gastronomia", "Aventura"])
    budget = st.selectbox("Orçamento", ["Econômico", "Médio", "Alto"])
    
    if st.button("Gerar Roteiro"):
        response = requests.post(
            "http://backend:8000/generate_itinerary",
            json={
                "days": days,
                "interests": interests,
                "budget": budget
            }
        )
        st.write(response.json()["itinerary"])