# AlgoritmoDeSubstituicaoDePaginas
TRABALHO REALIZADO PARA COMPOSIÇÃO DA NP1 - SISTEMAS OPERACIONAIS ABERTOS_SOA

VITOR FERNANDES BARBARULO D6929J-0 -SI6P68

Em sistemas operacionais de computador que usam paginação para gerenciar a memória virtual, o algoritmo de mudança de página determina quais páginas de memória serão gravadas no disco quando novas páginas precisarem ser alocadas. A paginação ocorre quando ocorre uma falha de página e as páginas livres não podem ser usadas para satisfazer a alocação, geralmente porque não há páginas suficientes para atender a esse requisito.
Quando a página selecionada e reproduzida no disco for referenciada novamente, a página será carregada do disco novamente, o que envolve operações de entrada / saída. Isso determina a qualidade do algoritmo de paginação: quanto menos tempo leva para recarregar a página, mais eficaz e melhor é o algoritmo. O algoritmo de mudança de página tem informações limitadas sobre o acesso disponível do hardware e tenta adivinhar quais páginas devem ser substituídas para minimizar o número total de falhas de página, equilibrando assim os custos operacionais envolvidos.
O código a seguir, com um algoritmo de substituição de páginas, foi criado em linguagem Python.
