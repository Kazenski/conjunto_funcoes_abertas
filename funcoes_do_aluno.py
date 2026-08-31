# ==============================================================================
# PACOTE DE EXERCÍCIOS: 30 FUNÇÕES EM PYTHON PARA TREINAMENTO
# ==============================================================================
# Este arquivo contém 30 funções simples divididas em categorias:
# - Matemática e Lógica Básica
# - Manipulação de Listas e Laços de Repetição (For/While)
# - Gamificação e RPG (Para aplicar a lógica em mecânicas de jogos)
#
# Cada função possui comentários explicando o que ela faz, os parâmetros que 
# recebe e o que retorna. É um excelente material para os alunos importarem
# em seus próprios projetos e testarem os resultados!
# ==============================================================================

import random

# ------------------------------------------------------------------------------
# CATEGORIA 1: MATEMÁTICA E LÓGICA BÁSICA
# ------------------------------------------------------------------------------

def eh_par(numero):
    '''
    Verifica se um número é par.
    Parâmetros:
      numero (int): O número a ser verificado.
    Retorno:
      bool: True se for par, False caso contrário.
    '''
    return numero % 2 == 0


def eh_impar(numero):
    '''
    Verifica se um número é ímpar.
    Parâmetros:
      numero (int): O número a ser verificado.
    Retorno:
      bool: True se for ímpar, False caso contrário.
    '''
    return numero % 2 != 0


def eh_positivo(numero):
    '''
    Verifica se o número é estritamente positivo (maior que zero).
    Parâmetros:
      numero (float/int): O valor a ser avaliado.
    Retorno:
      bool: True se positivo, False se zero ou negativo.
    '''
    return numero > 0


def eh_negativo(numero):
    '''
    Verifica se o número é negativo (menor que zero).
    Parâmetros:
      numero (float/int): O valor a ser avaliado.
    Retorno:
      bool: True se negativo, False se zero ou positivo.
    '''
    return numero < 0


def eh_primo(numero):
    '''
    Verifica se um número inteiro é primo.
    Parâmetros:
      numero (int): O número a ser testado.
    Retorno:
      bool: True se for primo, False caso contrário.
    '''
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def calcula_dobro(numero):
    '''
    Calcula o dobro de um valor.
    Parâmetros:
      numero (float/int): O número base.
    Retorno:
      float/int: O dobro do número.
    '''
    return numero * 2


def maior_de_dois(a, b):
    '''
    Compara dois números e retorna o maior deles.
    Parâmetros:
      a, b (float/int): Os números a serem comparados.
    Retorno:
      float/int: O maior número.
    '''
    if a > b:
        return a
    return b


def menor_de_dois(a, b):
    '''
    Compara dois números e retorna o menor deles.
    Parâmetros:
      a, b (float/int): Os números a serem comparados.
    Retorno:
      float/int: O menor número.
    '''
    if a < b:
        return a
    return b


def calcula_media(nota1, nota2, nota3):
    '''
    Calcula a média aritmética de 3 notas.
    Parâmetros:
      nota1, nota2, nota3 (float): As notas do aluno.
    Retorno:
      float: O valor da média.
    '''
    return (nota1 + nota2 + nota3) / 3


def celsius_para_fahrenheit(celsius):
    '''
    Converte uma temperatura de Celsius para Fahrenheit.
    Parâmetros:
      celsius (float): Temperatura em graus Celsius.
    Retorno:
      float: Temperatura equivalente em Fahrenheit.
    '''
    return (celsius * 9/5) + 32


# ------------------------------------------------------------------------------
# CATEGORIA 2: LISTAS E LAÇOS DE REPETIÇÃO (FOR / WHILE)
# ------------------------------------------------------------------------------

def soma_elementos_lista(lista_numeros):
    '''
    Soma todos os valores numéricos presentes em uma lista usando um laço for.
    Parâmetros:
      lista_numeros (list): Uma lista contendo números.
    Retorno:
      float/int: A soma total.
    '''
    soma = 0
    for num in lista_numeros:
        soma += num
    return soma


