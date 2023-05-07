import streamlit as st

st.title('Conclusão')
st.write('''
Feita a análise dos dados, criação de tabelas e geração do gráfico. Podemos notar uma eficiência maior do algoritmo sequencial, desde o arquivo de entrada A.in (arquivo de menor tamanho) até o J.in (de maior tamanho).

Há uma relação entre o tamanho do arquivo e a diferença entre o tempo médio levado para execução da ordenação. Nota-se que à medida que cresce o arquivo de entrada, essa diferença de tempo também cresce - sempre com o algoritmo sequencial se mostrando ser mais eficiente.

A variação do tempo levado em relação à média é menor no programa sequencial, assim podemos inferir uma previsibilidade maior no tempo de execução, pois este varia menos do que na versão concorrente.

Os resultados mostram também a dependência do hardware utilizado para testes, principalmente na implementação do Merge Sort utilizando threads, visto que é utilizado uma pool de threads com número de threads igual ao números de processadores lógicos da máquina utilizada. O aumento desse número de processadores lógicos pode melhorar o desempenho da concorrência. Além disso, não podemos descartar que há possibilidade de uma implementação mais eficiente no que tange utilização dos recursos da máquina.

Por fim, o estudo do "speed-up" (taxa de desempenho dos dois algoritmos) afirma o que foi dito no primeiro parágrafo da conclusão. Em nenhum arquivo de entrada, o "speed-up" apresentou valor maior do que 1 (o que caracterizaria como mais eficiente a versão concorrente).
''')

st.subheader('Referências')
st.markdown('''
- [Guide to Fork/Join Framework in Java, Baeldung](https://www.baeldung.com/java-fork-join)
- [Streamlit API Reference](https://docs.streamlit.io/library/api-reference)
- [Merge sort algorithm, MyCodeSchool (YouTube)](https://www.youtube.com/watch?v=TzeBrDU-JaY)
- [Java Concurrent Package Documentation](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/concurrent/package-summary.html)
- [Introduction to Threads Pool in Java, Baeldung](https://www.baeldung.com/thread-pool-java-and-guava)
- [A Guide to the Java Executor Service, Baeldung](https://www.baeldung.com/java-executor-service-tutorial)
''')