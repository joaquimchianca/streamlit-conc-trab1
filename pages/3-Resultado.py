from operator import itemgetter
import streamlit as st
import pandas as pd
import numpy as np
from data import conc_times, seq_times
import matplotlib.pyplot as plt

st.title('Resultado')

@st.cache_data
def cria_tabela(seq_timestamp, conc_timestamp):
    #Calculo dos tempos para versão sequencial
    seq_media = np.mean(seq_timestamp)
    seq_max = np.max(seq_timestamp)
    seq_min = np.min(seq_timestamp)
    seq_std = np.std(seq_timestamp)
    
    #Calculo dos tempos para versão concorrente
    conc_media = np.mean(conc_timestamp)
    conc_max = np.max(conc_timestamp)
    conc_min = np.min(conc_timestamp)
    conc_std = np.std(conc_timestamp)

    #Criacao do dataframe para expor dados
    data = {
            'Média': [seq_media, conc_media],
            'Máximo': [seq_max, conc_max],
            'Mínimo': [seq_min, conc_min],
            'Desvio Padrão': [seq_std, conc_std]
    }
    df = pd.DataFrame(data)
    return df

tabelas = []
for i in range(10):    
    tabelas.append(cria_tabela(seq_times[i], conc_times[i]))

st.header('Tabelas')
st.write("O tempo das tabelas está em milissegundos.")
st.write("0 - Versão Sequencial")
st.write("1 - Versão Concorrente")

col1, col2 = st.columns(2)
col1.subheader('A.in')
col1.dataframe(tabelas[0])
col2.subheader('B.in')
col2.dataframe(tabelas[1])

col1.subheader('C.in')
col1.dataframe(tabelas[2])
col2.subheader('D.in')
col2.dataframe(tabelas[3])

col1.subheader('E.in')
col1.dataframe(tabelas[4])
col2.subheader('F.in')
col2.dataframe(tabelas[5])

col1.subheader('G.in')
col1.dataframe(tabelas[6])
col2.subheader('H.in')
col2.dataframe(tabelas[7])

col1.subheader('I.in')
col1.dataframe(tabelas[8])
col2.subheader('J.in')
col2.dataframe(tabelas[9])

st.header('Gráfico')
seq_media = []
conc_media = []

arquivos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for tabela in tabelas:
    seq_media.append(tabela.loc[0, "Média"])
    conc_media.append(tabela.loc[1, "Média"])


fig, ax = plt.subplots()
ax.plot(arquivos, seq_media, label='Versão Sequencial')
ax.plot(arquivos, conc_media, label='Versão Concorrente')
ax.legend()
ax.set_xlabel('Arquivo de Teste')
ax.set_ylabel('Tempo médio (ms)')
ax.grid(alpha=0.2)
st.pyplot(fig=fig)

st.subheader('Ganho de desempenho')
st.write('Cálculo do ganho de desempenho por arquivo de entrada.')

performance = []
for i in range(10):
     performance.append(seq_media[i] / conc_media[i])

desempenho = {
    "A.in": round(performance[0], 3),
    "B.in": round(performance[1], 3),
    "C.in": round(performance[2], 3),
    "D.in": round(performance[3], 3),
    "E.in": round(performance[4], 3),
    "F.in": round(performance[5], 3),
    "G.in": round(performance[6], 3),
    "H.in": round(performance[7], 3),
    "I.in": round(performance[8], 3),
    "J.in": round(performance[9], 3),
}

st.json(desempenho)
st.write("Ganho de desempenho médio: ", round(np.mean(list(desempenho.values())), 3))
    