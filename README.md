# Sistema de Logística Portuária

Aplicação de terminal em Python para gerenciar a operação básica de um porto. O projeto foi feito para praticar estruturas de dados clássicas, e cada área do sistema usa uma estrutura diferente.

## Estruturas de dados utilizadas

| Módulo | Estrutura | Implementação |
|---|---|---|
| Frota de veículos | Lista | `list` do Python |
| Fila de caminhões | Fila (FIFO) | `queue.Queue` |
| Pilha de contêineres | Pilha (LIFO) | `list` com `append()` e `pop()` |
| Rotas entre portos | Árvore | Dicionários aninhados |

## Justificativa da escolha das estruturas de dados

**Lista – Gerenciamento da frota de veículos**

A lista foi escolhida para armazenar os veículos cadastrados no sistema, pois permite manter vários registros em uma única estrutura e realizar operações de cadastro, consulta, atualização e exclusão. Sua utilização facilita o gerenciamento da frota, permitindo percorrer os registros e localizar veículos por meio de seus identificadores (IDs).

**Fila – Gerenciamento dos caminhões**

A fila foi escolhida para representar os caminhões que aguardam atendimento no porto, pois esse processo precisa respeitar a ordem de chegada. Sua implementação segue o princípio FIFO (First In, First Out), garantindo que o primeiro caminhão cadastrado seja o primeiro a ser atendido.

**Pilha – Gerenciamento dos contêineres**

A pilha foi escolhida para representar o armazenamento e a retirada dos contêineres, seguindo o princípio LIFO (Last In, First Out). Dessa forma, o último contêiner inserido é o primeiro a ser retirado, permitindo simular o funcionamento de uma estrutura de empilhamento.

**Árvore – Gerenciamento das rotas entre portos**

A árvore foi escolhida porque permite representar relações hierárquicas entre os portos e suas rotas. Sua estrutura possibilita que um porto possua diferentes portos conectados, formando ramificações e permitindo organizar os caminhos de maneira hierárquica. No projeto, essa estrutura foi implementada utilizando dicionários aninhados.

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa (usa apenas o módulo `queue` da biblioteca padrão)

## Como executar

```bash
python main.py
```

O sistema abre um menu principal interativo, e a navegação é feita digitando o número da opção desejada.

## Funcionalidades

### Menu principal

```
1 - Gerenciar frota de veículos
2 - Gerenciar fila de caminhões
3 - Gerenciar pilha de contêineres
4 - Gerenciar árvore de rotas
5 - Salvar dados
6 - Carregar dados
7 - Sair
```

### 1. Frota de veículos (lista)

CRUD completo de veículos. Cada veículo tem ID, placa, modelo, transportadora e motorista.

- Cadastrar (não permite ID duplicado)
- Listar
- Consultar por ID
- Atualizar por ID
- Excluir por ID

### 2. Fila de caminhões (fila FIFO)

Os caminhões são atendidos na ordem de chegada. Cada caminhão tem ID, placa, transportadora e motorista.

- Cadastrar caminhão na fila (não permite ID duplicado)
- Listar caminhões na fila
- Consultar a situação da fila (quantidade e se está vazia)
- Atualizar caminhão por ID
- Excluir caminhão por ID
- Atender caminhão (remove o primeiro da fila)

### 3. Pilha de contêineres (pilha LIFO)

O último contêiner empilhado é o primeiro a sair. Cada contêiner tem ID, código, tipo e destino.

- Cadastrar contêiner (empilha no topo, sem ID duplicado)
- Listar contêineres (do topo para a base)
- Consultar a pilha (quantidade e ID do topo)
- Atualizar o contêiner do topo
- Excluir contêiner por ID (a ordem dos demais é preservada)
- Retirar contêiner (remove o do topo)

### 4. Árvore de rotas (árvore)

Representa as ligações entre portos, em que cada porto pode ter vários portos filhos.

- Cadastrar rota: o primeiro porto, sem porto de origem, vira a raiz (só pode existir uma raiz). Os demais são cadastrados informando o porto de origem
- Listar rotas (exibição hierárquica com indentação)
- Consultar um porto e os portos ligados a ele
- Atualizar (renomear) um porto
- Excluir um porto (remove também toda a sua subárvore)

Os nomes de portos não podem se repetir na árvore.

## Persistência de dados

As opções **Salvar dados** e **Carregar dados** gravam e leem o arquivo `dados_sistema.txt`, na mesma pasta do programa. Cada linha começa com um prefixo que indica o tipo do registro, e os campos são separados por `|`:

```
LISTA|id|placa|modelo|transportadora|motorista
FILA|id|placa|transportadora|motorista
PILHA|id|codigo|tipo|destino
ARVORE|porto_raiz|porto_filho|porto_neto|...
```

Na árvore, cada linha guarda o caminho completo da raiz até uma folha. Ao carregar, a estrutura é reconstruída a partir desses caminhos.

**Atenção:** carregar os dados substitui tudo o que está na memória naquele momento.

## Estrutura do código

O projeto está em um único arquivo, `main.py`, organizado em blocos:

1. Estruturas globais: `frota`, `fila_caminhoes`, `pilha_conteineres` e `rotas`
2. Funções de cada módulo (cadastrar, listar, consultar, atualizar, excluir)
3. Funções de persistência: `salvar_dados`, `carregar_dados`, `salvar_arvore` e `carregar_arvore`
4. Funções auxiliares da árvore: `localizar_porto` e `localizar_pai` (busca recursiva)
5. Submenus: `menu_frota`, `menu_fila`, `menu_pilha` e `menu_arvore`
6. `menu_principal`, que é o ponto de entrada

## Limitações conhecidas

- **Entradas numéricas sem validação:** digitar texto onde se espera número (opções de menu e IDs) gera um erro e encerra o programa.
- **Carregar sem arquivo:** usar "Carregar dados" antes de salvar pela primeira vez gera erro, pois `dados_sistema.txt` ainda não existe. Além disso, os dados em memória já foram apagados nesse ponto.
- **Caractere `|` nos dados:** como é o separador do arquivo, usá-lo em placa, nome, destino ou nome de porto corrompe o salvamento.
- **Árvore sem raiz vazia:** um porto só é salvo como parte de um caminho até uma folha. A estrutura continua consistente, mas o formato não registra nós de forma independente.
- **Sem controle de arquivo aberto:** o arquivo é aberto e fechado manualmente, sem `with`. Um erro no meio da gravação pode deixá-lo incompleto.

## Possíveis melhorias

- Validar entradas com `try/except`
- Usar `with open(...)` na leitura e gravação de arquivos
- Usar `collections.deque` no lugar de `queue.Queue` para facilitar listagem e exclusão na fila
- Separar o código em módulos (`frota.py`, `fila.py`, `pilha.py`, `rotas.py`)
- Trocar o formato `|` por JSON ou CSV