def encontra_maior_na_lista(lista_numeros):
    '''
    Percorre a lista e encontra o maior valor armazenado.
    Parâmetros:
      lista_numeros (list): Uma lista de números (não deve ser vazia).
    Retorno:
      float/int: O maior valor encontrado.
    '''
    if not lista_numeros:
        return None
    maior = lista_numeros[0]
    for num in lista_numeros:
        if num > maior:
            maior = num
    return maior


def conta_numeros_pares(lista_numeros):
    '''
    Conta quantos números pares existem dentro da lista.
    Parâmetros:
      lista_numeros (list): Lista de números inteiros.
    Retorno:
      int: A quantidade de números pares.
    '''
    contador = 0
    for num in lista_numeros:
        if num % 2 == 0:
            contador += 1
    return contador


def filtra_numeros_positivos(lista_numeros):
    '''
    Cria uma nova lista contendo apenas os números maiores que zero.
    Parâmetros:
      lista_numeros (list): Lista mista de números.
    Retorno:
      list: Uma nova lista apenas com os positivos.
    '''
    positivos = []
    for num in lista_numeros:
        if num > 0:
            positivos.append(num)
    return positivos


def multiplica_lista(lista_numeros, multiplicador):
    '''
    Multiplica todos os elementos da lista por um valor específico.
    Parâmetros:
      lista_numeros (list): Lista de números.
      multiplicador (int/float): O valor pelo qual multiplicar.
    Retorno:
      list: Uma nova lista com os valores multiplicados.
    '''
    resultado = []
    for num in lista_numeros:
        resultado.append(num * multiplicador)
    return resultado


def inverte_lista(lista):
    '''
    Recebe uma lista e retorna os elementos de trás para frente usando while.
    Parâmetros:
      lista (list): Uma lista qualquer.
    Retorno:
      list: A lista em ordem invertida.
    '''
    lista_invertida = []
    indice = len(lista) - 1
    while indice >= 0:
        lista_invertida.append(lista[indice])
        indice -= 1
    return lista_invertida


def verifica_elemento_presente(lista, elemento_procurado):
    '''
    Verifica se um determinado elemento existe na lista.
    Parâmetros:
      lista (list): A lista onde será feita a busca.
      elemento_procurado (any): O valor a ser buscado.
    Retorno:
      bool: True se encontrar, False caso contrário.
    '''
    for item in lista:
        if item == elemento_procurado:
            return True
    return False


def tabuada_completa(numero):
    '''
    Gera uma lista com os resultados da tabuada de 1 a 10 de um número.
    Parâmetros:
      numero (int): O número base da tabuada.
    Retorno:
      list: Uma lista contendo os 10 resultados.
    '''
    resultados = []
    for i in range(1, 11):
        resultados.append(numero * i)
    return resultados


def conta_vogais(texto):
    '''
    Percorre uma string (texto) e conta quantas vogais ela possui.
    Parâmetros:
      texto (str): O texto a ser analisado.
    Retorno:
      int: O número de vogais encontradas.
    '''
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


def remove_duplicatas(lista):
    '''
    Gera uma nova lista removendo os itens que estão repetidos.
    Parâmetros:
      lista (list): Uma lista com possíveis elementos repetidos.
    Retorno:
      list: Uma nova lista apenas com itens únicos.
    '''
    lista_unica = []
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)
    return lista_unica


# ------------------------------------------------------------------------------
# CATEGORIA 3: GAMIFICAÇÃO E RPG (Aplicando Lógica)
# ------------------------------------------------------------------------------

def calcula_dano_ataque(poder_ataque, armadura_inimigo):
    '''
    Calcula o dano causado em um monstro, garantindo que não seja negativo.
    Parâmetros:
      poder_ataque (int): O ataque base do herói.
      armadura_inimigo (int): A defesa do monstro.
    Retorno:
      int: O dano final causado (mínimo de 0).
    '''
    dano = poder_ataque - armadura_inimigo
    if dano < 0:
        return 0
    return dano


