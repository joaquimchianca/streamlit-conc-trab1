import streamlit as st

st.title('Trabalho Prático: Um estudo empírico sobre programação concorrente com threads')
st.write("""Disciplina: Programação Concorrente

Professor: Everton Cavalcante

Alunos: Bruno Wagner e Joaquim Chianca

Repositório: https://github.com/ufrn-concprog/trabalhoU1-a-team

UFRN - Natal, 2023.

""")

st.header('Introdução')
st.write("""
Este aplicativo analisa o desempenho de duas implementações, em Java, do algoritmo de ordenação Merge Sort - numa versão sequencial e outra concorrente - em relação ao tempo de execução em diferentes tamanhos de entrada. 
    
Os resultados são apresentados em gráficos e tabelas que mostram a diferença de performance da ordenação (em milissegundos), além do tempo máximo, mínimo, médio e desvio padrão para cada cenário de teste em que os dois programas foram submetidos. Também existe o cálculo de ganho de desempenho:

""")
         
st.latex(r'''
S =\frac{T_s}{T_c}
''')

st.markdown("""
sendo $S$ o *speed-up*, $T_s$ o tempo médio despendido pela versão sequencial e $T_c$ o tempo médio despendido pela versão concorrente. Caso o valor do *speed-up* seja superior a 1, tem-se que a versão concorrente é, em média, de fato melhor em termos de desempenho do que a sequencial.

Essa página da web foi feita por meio da biblioteca Streamlit do Python.

As seções do relatório estão localizadas na barra lateral esquerda.
""")

