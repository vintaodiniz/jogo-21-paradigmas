# Projeto Jogo 21 (Blackjack) - Avaliação de Paradigmas de Programação

Repositório do projeto avaliativo da disciplina de Paradigmas de Programação, ministrada pelo professor Rodrigo Medeiros Costa no curso de Ciência da Computação da Universidade da Amazônia (UNAMA). Este projeto propõe a resolução de um problema computacional de baixa a média complexidade, construído integralmente com a linguagem Python e aplicando os conceitos do paradigma imperativo.

## Integrantes e Contribuições
A atividade foi desenvolvida em grupo, com a participação e contribuição de cada integrante dividida da seguinte forma:
* **Victor Tadeu Diniz Kos Silva (GitHub: vintaodiniz):** Responsável pela criação das pastas do projeto, pela organização do ficheiro `main.py` e pela criação deste `README`.
* **[Nome do Integrante 2]:** [Escrevam o que vocês fizeram aqui]
* **Alexandre (completar nome e usuário do GitHub):** Responsável pelo módulo `economia.py`: saldo inicial, validação das apostas, atualização do saldo e condições de encerramento, com testes do módulo.

## Descrição do Problema
O problema escolhido consiste no desenvolvimento de um simulador em modo texto do clássico Jogo 21 (Blackjack), acrescido de um sistema de gestão de saldo bancário. O objetivo é criar uma lógica de execução clara onde o estado dos dados financeiros e de pontuação é alterado ao longo do processamento. A seguir, detalham-se as entradas, regras e os resultados esperados:
* **Entradas:** Opções de navegação do menu principal numérico, decisões do jogador durante a partida (pedir nova carta ou parar) e os valores inteiros inseridos para as apostas a cada rodada.
* **Regras Principais:** O jogador inicia com um saldo de R$ 1000. O objetivo de cada rodada é somar 21 pontos ou chegar o mais próximo possível sem ultrapassar esse limite. Cartas numéricas de 2 a 10 mantêm o seu valor nominal, enquanto figuras (J, Q, K) valem 10 pontos. 
* **Resultados Esperados:** O programa deve calcular os pontos da rodada, determinar o vencedor (jogador ou máquina), atualizar o saldo da banca e exibir os valores na tela. O jogo encerra automaticamente se a banca for zerada (derrota) ou se o jogador atingir a meta estipulada de R$ 50.000 (vitória).

## Instruções de Execução
Para testar a solução, é necessário cumprir os requisitos básicos e executar os passos abaixo:
1. Certifique-se de que o interpretador **Python 3.x** está instalado no seu sistema operativo.
2. Faça o clone deste repositório ou descarregue os ficheiros fonte contidos nele.
3. Abra um terminal (ou prompt de comando) e navegue até à pasta raiz do projeto.
4. Execute o comando: `python main.py`

## Explicação da Solução e Elementos Imperativos
O projeto foi modularizado em diferentes ficheiros para organizar a solução e demonstrar como o estado dos dados é modificado durante o fluxo de execução. A lógica do programa utiliza os seguintes recursos do paradigma imperativo:
* **Variáveis e Atribuições:** Uso constante de variáveis de estado (como a variável `saldo` e listas de `cartas`) que sofrem reatribuições diretas para registar ganhos ou perdas após cada rodada.
* **Sequência de Instruções:** O programa segue um fluxo ordenado no ficheiro central, invocando as regras de economia e lógica de cartas numa ordem rigorosa de processamento para garantir o funcionamento do jogo.
* **Estruturas de Decisão:** Utilização de instruções `if/elif/else` para avaliar quem venceu a rodada, validar o limite de pontos (21) e bloquear apostas que superem o saldo atual.
* **Estruturas de Repetição:** Implementação de laços `while` que mantêm o menu em funcionamento e controlam o ciclo de rodadas ativas enquanto o jogador possuir saldo maior que zero.
* **Funções ou Procedimentos:** Criação de sub-rotinas (como `exibir_regras()`, `calcular_pontos()` e `gerenciar_aposta()`) que encapsulam lógicas específicas, organizando o código e evitando repetição.

