import streamlit as st

st.title('Metodologia')
st.write('''
Para realizar a comparação, foram implementados em linguagem Java duas versões do algoritmo de ordenação Merge Sort, uma sequencial e outra concorrente.

Como ferramenta de versionamento de código, foi utilizado o Github.
''')

st.subheader('Especificações de hardware')
st.markdown('''
 - ***Processador:*** 2,3 GHz Intel Core i5 Quad-Core;
 - ***Sistema Operacional:*** macOS Ventura 13.2;
 - ***Memória:*** 8 GB 2133 MHz LPDDR3.
''')

st.subheader('Compilação')
st.markdown(''' 
 - Java 18 e Maven
''')

st.subheader('Métodos utilizados para experimentação')
st.markdown('''
    Foi criada uma classe Utils para implementação de funções que cuidam das chamadas de abertura escrita dos arquivos. Além disso, foi utilizado na versão concorrente classes do pacote Java 'Concurrent', a ForkMainPool, essa que disponibiliza uma API de performance para programas concorrentes.

    A tomada de decisão do uso da API se deve às falhas encontradas nas primeiras versões do Merge Sort concorrente, em que o compilador lançava o erro java.lang.outOfMemoryError: unable to create new thread. O erro se deve a demasiada quantidade de threads criadas pelo programa, impossibilitando o sistema operacional alocar recursos para criação de todas essas threads.

    O programa Java em si, executa os métodos necessários para ordenação (em ambas versões) e imprime na tela o tempo em milissegundos em que o processador levou para executar a tarefa. A partir da captura dessas marcas de tempo para cada arquivo de entrada utilizado nos testes,temos os dados necessários para obtenção dos resultados do experimento.

    A visualização dos dados foi feita utilizando Python e seus pacotes: Numpy e Pandas (para tratamento e criação das tabelas), Matplotlib (disposição dos dados em gráficos) e Streamlit (biblioteca que implementa uma interface web por meio de simples chamadas de métodos).

    Cada arquivos de teste contém vários números em ordem aleatória, sendo o primeiro arquivo com $2^{10}$ números, o segundo com $2^{11}$ números e seguindo assim até chegar no último, com $2^{19}$ números. Cada um desses arquivos foi executado 25 vezes para cada versão da implementação, seguindo a seguinte lógica:
    - 5 execuções para warm-up;
    - 20 execuções que servem de base para resposta.

    Além disso, foram utilizados Script Shell para automatização dos comandos em Terminal Linux e uso de Makefile junto do Maven para definição das configurações de compilação.
''')