def calcula_dano_critico(dano_base, eh_critico):
    '''
    Dobra o dano caso o ataque seja considerado um acerto crítico.
    Parâmetros:
      dano_base (int): O dano normal já calculado.
      eh_critico (bool): True se for golpe crítico, False se normal.
    Retorno:
      int: O dano com ou sem o multiplicador crítico.
    '''
    if eh_critico:
        return dano_base * 2
    return dano_base


def pode_equipar_item(nivel_personagem, nivel_minimo_item):
    '''
    Verifica se o personagem tem nível suficiente para equipar uma arma.
    Parâmetros:
      nivel_personagem (int): Nível atual do herói.
      nivel_minimo_item (int): Nível exigido pelo equipamento.
    Retorno:
      bool: True se puder equipar, False caso contrário.
    '''
    return nivel_personagem >= nivel_minimo_item


def filtra_bestiario_perigoso(lista_monstros, nivel_ameaca_minimo):
    '''
    Filtra um bestiário para retornar apenas os monstros mais fortes.
    Parâmetros:
      lista_monstros (list): Lista de listas (ex: [['Goblin', 2], ['Dragão', 50]])
      nivel_ameaca_minimo (int): Nível mínimo para ser considerado perigoso.
    Retorno:
      list: Uma nova lista apenas com o nome dos monstros perigosos.
    '''
    perigosos = []
    for monstro in lista_monstros:
        nome = monstro[0]
        nivel = monstro[1]
        if nivel >= nivel_ameaca_minimo:
            perigosos.append(nome)
    return perigosos


def aplica_pocao_cura(vida_atual, vida_maxima, valor_cura):
    '''
    Aplica cura ao personagem sem deixar ultrapassar a vida máxima.
    Parâmetros:
      vida_atual (int): HP atual do personagem.
      vida_maxima (int): Limite máximo de HP do personagem.
      valor_cura (int): Quanto a poção recupera.
    Retorno:
      int: A nova vida do personagem após o uso da poção.
    '''
    nova_vida = vida_atual + valor_cura
    if nova_vida > vida_maxima:
        return vida_maxima
    return nova_vida


def conta_itens_mochila(mochila, nome_item):
    '''
    Conta quantas unidades de um item específico o herói tem na mochila.
    Parâmetros:
      mochila (list): Lista com os nomes dos itens guardados.
      nome_item (str): O item que estamos procurando (ex: "Poção de Vida").
    Retorno:
      int: A quantidade desse item na mochila.
    '''
    quantidade = 0
    for item in mochila:
        if item == nome_item:
            quantidade += 1
    return quantidade


def calcula_xp_batalha(lista_inimigos_derrotados, xp_por_inimigo):
    '''
    Calcula a experiência total ganha ao fim de um combate.
    Parâmetros:
      lista_inimigos_derrotados (list): Lista com os inimigos vencidos.
      xp_por_inimigo (int): Quanto de XP cada monstro concede.
    Retorno:
      int: O total de experiência acumulada.
    '''
    total_inimigos = len(lista_inimigos_derrotados)
    return total_inimigos * xp_por_inimigo


def verifica_subida_de_nivel(xp_atual, xp_necessaria):
    '''
    Checa se o personagem acumulou experiência suficiente para subir de nível.
    Parâmetros:
      xp_atual (int): A experiência total do personagem.
      xp_necessaria (int): O limiar para alcançar o próximo nível.
    Retorno:
      bool: True se subiu de nível, False se ainda falta XP.
    '''
    return xp_atual >= xp_necessaria


def rola_dado(faces):
    '''
    Simula a rolagem de um dado de RPG (D4, D6, D20, etc).
    Parâmetros:
      faces (int): O número de lados do dado (ex: 20 para um D20).
    Retorno:
      int: Um número sorteado entre 1 e o número de faces.
    '''
    return random.randint(1, faces)


def sorteia_loot(tabela_loot):
    '''
    Sorteia um item aleatório deixado por um inimigo derrotado.
    Parâmetros:
      tabela_loot (list): Uma lista contendo os itens possíveis de cair.
    Retorno:
      str: O nome do item sorteado (ou None se a lista for vazia).
    '''
    if not tabela_loot:
        return None
    indice_sorteado = random.randint(0, len(tabela_loot) - 1)
    return tabela_loot[indice_sorteado]
