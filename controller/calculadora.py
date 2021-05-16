"""Calculadora de número de visualizações esperado para anúncios

Este script fornece a estimativa de número de visualizações que um
anúncio receberá para um dado investimento em reais.

É necessário que o módulo `math` esteja instalado no ambiente em que
este script está sendo executado.

Este arquivo também pode ser importado como módulo e fornece as
seguintes funções:

    * calcular_visualizacoes_por_investimento:
    * calcular_cliques_por_visualizacao:
    * calcular_compartihamentos_por_cliques:
    * calcular_visualizacoes_por_compartilhamento:
    * calcula_total_visualizacoes:
    * main: função principal do script
"""

from math import floor

def calcular_visualizacoes_por_investimento(i):
    """Calcula número inicial de visualizações
    
    Parâmetros
    ----------
    i: float
        Valor do investimento inicial, em reais e centavos
    
    Retorna
    -------
    v_anuncio_original: int
        Número de visualizações do (...)
    """

    v_anuncio_original = floor(i * 30)
    return v_anuncio_original

def calcular_cliques_por_visualizacao(v):
    """Calcula o número de cliques a partir do número de visualizações
    
    Parâmetros
    ----------
    v: int
        Número de visualizações
    
    Retorna
    -------
    cliques: int
        Número de cliques resultantes
    """

    cliques = floor(v * (12/100)) # Cada 100 visualizações gera 12 cliques
    return cliques

def calcular_compartihamentos_por_cliques(c):
    """Calcula número de compartilhamentos a partir do número de cliques
    
    Parâmetros
    ----------
    c: int
        Número de cliques
    
    Retorna
    -------
    compartilhamentos: int
        Número de compartilhamentos
    """

    # Cada 20 cliques resultam em 3 compartilhamentos
    compartilhamentos = floor(c * (3/20))
    return compartilhamentos

def calcular_visualizacoes_por_compartilhamento(cp):
    """Calcula o número de visualizações esperadas a partir de um
       número de compartilhamentos
    
    Parâmetros
    ----------
    cp: int
        Número de compartilhamentos
    
    Retorna
    -------
    visualizacoes_por_compartilhamento: int
        Número de visualizações por compartilhamento
    """

    visualizacoes_por_compartilhamento = floor(40*cp)
    return visualizacoes_por_compartilhamento

def calcula_totais(i,n_compartilhamentos=3):
    """Calcula o total de visualizações, cliques e compartilhamentos
    no anúncio para dado investimento
    
    Parâmetros
    ----------
    i: float
        Valor do investimento inicial, em reais e centavos
    n_compartilhamentos: int, opcional
        Número máximo de compartilhamentos consecutivos do anúncio. Default: 3
    
    Retorna
    -------
    Dicionario contendo o total de visualizações, cliques e compartilhamentos.
    total = {'visualizacoes': int, 'cliques': int, 'compartilhamentos': int}
        Número total de visualizações no anúncio
    """

    # Passo 1: Calcula número de visualizações no anúncio original
    visualizacoes = calcular_visualizacoes_por_investimento(i)
    compartilhamentos_total = 0
    cliques_total = 0
    visualizacoes_total = visualizacoes
    #n_compartilhamentos = número máximo de compartilhamentos consecutivos
    # 1ª pessoa vê anuncio original -> compartilha (n=1)
    # 2ª pessoa vê o compartilhamento da 1ª -> compartilha (n=2)
    # 3ª pessoa vê o compartilhamento da 2ª -> compartilha (n=3)
    # 4ª pessoa vê o compartilhamento da 3ª -> não compartilha e fecha o ciclo
    n_compartilhamentos = 3
    #Passo 2: calculando o numero de visualizações em um ciclo de
    # compartilhamento usando um laço de repetição em que n varia de 0 a 2,
    # ou seja, completando 3 compartilhamentos
    for n in range(n_compartilhamentos):
        #calcular nº de cliques a partir das visualizacoes
        cliques = calcular_cliques_por_visualizacao(visualizacoes)
        cliques_total += cliques
        #calcular nº de compartilhamentos a partir dos cliques
        compartilhamentos = calcular_compartihamentos_por_cliques(cliques)
        compartilhamentos_total += compartilhamentos
        #somar o nº de visualizacoes do compartilhamento ao numero anterior
        #de visualizacoes
        visualizacoes = calcular_visualizacoes_por_compartilhamento(\
            compartilhamentos)
        visualizacoes_total += visualizacoes
        n += 1
    total = {'visualizacoes': visualizacoes_total, 'cliques': cliques_total,\
        'compartilhamentos': compartilhamentos_total}
    return total

def main():
    print('\n---------- Calculadora de Anúncios ----------\n')
    investimento = float(input('Informe o valor a ser investido no anúncio: R$ '))
    total = calcula_totais(investimento)
    visualizacoes = total['visualizacoes']
    print('>> Previsão de visualizações para ', investimento,
    ' reais investidos: ', visualizacoes)

if __name__ == '__main__':
    main()











