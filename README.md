Explicação do Código
Este script em Python foi projetado para calcular a carga térmica de um ambiente ou sala e recomendar o tamanho apropriado de um condicionador de ar com base nessa carga. Ele inclui várias funções e solicitações de entrada para coletar informações sobre a sala e seus componentes. Veja como o código funciona:

Definições de Tabela: O código começa definindo várias tabelas/constantes para diferentes parâmetros relacionados ao ambiente, incluindo o número de andares, presença de janelas, portas, pessoas e aparelhos elétricos. Esses valores são usados em cálculos subsequentes.

Função para Validar Entradas Decimais: A função decimal é definida para garantir que os valores de entrada para dimensões sejam ou inteiros ou números de ponto flutuante. Ela verifica se a entrada pode ser convertida em um valor numérico válido.

Função recinto: Esta função é usada para coletar informações sobre o ambiente e calcular a carga térmica. Ela pergunta ao usuário sobre as dimensões da sala, o número de andares e se a sala tem uma conexão direta com o telhado. Ela calcula o volume da sala e a carga térmica com base no número de andares e na presença de uma conexão com o telhado.

Função tabela_janela: Se houver janelas na sala, esta função é chamada para coletar informações sobre cada janela. Ela pergunta ao usuário sobre as propriedades da janela (exposição ao sol de manhã ou tarde, presença de cortinas, dimensões) e calcula a carga térmica contribuída por cada janela.

Função tabela_porta: Se houver portas na sala, esta função é chamada para coletar informações sobre cada porta. Ela pergunta ao usuário sobre as dimensões da porta e calcula a carga térmica contribuída por cada porta.

Função tabela_pessoas: Esta função coleta o número de pessoas na sala e calcula a carga térmica contribuída por elas.

Função tabela_watt_nominal: Esta função coleta informações sobre a potência nominal de aparelhos elétricos na sala e calcula a carga térmica contribuída por eles.

Função final: Esta função exibe os resultados, incluindo as cargas térmicas de diferentes fontes (sala, janelas, portas, pessoas e aparelhos). Em seguida, ela calcula a carga térmica total em Kcal/h e a converte para BTU. Ela recomenda um condicionador de ar apropriado com base na carga total de BTU requerida e exibe o modelo e o preço.

Execução: O código começa chamando a função recinto para iniciar o processo e orienta o usuário por meio de várias solicitações de entrada.
