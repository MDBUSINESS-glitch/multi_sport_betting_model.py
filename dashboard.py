import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard de Apostas NBA")

# Carregar dados
data = pd.read_csv('betting_results.csv')

# Métricas
total_pl = data['Profit_Loss'].sum()
win_rate = (data['Profit_Loss'] > 0).mean() * 100 if not data.empty else 0
st.metric("Profit/Loss Total", f"R$ {total_pl:.2f}")
st.metric("Taxa de Acerto", f"{win_rate:.2f}%")
st.metric("ROI", f"{(total_pl / (len(data) * 10)) * 100:.2f}%" if not data.empty else "0%")

# Tabela
st.subheader("Histórico de Apostas")
st.dataframe(data)

# Gráfico
st.subheader("Gráfico de Profit/Loss Cumulativo")
if not data.empty:
    data['Cumulative_PL'] = data['Profit_Loss'].cumsum()
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Cumulative_PL'])
    st.pyplot(fig)

# Resultados por Jogador
st.subheader("Resultados por Jogador")
if not data.empty:
    player_pl = data.groupby('Player')['Profit_Loss'].sum()
    st.bar_chart(player_pl)

# Filtro
if not data.empty:
    player_filter = st.selectbox("Filtrar por Jogador", data['Player'].unique())
    filtered = data[data['Player'] == player_filter]
    st.dataframe(filtered)