## Reflexão sobre o Desenvolvimento
Nesta etapa, relatamos o processo de construção da solução pela equipa, abordando decisões, dificuldades e possíveis melhorias:
* **Decisões:** A principal decisão do grupo foi modularizar o código separando a interface (`main.py`), as regras de negócio (`logica.py`) e o controle financeiro (`economia.py`). Isso facilitou o uso do versionamento no Git, permitindo commits paralelos sem conflitos severos.
* **Dificuldades:** A maior dificuldade mesmo foi em relação ao nosso tempo para realizar o projeto, pois o mesmo foi realizado em periodo de prova então tentamos fazer algo rapido e funcional.
* **Possíveis Melhorias:** seria interessante uma interfacee melhor e efeitos sonoros `.txt`].

## Módulo de economia (Alexandre)

O módulo usa valores inteiros em reais. Cada nova partida começa com R$ 1.000.
Entradas inválidas repetem a pergunta até uma aposta positiva e dentro do saldo.
É permitido apostar todo o saldo. Sem saldo, `gerenciar_aposta` retorna `0` e a
rodada não deve começar.

Na regra simplificada adotada, vitória rende o valor da aposta, derrota perde o
valor da aposta e empate não altera o saldo. Não há pagamento especial por 21.
Exemplo: com saldo de R$ 1.000 e aposta de R$ 100, o resultado será R$ 1.100,
R$ 900 ou R$ 1.000, respectivamente.

### Integração com as rodadas

`main.py` ainda contém somente o menu e `logica.py` está vazio nesta branch.
Portanto, o módulo está disponível, mas o jogo completo ainda precisa ser integrado.
A equipe deve seguir esta sequência:

1. Chamar `inicializar_banca()` uma vez ao iniciar uma nova partida.
2. Verificar `verificar_fim_jogo(saldo)` antes de começar outra rodada.
3. Obter `aposta = gerenciar_aposta(saldo)`; não jogar se retornar `0`.
4. Determinar o resultado com a lógica de cartas: `"vitoria"`, `"derrota"` ou
   `"empate"`, sempre do ponto de vista do jogador.
5. Executar `saldo = atualizar_saldo(saldo, aposta, resultado)` uma única vez.
6. Exibir o saldo e verificar novamente a condição de encerramento.

**Não descontar a aposta antes de chamar `atualizar_saldo`.** Essa função já
calcula o ganho ou a perda líquidos. Ela rejeita apostas e resultados inválidos
com `ValueError`, para detectar erros na integração.

### Conceitos imperativos presentes na economia

- Sequência: ler a aposta, validar, calcular o saldo e verificar o encerramento.
- Variáveis e atribuições: `saldo_atual = saldo_atual + aposta` altera o estado
  local; quem chama a função guarda o retorno na variável `saldo`.
- Decisões: `if/elif/else` valida apostas e seleciona o resultado da rodada.
- Repetição: `while True` repete a leitura quando a entrada é inválida.
- Funções: cada etapa financeira tem uma função própria.
- Tratamento de entrada: `try/except ValueError` trata textos que não são inteiros.

### Validação e decisões do módulo

Execute `python -m unittest -v test_economia` na pasta do projeto. Os testes
usam apenas a biblioteca padrão do Python e verificam entradas inválidas,
ganhos, perdas, empates, aposta de toda a banca, reinício e limites da meta.
As classes no arquivo de testes pertencem ao framework `unittest`; o módulo
do jogo foi implementado com funções e estruturas imperativas.

Foram usados inteiros para acompanhar a regra de apostas do README e uma única
função para liquidar a rodada. Um cuidado de integração é evitar descontar a
aposta duas vezes. Uma possível melhoria é permitir cancelar a aposta e voltar
ao menu. A equipe deve complementar a reflexão com as dificuldades que vivenciou.

## Apresentação do Projeto
Abaixo encontra-se o link com a demonstração da aplicação em pleno funcionamento:
* [**Clique aqui para assistir ao vídeo de apresentação da equipa**](URL_DO_VIDEO_AQUI)
