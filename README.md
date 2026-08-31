## PACOTE DE EXERCÍCIOS: 30 FUNÇÕES EM PYTHON PARA TREINAMENTO
### Este arquivo contém 30 funções simples divididas em categorias:
- Matemática e Lógica Básica
- Manipulação de Listas e Laços de Repetição (For/While)
- Gamificação e RPG (Para aplicar a lógica em mecânicas de jogos)

Cada função possui comentários explicando o que ela faz, os parâmetros que recebe e o que retorna. É um excelente material para os alunos importarem em seus próprios projetos e testarem os resultados!


## Funções em Python para Treinamento de Lógica

Este repositório contém uma coleção de 30 funções simples e práticas em Python, desenvolvidas para ajudar estudantes e iniciantes a praticarem a modularização do código, a importação de arquivos e a lógica de programação.

O arquivo principal `exercicios_funcoes.py` pode ser baixado e importado nos seus projetos para que você possa explorar e testar cada função.

## Categorias de Funções

Para facilitar o aprendizado, as funções foram organizadas em três categorias de complexidade progressiva:

### 1. Matemática e Lógica Básica
Funções para praticar operadores lógicos, operações matemáticas e retornos simples.
- Verificação de números pares, ímpares, positivos, negativos e primos.
- Cálculos básicos: dobro, média aritmética, maior/menor de dois valores.
- Conversão de temperaturas (Celsius para Fahrenheit).

### 2. Listas e Laços de Repetição (FOR / WHILE)
Funções que envolvem iterações, manipulação de coleções e lógica de busca.
- Soma de elementos, busca do maior valor, contagem de números pares.
- Filtragem de positivos, multiplicação de itens da lista, inversão de listas usando `while`.
- Verificação de presença, geração de tabuada, contagem de vogais e remoção de duplicatas.

### 3. Gamificação e RPG (A Lógica de Imperiall)
Funções que aplicam a lógica de programação a mecânicas divertidas de jogos (com leve inspiração no sistema Imperiall World!).
- Cálculo de dano (ataque vs defesa), cálculo de dano crítico.
- Verificação de nível para equipar itens, filtragem de bestiário perigoso.
- Aplicação de poção de cura, contagem de itens na mochila, cálculo de XP ganho em batalha.
- Verificação de subida de nível, simulação de rolagem de dados (`random`) e sorteio de *loot*.

## Como Usar

A melhor forma de aprender é colocando a mão na massa! Siga os passos abaixo para testar as funções:

1.  **Faça o Download:** Baixe o arquivo `exercicios_funcoes.py` e coloque-o na mesma pasta do seu projeto.
2.  **Crie seu Arquivo de Teste:** Crie um novo arquivo, por exemplo, `main.py`.
3.  **Importe e Teste:** Use a declaração `import` para trazer as funções para o seu arquivo principal e brinque com os resultados.

**Exemplo Prático (no seu arquivo `main.py`):**

```python
# Importa o arquivo com as funções
import exercicios_funcoes as ex

# Testando Matemática
numero_secreto = 17
if ex.eh_primo(numero_secreto):
    print(f"O número {numero_secreto} é primo!")
else:
    print(f"O número {numero_secreto} não é primo.")

# Testando Listas
minhas_notas = [8.5, 9.0, 7.5, 10.0]
media = ex.soma_elementos_lista(minhas_notas) / len(minhas_notas)
print(f"Sua média é: {media}")

# Testando RPG
dano = ex.calcula_dano_ataque(poder_ataque=25, armadura_inimigo=10)
print(f"Você causou {dano} pontos de dano no monstro!")
